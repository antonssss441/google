from tools import service
import argparse


def main():
    parser = argparse.ArgumentParser(description="Создает вложенную папку")
    parser.add_argument("-n", "--name", help="Введите название папки", required=True)
    parser.add_argument("--id", help="Введите id папки, куда будет вложена папка", required=True)
    args = parser.parse_args()
    
    file_metadata = {
        "name": args.name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [args.id]
    }

    service.files().create(body=file_metadata, fields="id").execute()


if __name__ == '__main__':
    main()