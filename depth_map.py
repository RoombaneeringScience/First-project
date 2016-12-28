import freenect
import matplotlib.pyplot as plt
import numpy as np
import math
import create2api

bot = create2api.Create2()
bot.start()
bot.safe()

plt.ion()

X = 0
Y = 0

phi = 0.089

landmarks = {}


for x in range(100):
    depth, timestamp = freenect.sync_get_depth()
    data = depth[240]
    bot.get_packet(20)

    X = X + bot.sensor_state["distance"]

    for i in range(len(data)):
        if data[i] < 1900:
            angle = phi*(i-320)

            x_landmark = math.floor(data[i]*math.cos(angle)) + X
            y_landmark = math.floor(data[i]*math.sin(angle)) + Y

            points = landmarks.keys()
            x = [e[0] for e in points]
            y = [e[1] for e in points]

            plt.scattter(x,y)

            landmarks[(x_landmark, y_landmark)] = timestamp

    bot.drive_straight(100)
