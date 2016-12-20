import create2api
import time
import json

#Create a Create2. This will automatically try to connect to your
#   robot over serial
bot = create2api.Create2()

#Start the Create2
bot.start()

#Put the Create2 into 'safe' mode so we can drive it
bot.safe()

#Tell the Create2 to drive straight forward at a speed of 100 mm/s
speed = 100

while True:
    bot.get_packet(101)

    song = 2 * ['E5', 'E5', 'E5'] + ['E5', 'G5', 'C5'] + ['D5', 'E5']
    length = 2 * [8, 8, 16] + [8, 8, 8] + [8, 16]

    bot.play_test_sound(song, length)
    bot.digit_led_ascii("nner")

    time.sleep(2)

    song = 5* ['F5'] + 5 * ['E5']
    length = [8, 8, 10, 6, 8] + [8, 8, 6, 6, 8]

    bot.play_test_sound(song, length)
    bot.digit_led_ascii("CHRI")

    time.sleep(1.3)
    bot.digit_led_ascii("TMAS")
    song = 2 * ['D5'] + ['E5', 'D5', 'G5']
    length = 2*[8] + [8, 16, 16]

    bot.play_test_sound(song, length)
    time.sleep(1.3)

    bot.get_packet(101)
'''
    for bumper in bot.sensor_state["light bumper"]:
        if bot.sensor_state["light bumper"][bumper]:
            bot.drive(100, 10)
            time.sleep(2)
            bot.drive_straight(0)
'''





#Packet 100 contains all sensor data.
while True:
    break
    bot.get_packet(1)
    bot.get_packet(101)
    data = bot.sensor_state
    if data["light bumper"]["center left"]:
        angle = bot.sensor_state["angle"]

        P = 100

        error = angle - 180
        while True:
            if error > 0:
                bot.drive(abs(error/360)*100, -1);
            if error < 0:
                bot.drive(abs(error/360) * 100, 1);
            angle += bot.sensor_state["angle"]
            bot.get_packet(6)
            print error
            error = angle - 180
        bot.drive_straight(0)


#Wait for 5 seconds
#time.sleep(5)

#Tell the Create2 to drive straight backward at a speed of 100 mm/s
#bot.drive_straight(-100)

#Wait for 5 seconds
#time.sleep(5)

#Stop the bot
bot.drive_straight(0)

#Close the connection
bot.destroy()
