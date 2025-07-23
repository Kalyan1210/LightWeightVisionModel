# LightWeightVisionModel
Flexible and powerful image analysis

# Image Understanding CLI 

A powerful command-line interface for AI-powered image analysis and understanding. Built with PyTorch and Transformers, this tool provides easy-to-use commands for analyzing images with state-of-the-art vision-language models.

## Features 

- **Single Image Analysis** - Analyze individual images with AI descriptions
- **Batch Processing** - Process entire directories of images at once
- **Web Interface** - Launch a Streamlit web app for interactive use
- **Multiple Model Support** - Use different pre-trained models
- **Export Results** - Save analysis results to JSON files
- **Cross-Platform** - Works on Windows, macOS, and Linux

## Quick Start Here:

### Installation

#### Option 1: Automatic Installation (Recommended)

**Linux/macOS:**
```bash
chmod +x install.sh
./install.sh
```

**Windows:**
```cmd
install.bat
```

#### Option 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/image-understanding-cli.git
cd image-understanding-cli

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install CLI tool
pip install -e .
```

#### Option 3: Using Make (Linux/macOS)

```bash
make install
```

### Basic Usage

```bash
# Show help
image-cli --help

# Analyze a single image
image-cli single path/to/image.jpg

# Analyze with custom text prompt
image-cli single image.jpg --text "What's in this image?"

# Process all images in a directory
image-cli batch ./my_images/

# Save results to file
image-cli batch ./my_images/ --output results.json

# Launch web interface
image-cli streamlit

# Show system information
image-cli info
```

## Commands 📋

### `single` - Analyze Single Image

Analyze a single image and get an AI-generated description.

```bash
image-cli single <image_path> [options]
```

**Options:**
- `--text, -t` - Add text prompt for guided analysis
- `--model, -m` - Specify model to use (default: microsoft/git-base)

**Examples:**
```bash
# Basic analysis
image-cli single photo.jpg

# With text prompt
image-cli single photo.jpg --text "Describe the colors in this image"

# Using different model
image-cli single photo.jpg --model "Salesforce/blip-image-captioning-base"
```

### `batch` - Process Multiple Images

Process all images in a directory and optionally save results.

```bash
image-cli batch <directory> [options]
```

**Options:**
- `--output, -o` - Output file for results (JSON format)
- `--model, -m` - Specify model to use

**Examples:**
```bash
# Process directory
image-cli batch ./photos/

# Save results to file
image-cli batch ./photos/ --output analysis_results.json
```

### `streamlit` - Web Interface

Launch an interactive web interface for image analysis.

```bash
image-cli streamlit [options]
```

**Options:**
- `--port, -p` - Port number (default: 8501)

**Example:**
```bash
# Launch on default port
image-cli streamlit

# Launch on custom port
image-cli streamlit --port 8080
```

### `info` - System Information

Display system information and check dependencies.

```bash
image-cli info
```

## Supported Image Formats 🖼️

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Models 🤖

The CLI supports various pre-trained models:

- `microsoft/git-base` (default) - General image captioning
- `Salesforce/blip-image-captioning-base` - BLIP model for captioning
- `microsoft/git-large` - Larger version with better accuracy
- `Salesforce/blip-image-captioning-large` - Large BLIP model

## Configuration ⚙️

### Environment Variables

You can set these environment variables to customize behavior:

```bash
export IMAGE_CLI_MODEL="microsoft/git-base"  # Default model
export IMAGE_CLI_DEVICE="cuda"               # Force device (cuda/cpu)
export IMAGE_CLI_LOG_LEVEL="INFO"            # Logging level
```

### Config File (Optional)

Create a `config.yaml` file in your project directory:

```yaml
model:
  name: "microsoft/git-base"
  device: "auto"  # auto, cuda, cpu
  
output:
  format: "json"  # json, csv, txt
  timestamp: true
  
logging:
  level: "INFO"
  file: "image_cli.log"
```

## Examples 📚

### Analyze Family Photos

```bash
# Process all family photos and save results
image-cli batch ~/Pictures/Family/ --output family_analysis.json

# View specific photo
image-cli single ~/Pictures/vacation.jpg --text "What activities are shown?"
```

### Content Moderation

```bash
# Analyze images for content
image-cli batch ./uploads/ --text "Describe any inappropriate content" --output moderation.json
```

### E-commerce Product Analysis

```bash
# Analyze product images
image-cli batch ./products/ --text "Describe this product" --output product_descriptions.json
```

## Development 🛠️

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/image-understanding-cli.git
cd image-understanding-cli

# Install in development mode
make dev

# Run tests
make test

# Format code
make format

# Run linter
make lint
```

### Project Structure

```
image-understanding-cli/
├── cli.py              # Main CLI script
├── app.py             # Streamlit web app
├── requirements.txt   # Python dependencies
├── setup.py          # Package setup
├── Makefile          # Build commands
├── install.sh        # Linux/macOS installer
├── install.bat       # Windows installer
├── README.md         # This file
└── tests/            # Test files
    └── test_cli.py
```

### Adding New Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `make test`
6. Submit a pull request

## Troubleshooting 🔧

### Common Issues

**"No module named 'transformers'"**
```bash
pip install transformers
```

**CUDA out of memory**
```bash
# Force CPU usage
export IMAGE_CLI_DEVICE="cpu"
image-cli single image.jpg
```

**Permission denied on install.sh**
```bash
chmod +x install.sh
./install.sh
```

**Streamlit not found**
```bash
pip install streamlit
```

### Performance Tips

- Use GPU if available for faster processing
- Process images in smaller batches for large datasets
- Use smaller models for faster inference
- Resize large images before processing

## Contributing 🤝

Contributions are welcome! Please read our contributing guidelines and submit pull requests for any improvements.

### Areas for Contribution

- Additional model support
- Performance optimizations
- New output formats
- Better error handling
- Documentation improvements

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Built with [Transformers](https://huggingface.co/transformers/) by Hugging Face
- Uses [PyTorch](https://pytorch.org/) for deep learning
- Web interface powered by [Streamlit](https://streamlit.io/)
- Inspired by the amazing work of the computer vision community

## Support 💬

- Create an issue on GitHub for bug reports
- Star the repository if you find it useful
- Share with others who might benefit

---

**Happy analyzing! 🎉**
