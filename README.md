# bill-ocr-pipeline

Build Status: In Development

This repository is a pipeline that reads photos of bills and receipts from a Google Drive folder and extracts their text using OCR. Instead of typing transaction details into my finance app by hand, the goal is to automate the whole flow, from a photo of a bill to a clean transaction in Firefly III.

## Tech Stack

* **OCR:** [PaddleOCR 3.2.2]
* **Ingestion:** [Google Drive API, Pillow]
* **Language:** [Python]
* **Planned:** [Firefly III]

## Current Status

* [x] Download images from a Google Drive folder
* [x] Extract text and confidence scores from each image with PaddleOCR
* [ ] Parse raw OCR lines into structured data (merchant, date, total, line items)
* [ ] Push parsed transactions to Firefly III
* [ ] Review step before posting, since OCR isn't always accurate
* [ ] Duplicate detection so re-running doesn't double-book transactions
* [ ] Tests, using synthetic receipts only

Right now the pipeline only prints the detected text and its confidence score. Nothing is written anywhere yet.

## Quick Start

Instructions to get the project running locally.

```bash
# Clone the repository
git clone https://github.com/JosaphatCornelius/bill-ocr-pipeline.git
cd bill-ocr-pipeline

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GDRIVE_FOLDER_ID=your-folder-id
GDRIVE_CREDENTIAL={"type": "service_account", ...}
```

*Note: `GDRIVE_CREDENTIAL` is the full service account JSON on a single line. The service account also needs access to the Drive folder you want to read. Never commit the `.env` file.*

## Usage

```bash
python main.py
```

Every image in the Drive folder is downloaded and run through OCR, and the detected text is printed with its confidence score.

## Project Structure

```
main.py             # entry point
pipeline/
  ingest.py         # Google Drive download -> PIL images
  ocr.py            # PaddleOCR text extraction
```

## Roadmap

* A `pipeline/parser.py` module for Indonesian receipt formats (e.g. `Rp 1.250.000`, `dd/mm/yyyy`)
* A `pipeline/firefly.py` module that posts transactions through the Firefly III API
* A `--dry-run` mode that prints the transaction payload instead of posting it
* `FIREFLY_URL` and `FIREFLY_TOKEN` environment variables for the integration

## Contributing & License

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Currently unlicensed. All rights reserved.
