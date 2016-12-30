import socket

s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print "connection recived" + str(addr)
    c.send(str([1,2,3,4]))
    c.close()
