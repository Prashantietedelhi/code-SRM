import SocketServer
import json
from subprocess import *

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = json.loads(self.request.recv(1024).strip())
	    print "get"
            print data
        except Exception, e:
            print "Exception wile receiving message: ", e



    
HOST="192.168.1.169"
PORT=9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPServerHandler)
server.serve_forever()
