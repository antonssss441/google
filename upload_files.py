import os
import mimetypes
from googleapiclient.http import MediaFileUpload
from tools import service, existing_files


def main():
    for root,dirs,files in os.walk('Google'):
        for file in files:
            filepath = os.path.join(root,file)
            mime_type, _ = mimetypes.guess_type(filepath)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            media = MediaFileUpload(filepath,mimetype=mime_type ,resumable=True)
            file_metadata = {
                'name': file,
                'parents': ['1sFrxPxX0f_20V9_X0eVPEX-YT41eW_Zl']
            }
            if file not in existing_files:
                service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                print(f'{file} загружен.')
            else:
                service.files().update(fileId=existing_files[file], media_body=media).execute()
                print(f'{file} обновлен.')


if __name__ == '__main__':
    main()