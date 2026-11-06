import io
from googleapiclient.http import MediaIoBaseDownload
from PIL import Image


def get_image_bytes_from_drive(service, file_id):
    """Downloads the file from Drive and returns the raw binary bytes."""
    request = service.files().get_media(fileId=file_id)
    file_stream = io.BytesIO()
    downloader = MediaIoBaseDownload(file_stream, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    # Rewind the pointer to the beginning of the stream
    file_stream.seek(0)

    # Return raw binary data
    return file_stream.read()


def get_pil_image_from_drive(service, file_id):
    """Downloads the file from Drive and returns a PIL Image object."""
    image_bytes = get_image_bytes_from_drive(service, file_id)

    # Convert binary bytes back into a stream for PIL to read
    return Image.open(io.BytesIO(image_bytes)).convert("RGB")


def get_items_from_drive_folder(drive_service, folder_id):
    items = []
    page_token = None

    query = f"'{folder_id}' in parents and trashed=false"

    while True:
        results = drive_service.files().list(
            q=query,
            spaces="drive",
            fields="nextPageToken, files(id, name)",
            pageToken=page_token,
        ).execute()
        items.extend(results.get("files", []))
        page_token = results.get("nextPageToken", None)
        if not page_token:
            break

    if not items:
        print("No files found.")
        return []

    print("Found {} files.".format(len(items)))
    for item in items:
        print(item["name"])

    return items
