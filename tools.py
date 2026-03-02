from Google import Create_Service # импортируем функцию из начального файла
import argparse


parser = argparse.ArgumentParser(description="Получение списка файлов из папки")
parser.add_argument("--amount", help="Введите количество файлов", required=True)
args = parser.parse_args()

CLIENT_SECRET_FILE = 'credentials.json' # путь до файла с данными клиента, которого создавали ранее в кратком руковдстве 
API_NAME  = 'drive' # название API системы
API_VERSION = 'v3' # версия API системы
SCOPES = ['https://www.googleapis.com/auth/drive'] # Доступ к командам и действиям

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

results = service.files().list(
    pageSize=args.amount,
    fields="files(id, name)",
    q=f"'1sFrxPxX0f_20V9_X0eVPEX-YT41eW_Zl' in parents"
).execute()

existing_files = {item['name']: item['id'] for item in results.get('files', [])}