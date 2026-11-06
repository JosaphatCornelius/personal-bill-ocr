import os
import json
import traceback
import numpy as np
from urllib.error import HTTPError
from pipeline.ingest import get_pil_image_from_drive, get_items_from_drive_folder
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from paddleocr import PaddleOCR
from dotenv import load_dotenv

SCOPES = ["https://www.googleapis.com/auth/drive"]
load_dotenv(verbose=True)


def main():
    folder_id = os.getenv("GDRIVE_FOLDER_ID")
    service_account_info = json.loads(os.getenv("GDRIVE_CREDENTIAL"))
    credentials = Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES
    )
    drive_service = build("drive", "v3", credentials=credentials)

    pipeline = PaddleOCR(use_textline_orientation=True, lang="id")

    try:
        images = get_items_from_drive_folder(drive_service, folder_id)
        for img in images:
            bill_image = get_pil_image_from_drive(drive_service, img["id"])
            img_np = np.array(bill_image)
            ocr_result = pipeline.predict(img_np)

            if not ocr_result:
                print(f"Skipping {img['name']}: no result returned.")
                continue

            for res in ocr_result:
                texts = res["rec_texts"]
                scores = res["rec_scores"]

                if not texts:
                    print(f"Skipping {img['name']}: no text detected.")
                    continue

                print(f"--- {img['name']} ---")
                for text, confidence in zip(texts, scores):
                    print(f"Detected text: {text} ({confidence:.2f})")

    except HTTPError as error:
        print(f"HTTP error occurred: {error}")
    except Exception:
        traceback.print_exc()  # shows the real line instead of just the message


if __name__ == "__main__":
    main()
