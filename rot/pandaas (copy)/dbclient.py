import socket
import json

data = {'name':'chandrakant', 'college':'IIIT-A','branch':'it','gender':'male'}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.123', 9998))
s.send(json.dumps(data))
#result = json.loads(s.recv(1024))
#print result
s.close()