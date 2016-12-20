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

bot.drive_direct(100, 100)

time.sleep(3)

bot.drive_direct(0,0)

bot.destroy()
