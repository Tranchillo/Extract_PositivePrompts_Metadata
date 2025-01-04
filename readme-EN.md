# Extract Positive Prompts - Positive Prompts Extractor

This Python script is designed to extract positive prompts from metadata of PNG images generated with ComfyUI. The script analyzes all PNG images in the current directory and extracts positive prompts, saving them in separate text files.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone the repository or download the script

```bash
git clone https://github.com/Tranchillo/Extract_PositivePrompts_Metadata
cd Extract_PositivePrompts_Metadata
```

2. (Recommended) Create and activate a virtual environment

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required dependencies

```bash
pip install pillow
```

## Usage

1. Place the script in the same directory as the PNG images to be processed
2. Run the script:

```bash
python Extract_PositivePrompts_Metadata.py
```

The script will:
- Scan all PNG files in the current directory
- Extract positive prompts from metadata of images generated with ComfyUI
- Create a .txt file for each image containing the positive prompt
- The text file name will be the same as the original image but with .txt extension

## Output

For each successfully processed image, a .txt file containing the positive prompt will be created. The script will also display status messages in the terminal to indicate:
- Which files were successfully processed
- Which files don't contain positive prompts
- Any errors during processing

## Notes

- The script currently only supports PNG files
- Metadata must be in the specific format used by ComfyUI
- If an image doesn't contain valid metadata or positive prompts, an appropriate message will be displayed

## Troubleshooting

If you encounter errors while running the script, verify that:
- The images are in PNG format
- The images contain valid ComfyUI metadata
- Python and required dependencies are correctly installed
- The script is in the same directory as the images to be processed

## License

GNU General Public License v3.0
