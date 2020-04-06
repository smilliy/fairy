# -*- coding: utf-8 -*-

import socket
s=socket.socket()

host=socket.gethostname()
print(host)
port=99
s.connect((host,port))
print(s.recv(99))