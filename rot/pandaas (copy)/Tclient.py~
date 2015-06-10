from socket import *
import json


class Client:

    host = ""
    port = ""
    buf  = ""
    addr = ""
    jsonData={"jobId":"98ss90","Operation":"create VM","operationType":"client","server": {"name": "webalizer", "imageRef": "2022fc15-3a3a-4e29-848c-b3a931d61a8e", "key_name": "hadoop", "flavorRef": "2", "max_count": 1, "min_count": 1, "networks": [{"uuid": "47f63ef5-0173-4b76-992e-e89d0b3a5552"}] , "security_groups": [{"name": "default"}]}}
    def __init__(self, host, port):

        self.host=host;
        self.port=port;
        self.buf=1024;

    def connectToServer(self):

        self.addr = (self.host,self.port)
        clientsocket = socket(AF_INET, SOCK_STREAM)
        clientsocket.connect(self.addr)

        while 1:
            data = raw_input(">> ")
            if not data:
                break
            else:
                clientsocket.send(json.dumps(self.jsonData))
                data = json.loads(clientsocket.recv(self.buf))
                if not data:
                    break
                else:
                    print data
        clientsocket.close()

client1 = Client('localhost', 59969);
client1.connectToServer();
