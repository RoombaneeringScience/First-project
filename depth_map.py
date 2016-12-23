from SimpleCV import *
import matplotlib.pyplot as plt
import numpy as np

cam = Kinect()
cam2 = SimpleCV.Camera()


while True:
    depth = cam.getDepth()
    pic = cam2.getImage()
    data = depth.getNumpy()
    pic.show()

    print data.shape
