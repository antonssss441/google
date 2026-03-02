import io
import os
from googleapiclient.http import MediaIoBaseDownload
from tools import service, existing_files


def main():
    for existing_file in existing_files:
        request = service.files().get_media(fileId=existing_files[existing_file])
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))
        os.makedirs('Downloads', exist_ok=True)
        fh.seek(0)
        with open(f"Downloads/{existing_file}", 'wb') as file:
            file.write(fh.read())  


if __name__ == '__main__':
    main()