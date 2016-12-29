import freenect
import matplotlib.pyplot as plt
import numpy as np
import math
import create2api
import cv2

bot = create2api.Create2()
bot.start()
bot.safe()

X = 0
Y = 0

pos = []

phi = 0.001553

landmarks = {}
depth, timestamp = freenect.sync_get_depth()

bot.drive_straight(100)
for j in range(30):
    print "fetching kinect data"
    depth, timestamp = freenect.sync_get_depth()
    print "Kinect Data Recived"

    data = depth[240]
    bot.get_packet(0)

    X = X + bot.sensor_state["distance"]
    pos.append(X)
    print bot.sensor_state["distance"]
    print "Processing"
    for i in range(len(data)):
    	if data[i] < 1900:
        	angle = phi*(i-320)

            	x_landmark = math.ceil(data[i]*math.cos(angle)) 
            	y_landmark = math.ceil(data[i]*math.sin(angle))
            	landmarks[(x_landmark, y_landmark)] = timestamp




bot.drive_straight(0)
points = landmarks.keys()
x = [e[0] for e in points]
y = [e[1] for e in points]

<<<<<<< HEAD
plt.scattter(x,y)
=======
plt.scatter(y,x)
plt.scatter([0 for i in range(len(pos))], pos, color='red')
>>>>>>> origin/master
plt.show()
bot.destroy()
