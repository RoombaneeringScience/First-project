import freenect
import matplotlib.pyplot as plt
import numpy as np
import math
import create2api
import cv2
import sys

#initalize the create 2
bot = create2api.Create2()
bot.start()
bot.safe()

#global robot coordinates
X = 0
Y = 0
theta = 0

#array to track position over time
pos = []

#this is the angle of one kinect pixel
PIXEL_ANGLE = 0.001553

landmarks = {}

#initalizing kinect by running this before any other code
print "initalizing Kinect - WARNING you may need to run this multiple times."

try:
    depth, timestamp = freenect.sync_get_depth()
except KeyboardInterrupt:
    print "Closing"
    sys.exit()

#initalizing the state vector, note there are no landmarks yet
X = np.matrix([[X, Y, theta]])
