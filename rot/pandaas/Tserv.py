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
                        if(data['Operation']=='create VM'):
                           dbserver.insertDataToDB(data['jobId'],clientaddr[0],clientaddr[1],data['Operation'],status,data['operationType'])
                        #self.sendToResourceManager(RMIP,RMPort,4096,strJson)
                           self.sendToResourceManager(RMIP,RMPort,4096,data)
                        if(data['Operation']=='Job Submit'):
                           self.runJob(data['jobId'])
                        clientsocket.send(json.dumps({"response":"success"}))
                        clientsocket.close()
        except Exception, e:
            print e;
            log.writreOnError(str(clientaddr[0]),str(clientaddr[1]),str(e))

    def runJob(self,jobId):
        print "job"
        print "job ip=", jobId
        dbserver=DBServer();
        vm_IP=dbserver.queryVMIP(str(jobId));
        print "vitrual ip=", vm_IP

        dbserver.insertJobData(vm_IP,"Job Submit","pending");

        s = socket()         # Create a socket object
        host = "203.0.113.130" # Get server ip to connect
        port = 12355                 # Reserve a port for your service.
        s.connect((host, port))
        s.send("Hello server!")
        with open('/home/srmri-shyam/access_log/access_log', 'rb') as file_to_send:
                for data in file_to_send:
                        s.sendall(data)

        file_to_send.close()
     
        s.close()
        print "Done Sending"
        sleep(10)
        #call('wget -c http://203.0.113.130/webData.tar.gz',shell=True)  #chande the ip addree of the server node
        dbserver.updateJobData(vm_IP,"Job Submit","Done");

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

        
