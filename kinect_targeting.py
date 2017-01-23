from SimpleCV import *
import create2api
import time
from pykalman import KalmanFilter
import numpy as np

kf = KalmanFilter()


cam = Kinect()
display = SimpleCV.Display()

X = np.array([0])
state_variance = np.array([1])
kinect_variance = np.array([10])




bot = create2api.Create2()
#Start the Create2
bot.start()
#Put the Create2 into 'safe' mode so we can drive it
bot.safe()

print "Powering on kinect"
bot.kinect_power()


while display.isNotDone():


    img = cam.getImage()
    depth = cam.getDepth()

    dist = img.colorDistance((255,0,0)).dilate(2).binarize(100)

    blobs = dist.findBlobs()
    if blobs:
        for blob in blobs:
            max_blob = blob
            max_blob.drawHull()
            dist.drawCircle((max_blob.x, max_blob.y), 5, SimpleCV.Color.BLUE, 2)
            #dist.drawText("Distance " + str(depth.getPixel(max_blob.x, max_blob.y)),(max_blob.x, max_blob.y))

    bot.get_packet(2)
    distance = bot.sensor_state['distance']


    #kf.filter_update()

    dist.show()
