import socket               # Import socket module
import np
import cv2
s = socket.socket()         # Create a socket object
host = "192.168.1.102" # Get local machine name
port = 8000                # Reserve a port for your service.

while True:
    s.connect((host, port))
    data = np.ndarray(s.recv(4096))
    depth = cv2.cvtColor(data,cv2.COLOR_RGB2BGR)
    cv2.imshow('Depth image',depth)
    s.close                     # Close the socket when done
