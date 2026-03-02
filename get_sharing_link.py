from tools import service, existing_files


def main():
    for existing_file in existing_files:
        permission = { 
            'type': 'anyone',
            'role': 'reader'
        }
        response_permission = service.permissions().create(fileId=existing_files[existing_file], body=permission).execute()
        response_share_link = service.files().get(fileId=existing_files[existing_file], fields='webViewLink').execute()['webViewLink']
        print(response_share_link)


if __name__ == '__main__':
    main()