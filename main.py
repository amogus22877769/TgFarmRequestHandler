from pyrogram import Client
import asyncio
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import pprint
import io

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'mindful-furnace-433013-p9-faafd585a99f.json'
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
results = service.files().list(pageSize=10,
                               fields="nextPageToken, files(id, name)").execute()
for result in results.get('files'):
    if(result.get('name') != "Request Storage"):
        f = open(result.get('name'), "w")
        f.close()
        file_id = result.get('id')
        request = service.files().get_media(fileId=file_id)
        filename = result.get('name')
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        service.files().delete(fileId=file_id).execute()
"""async def send_message(app):
        await app.send_message("yak8vlev", "сап")
apps = []
async def main():
        async with app:
                await app.send_message("yak8vlev", "сап")

for app in apps:
        app.run(main())"""
