import create2api
import time
import pygame
import math


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

    #initalizing the state vector, note there are no landmarks yet
    #[x ,y, theta column vector]
    X = np.matrix([0, 0, 0]).transpose()

    ENCODER_STEP = 72/508.8

    while 1:
        #get encoder data
        bot.get_packet(101)

        left_encoder = bot.sensor_state['left encoder counts']
        right_encoder = bot.sensor_state['right encoder counts']

        ds = 0.5*(left_encoder + right_encoder)*ENCODER_STEP
        dangle = ((left_encoder - right_encoder)*ENCODER_STEP)/235

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bot.drive_straight(0)
                bot.destroy()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bot.drive_direct(100, 100)
                elif event.key == pygame.K_DOWN:
                    bot.drive_direct(-100, -100)
                elif event.key == pygame.K_LEFT:
                    bot.drive_direct(100, -100)
                elif event.key == pygame.K_RIGHT:
                    bot.drive_direct(-100, 100)
                else:
                    bot.drive_straight(0)
