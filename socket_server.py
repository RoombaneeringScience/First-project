import socket
import create2api
import freenect
#   robot over serial
bot = create2api.Create2()
#Start the Create2
bot.start()
#Put the Create2 into 'safe' mode so we can drive it
bot.safe()
bot.kinect_power()

array,_ = freenect.sync_get_depth()

s = socket.socket()
port = 8000

s.bind(("192.168.1.102", port))

s.listen(5)

while True:
    c, addr = s.accept()
    print "connec pythotion recived" + str(addr)
    array,_ = freenect.sync_get_video()
    c.sendall(str(array))
c.close()
