import socket
import create2api

#   robot over serial
bot = create2api.Create2()
#Start the Create2
bot.start()
#Put the Create2 into 'safe' mode so we can drive it
bot.safe()
bot.kinect_power()

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print "connec pythotion recived" + str(addr)
    array,_ = freenect.sync_get_video()
    c.sendall(str(array))
    c.close()
