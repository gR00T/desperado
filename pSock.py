#!/usr/bin/python2.7
import socket
import struct
import random

def ABCD():
    #9879oa8c09809ac908809
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('localhost',random.choice(range(15000,15999))))
    s.listen(1)

    #90098908c0fdada098c908
    while True:
        conn, addr = s.accept()
        buff = conn.recv(64)
        if len(buff) > 0:
            if buff.strip('\n') == "328bd8fa998209ac17ede5e5c69c4e98":
                print "Correct!"
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
            else:
                print "Wrong, you sent: " + buff
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
