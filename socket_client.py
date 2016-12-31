import socket               # Import socket module
import numpy as np
import time
import cv2
s = socket.socket()         # Create a socket object
host = "192.168.1.102"      # Get local machine name
port = 8000                 # Reserve a port for your service.
s.connect((host, port))
data = np.zeros(shape=480*640, dtype=int)
buf = memoryview(data)
while len(buf):
    n = s.recv_into(buf)
    print n
    buf = buf[n:]
data =  data.reshape((480,640))
s.close()
array = cv2.cvtColor(data,cv2.COLOR_RGB2BGR)
cv.imshow('Depth image',array)
