import freenect
import matplotlib.pyplot as plt
import numpy as np
import math
import create2api

bot = create2api.Create2()
bot.start()
bot.safe()

X = 0
Y = 0

phi = 0.089

landmarks = {}

bot.drive_straight(100)
for j in range(10):
    depth, timestamp = freenect.sync_get_depth()
    print "Kinect Data Recived"
    data = depth[240]
    bot.get_packet(20)

    X = X + bot.sensor_state["distance"]
    print "Processing"
    for i in range(len(data)):
        print i
        if data[i] < 1900:
            angle = phi*(i-320)

            x_landmark = math.floor(data[i]*math.cos(angle)) + X
            y_landmark = math.floor(data[i]*math.sin(angle)) + Y

            landmarks[(x_landmark, y_landmark)] = timestamp

bot.drive_straight(0)
points = landmarks.keys()
x = [e[0] for e in points]
y = [e[1] for e in points]

plt.scattter(y,x)
plt.show()

bot.destory()
