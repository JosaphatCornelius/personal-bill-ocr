from pipeline.ocr import ocr
from pipeline.ingest import get_pil_image_from_drive

def main():
    # 1. Path to your downloaded Google Cloud Service Account JSON key file
    SERVICE_ACCOUNT_FILE = 'path/to/your/credentials.json'

    # 2. Define the permissions (scopes) your script needs (Read-only here)
    SCOPES = ['https://googleapis.com']

    # 3. Authenticate using the credentials file
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # 4. Build and return the "service" object
    service = build('drive', 'v3', credentials=creds)

    bill_image = get_pil_image_from_drive(service, "id")
    ocr()


if __name__ == '__main__':
    main()
