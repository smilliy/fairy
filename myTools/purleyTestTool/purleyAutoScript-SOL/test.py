# -*- coding: utf-8 -*-

# import configparser
#
# config = configparser.ConfigParser()
# config.read("config.ini", encoding='utf-8')
# print(config.get("BMC", "userid"))
# print(config.get("ipmitool", "path"))

import paramiko
from paramiko.transport import Channel
from paramiko.transport import Transport
import socket
import threading
import time

socket1 = socket.socket()
socket1.bind(("127.0.0.1", 99))
socket1.listen(5)
print(socket1)
transport1 = Transport(socket1)
t1 = threading.Thread(target=transport1.start_server)
t1.start()
print(68)
print(transport1)
with Channel(chanid=transport1) as c1:
    c1.recv_ready()
    print(c1)
    # sftp = paramiko.SFTPServer(channel=chanel1, name="", server="")

    while True:
        print(c1.active)


print(55)
