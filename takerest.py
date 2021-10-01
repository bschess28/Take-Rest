from plyer import notification
import time


def giveNotification():
     notification.notify( 
            title = "Take Rest", 
            message=" Its 25 minutes and you need to give rest to your eyes minimum for 5 minutes.\nDo AFK and get out of screen" , 
            app_name = "Take Rest",
            ticker="Give rest to your eyes",
            timeout=25
        ) 


def sleep():
    time.sleep(1500)


while True:
    giveNotification()
    sleep()


