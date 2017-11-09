import socket
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',14000))
s.listen(1)

while True:
    conn, addr = s.accept()
    buff = conn.recv(64)
    if len(buff) > 0:
        if buff.strip('\n') == "password":
            print "Correct!"
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
        else:
            print "Wrong, you sent: " + buff
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
