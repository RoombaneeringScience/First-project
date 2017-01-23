import create2api
import time
import pygame
import math
import numpy as np
import matplotlib.pyplot as plt
import kalman
VELOCITIES = {pygame.K_UP: (100, 100), pygame.K_DOWN: (-100, -100), pygame.K_LEFT: (100, -100), pygame.K_RIGHT: (-100, 100)}

def initialize_kalman_filter():
    A = np.eye(3)
    def B(x, u):
        v, w = u
        dx = v*math.cos(x[2] + w/2.)
        dy = v*math.sin(x[2] + w/2.)
        dtheta = w
        return np.matrix([dx, dy, dtheta]).transpose()
    D = np.eye(3)
    R = np.matrix([[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.05]])
    Q = R

    return kalman.KalmanFilter(A, B, D, R, Q)

if __name__ == "__main__":

    #Create a Create2. This will automatically try to connect to your
    #   robot over serial
    bot = create2api.Create2()
    #Start the Create2
    bot.start()
    #Put the Create2 into 'safe' mode so we can drive it
    bot.safe()
    bot.kinect_power()
    pygame.init()
    screen = pygame.display.set_mode((30,30))
    pygame.display.set_caption('Pygame Keyboard Test')

    ENCODER_STEP = 72/508.8

    kalman_filter = initialize_kalman_filter();
    t = time.time()

    plt.ion()
    v = (0,0)
    while True:
        #get encoder data
        bot.get_packet(101)

        left_encoder = bot.sensor_state['left encoder counts']
        right_encoder = bot.sensor_state['right encoder counts']

        ds = 0.5*(left_encoder + right_encoder)*ENCODER_STEP
        dangle = ((left_encoder - right_encoder)*ENCODER_STEP)/235.
        x = kalman_filter.get_x()
	    z = np.zeros((3,1))
        z[0] = x[0] + ds*math.cos(x[2] + dangle/2)
	    z[1] = x[1] + ds*math.sin(x[2] + dangle/2.)
        z[2] = x[2] + dangle

        dt = (time.time() - t)/1000000.
        speed = 0.5*(v[0] + v[1])*dt
        w = (v[1] - v[0])/235.*dt

        kalman_filter.update(z, (speed, w))
        plt.scatter(x[0], x[1])
        plt.pause(0.05)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bot.drive_straight(0)
                bot.destroy()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in VELOCITIES.keys():
                    v = VELOCITIES[event.key]
                else:
                    v = (0, 0)
		print v
                bot.drive_direct(v[0], v[1])
