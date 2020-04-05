# -*- coding: utf-8 -*-

import socket
s=socket.socket()

host=socket.gethostname()
print(host)
port=99
s.bind((host,port))

s.listen(5)
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.send(('welcome').encode())
    c.close()
