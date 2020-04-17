from googleapiclient.http import MediaIoBaseDownload
from apiclient import errors
import io
import os

def main(item, service):  
    
    print("\nDeleting Old File...")
    try:
        service.files().delete(fileId=item['id']).execute()
        print('Sermon.mp3 Deleted')
        
    except(errors.HttpError, error):
        print('An error occurred: %s' % error)
                