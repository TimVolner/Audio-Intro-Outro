from __future__ import print_function
from googleapiclient.http import MediaIoBaseDownload
import io
import os

def download(file, service):  
    
    directory = os.getcwd()
    filename = directory + "\\media\\sermon_in.mp3"
   
    file_id = file['id']
    request = service.files().get_media(fileId=file_id)
    
    fh = open(filename, 'wb')
    
    print("\nDownloading...")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100) )   
    