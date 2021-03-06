from socket import *
import thread
import json
import SocketServer
from dbserver import *
import os
from log import *

class Server:

    host,port,buf,addr = "","","",""

    def __init__(self, host, port):

        self.host = host
        self.port = port
        self.buf = 1024
        self.addr = (host, port)
        self.serversocket = socket(AF_INET, SOCK_STREAM)
        self.serversocket.bind(self.addr)
        self.serversocket.listen(2)

    def handler(self,clientsocket, clientaddr,RMIP,RMPort):
        log=Log();
        try:
            print "Accepted connection from: ", (clientaddr[0]), (clientaddr[1])
            while 1:
                    data = json.loads(clientsocket.recv(4096).strip())
                    #data = clientsocket.recv(1024)
                    strJson = json.dumps(data)
                    #print type(strJson)
                    print strJson
                    if not data:
                        break
                    else :
                        #msg = "You sent me: %s" % data
                        dbserver=DBServer()
                        log.writreToSuccess(str(clientaddr[0]),str(clientaddr[1]),data)
                        if(data['Operation']=='create VM'):
                            status="creating vm"
                        if(data['Operation']=='delete VM'):
                            status="deleting vm"
                        if(data['Operation']=='Job Submit'):
                            status="Executing"
                            runJob()
                        dbserver.insertDataToDB(data['jobId'],clientaddr[0],clientaddr[1],data['Operation'],status,data['operationType'])
                        #self.sendToResourceManager(RMIP,RMPort,4096,strJson)
                        self.sendToResourceManager(RMIP,RMPort,4096,data)

                        clientsocket.send(json.dumps({"response":"success"}))
                        clientsocket.close()
        except Exception, e:
            print e;
            log.writreOnError(str(clientaddr[0]),str(clientaddr[1]),str(e))
    def sendToResourceManager(self,host,port,buff,data):
        addr=(host,port)
        clientsocket = socket(AF_INET, SOCK_STREAM)
        clientsocket.connect(addr)
        data=json.dumps(data)
        #data="'"+data+"'"
        #print type(data)
        #print data
        clientsocket.send(data)
        receivedData = json.loads(clientsocket.recv(self.buf))
        print receivedData['vm_id']
        if receivedData['vm_id']:
            #print "received data is -------------->"
            #print receivedData
            dbserver=DBServer();
            # receivedData['job_id'],"vm created","Resource Manager",receivedData['vm_ip'],receivedData['vm_id'],type(receivedData['job_id'])
            dbserver.updateDB(str(receivedData['job_id']),"vm created","Resource Manager",str(receivedData['vm_ip']),str(receivedData['vm_id']))
        clientsocket.close()

        
