# personal-bill-ocr

[![Status](https://img.shields.io/badge/status-in%20development-yellow)](https://github.com/JosaphatCornelius/personal-bill-ocr)

A pipeline that reads photos of bills and receipts from a Google Drive folder and extracts their text with OCR. The goal is to replace manual entry in my finance app, going from a photo of a bill to a clean transaction in Firefly III.

## Tech Stack

* **Core:** [Python, PaddleOCR 3.2.2 (Indonesian), Pillow]
* **Source:** [Google Drive API]
* **Target:** [Firefly III (planned)]

## Quick Start

Instructions to get the development environment running locally.

```bash
# Clone the repository
git clone https://github.com/JosaphatCornelius/personal-bill-ocr.git
cd personal-bill-ocr

# Install dependencies
pip install -r requirements.txt

# Create your env file from the example, then fill in your values
cp .env.example .env

# Run
python main.py
```

*Note: Ensure you have Python 3.9+ installed. Set up the necessary environment variables in a `.env` file before running. `GDRIVE_CREDENTIAL` is the full service account JSON on a single line, and the service account needs access to the Drive folder you want to read.*

## Usage

Put your bill images in the Google Drive folder set in `GDRIVE_FOLDER_ID`, then run `python main.py`. Each image is downloaded, run through OCR, and the detected text is printed with its confidence score. Parsing into structured data and posting to Firefly III are still in progress.

```
--- bill-01.jpg ---
Detected text: TOTAL 45.000 (0.97)
```

## Contributing & License

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Currently unlicensed. All rights reserved.
