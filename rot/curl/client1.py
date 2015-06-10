import socket
import SocketServer
import json
from subprocess import *
import sys

data = {'name':'chandrakant', 'college':'IIIT-A','branch':'it','gender':'male'}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.169',8788))
s.send(json.dumps(data))
received = str(s.recv(1024))
print received
#s.close()
