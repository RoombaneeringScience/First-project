import create2api
import time
import json

#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array


if __name__ == "__main__":

    #Create a Create2. This will automatically try to connect to your
    #   robot over serial
    bot = create2api.Create2()
    #Start the Create2
    bot.start()
    #Put the Create2 into 'safe' mode so we can drive it
    bot.safe()
    bot.kinect_power()
    while 1:
        frame = get_video()
        cv2.imshow('RGB image',frame)
        k = cv2.waitKey(5)
        print k
        '''
        if keys[K_UP]:
            bot.drive_direct(100, 100)
        else if keys[K_DOWN]:
            bot.drive_direct(-100, -100)
        else if keys[K_LEFT]:
            bot.drive_direct(100, -100)
        else if keys[K_LEFT]:
            bot.drive_direct(-100, 100)
        else if keys[K_ESCAPE].
            bot.drive_straight(0)
            break
        '''
    bot.destroy()
