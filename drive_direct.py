import create2api
import time
import json
import freenect
import cv2
import pygame


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

    while 1:
        #frame = get_video()
        #cv2.imshow('RGB image',frame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bot.drive_straight(0)
                bot.destroy()
                sys.exit()
            if event.type == pygame.K_UP:
                bot.drive_direct(100, 100)
            elif event.type == pygame.K_DOWN:
                bot.drive_direct(-100, -100)
            elif event.type == pygame.K_LEFT:
                bot.drive_direct(100, -100)
            elif event.type == pygame.K_RIGHT:
                bot.drive_direct(-100, 100)
            else:
                bot.drive_straight(0)
