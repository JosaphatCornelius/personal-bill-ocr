import os
import json
import traceback
from pipeline.ocr import text_extraction
from urllib.error import HTTPError
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from pipeline.ingest import load_images
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

    try:
        images = load_images(drive_service, folder_id)
        results = text_extraction(images)

        for name, lines in results.items():
            print(f"--- {name} ---")
            for line in lines:
                print(f"{line['text']} ({line['confidence']:.2f})")

    except HTTPError as error:
        print(f"HTTP error occurred: {error}")

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    main()
