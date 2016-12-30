import socket               # Import socket module
import numpy as np
import cv2
s = socket.socket()         # Create a socket object
host = "localhost"      # Get local machine name
port = 8000                 # Reserve a port for your service.
s.connect((host, port))

while True:
    data = np.ndarray(shape=(480,640), dtype=int)
    view = memoryview(data)
    print view
    while len(view):
        nrecv = s.recv_into(view)
        print nrecv
        view = view[nrecv:]
    print data.shape()
    print data

    #depth = cv2.cvtColor(data,cv2.COLOR_RGB2BGR)
    #cv2.imshow('Depth image',depth)
s.close                     # Close the socket when done
