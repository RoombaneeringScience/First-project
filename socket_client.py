import socket               # Import socket module
import numpy as np
s = socket.socket()         # Create a socket object
host = "localhost"      # Get local machine name
port = 8000                 # Reserve a port for your service.
s.connect((host, port))

md = socket.recv_json(flags=0)
msg = socket.recv(flags=0, copy=True, track=False)
buf = buffer(msg)
A = numpy.frombuffer(buf, dtype=md['dtype'])
print A.reshape(md['shape'])
print md
#depth = cv.cvtColor(data,cv2.COLOR_RGB2BGR)
#cv2.imshow('Depth image',depth)
