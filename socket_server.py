import socket
import create2api
import freenect
import zmq
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

s.bind(("localhost", port))

s.listen(5)

while True:
    c, addr = s.accept()
    print "connec pythotion recived" + str(addr)
    array,_ = freenect.sync_get_video()
    """send a numpy array with metadata"""
    md = dict(
        dtype = str(A.dtype),
        shape = A.shape,
    )
    c.send_json(md, 0|zmq.SNDMORE)
    c.send(A, 0, copy=True, track=False)
    c.close()
