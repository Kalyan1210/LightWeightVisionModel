import streamlit as st
import torch
import clip
from PIL import Image
import numpy as np

# Load CLIP model and preprocessing
@st.cache_resource
def load_clip_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    return model, preprocess, device

try:
    model, preprocess, device = load_clip_model()
    model_loaded = True
except Exception as e:
    st.error(f"Failed to load CLIP model: {e}")
    model_loaded = False

# Function to predict descriptions and probabilities
def predict(image, descriptions):
    if not model_loaded:
        return "Model not loaded", 0.0
    
    try:
        image = preprocess(image).unsqueeze(0).to(device)
        text = clip.tokenize(descriptions).to(device)

        with torch.no_grad():
            image_features = model.encode_image(image)
            text_features = model.encode_text(text)

            logits_per_image, logits_per_text = model(image, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()

        best_idx = np.argmax(probs)
        return descriptions[best_idx], np.max(probs)
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return "Error in prediction", 0.0

# Streamlit app
def main():
    st.title("Image understanding model test")

    if not model_loaded:
        st.error("⚠️ Model failed to load. Please check the logs.")
        return

    # Instructions for the user
    st.markdown("---")
    st.markdown("### Upload an image to test how well the model understands it")

    # Upload image through Streamlit with a unique key
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"], key="uploaded_image")

    if uploaded_image is not None:
        try:
            # Convert the uploaded image to PIL Image
            pil_image = Image.open(uploaded_image).convert('RGB')

            # Display the image
            st.image(pil_image, caption="Uploaded Image.", use_column_width=True, width=200)
            
            # Instructions for the user
            st.markdown("### 2 Lies and 1 Truth")
            st.markdown("Write 3 descriptions about the image, 1 must be true.")

            # Get user input for descriptions
            description1 = st.text_input("Description 1:", placeholder='A red apple')
            description2 = st.text_input("Description 2:", placeholder='A car parked in a garage')
            description3 = st.text_input("Description 3:", placeholder='An orange fruit on a tree')

            descriptions = [description1, description2, description3]

            # Button to trigger prediction
            if st.button("Predict"):
                if all(descriptions):
                    with st.spinner("Making prediction..."):
                        # Make predictions
                        best_description, best_prob = predict(pil_image, descriptions)

                        # Display the highest probability description and its probability
                        st.write(f"**Best Description:** {best_description}")
                        st.write(f"**Prediction Probability:** {best_prob:.2%}")

                        # Display progress bar for the highest probability
                        if isinstance(best_prob, (int, float)) and 0 <= best_prob <= 1:
                            st.progress(float(best_prob))
                else:
                    st.warning("Please fill in all three descriptions!")
        
        except Exception as e:
            st.error(f"Error processing image: {e}")

if __name__ == "__main__":
    main()
