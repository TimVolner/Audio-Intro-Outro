import quickstart
import drive_download
import sermon_overlay
import drive_upload
import drive_delete
import time

while True:

    try:
        item, service = quickstart.main()
        valid = True
    except:
        valid = False
    
    if valid:
        drive_download.download(item, service)
        valid = sermon_overlay.main()
    
    #succeed = True
    
    if valid:
        drive_upload.main()
        
        drive_delete.main(item, service)
    
        print("\n**********Completed Overlay**********")
    
    time.sleep(15)