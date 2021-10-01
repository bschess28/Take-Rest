from plyer import notification
import time


def giveNotification():
     notification.notify( 
            title = "Take Rest", 
            message=" Its 25 minutes and you need to give rest to your eyes minimum for 5 minutes.\nDo AFK and get out of screen" , 
            timeout=30
        ) 

while True:
    giveNotification()
    time.sleep(1800)


