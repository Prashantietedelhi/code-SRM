from socket import *
import json


class Client:

    host = ""
    port = ""
    buf  = ""
    addr = ""
    jsonData={"jobId":"98ss90","operation":"Job Submit","operationType":"client","tool":"webalizer","inputdir":"dmesg.tar.gz"}
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
