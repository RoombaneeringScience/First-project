import socket               # Import socket module
import numpy as np
import cv2
s = socket.socket()         # Create a socket object
host = "192.168.1.102"      # Get local machine name
port = 8000                 # Reserve a port for your service.
s.connect((host, port))
try:
    while True:
        ultimate_buffer = ''
        while True:
            receiving_buffer = client_connection.recv(1024)
            ultimate_buffer=''
            if not receiving_buffer: break
            ultimate_buffer+= receiving_buffer
            print '-',
        depth = np.ndarray(ultimate_buffer)
        depth = cv2.cvtColor(data,cv2.COLOR_RGB2BGR)
        cv2.imshow('Depth image',depth)
except KeyboardInterrupt:
    s.close                     # Close the socket when done
