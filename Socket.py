import socket

_socket = socket.socket()
port = 40764

_socket.bind(('', port))
print ("socket binded to %s" %(port))

_socket.listen(5)
print ("socket is listening")

while True:
    c, addr = _socket.accept()
    print ('Got connection from', addr )

    c.send(b'Thank you for connecting')

    c.close()