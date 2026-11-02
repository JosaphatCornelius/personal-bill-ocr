import os
import json
from urllib.error import HTTPError
from pipeline.ocr import ocr
from pipeline.ingest import get_pil_image_from_drive, get_items_from_drive_folder
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
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
        images = get_items_from_drive_folder(drive_service, folder_id)
        for img in images:
            bill_image = get_pil_image_from_drive(drive_service, img["id"])
            result = ocr(bill_image)
            print(result)

    except HTTPError as error:
        print(f"An error occurred: {error}")
        return None

    except Exception as error:
        print(f"An error occurred: {error}")
        return None


if __name__ == '__main__':
    main()
