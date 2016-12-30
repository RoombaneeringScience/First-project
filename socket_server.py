import socket

s = socket.socket()
port = 8000

s.bind(("192.168.1.102", port))

s.listen(5)

while True:
    c, addr = s.accept()
    print "connection recived" + str(addr)
    c.send(str([1,2,3,4]))
    c.close()
