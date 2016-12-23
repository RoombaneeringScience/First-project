from SimpleCV import *
import matplotlib.pyplot as plt
import numpy as np

cam = Kinect()


while True:
    depth = cam.getDepth()
    data = depth.getNumpy()

    print data.shape
