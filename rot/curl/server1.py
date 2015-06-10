import SocketServer
import json
from subprocess import * 
import socket
from log import *
import subprocess
class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):		#handle function
        lo=Log()		# create log object
        try:
            data = self.request.recv(1024).strip() # loads the json data
            #data = str(data)
	    print self.client_address[0]
	    print type(data)
	#    HOST="203.0.113.190" # send the result to client
	 #   PORT=8788
	  #  print data
	   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# create socket object
	    #s.connect((HOST,PORT)) # connect to host and port
	    #s.send(json.dumps({'status':'success'}))
	    #self.request.sendall(json.dumps({'status':'success'}))#,(HOST,PORT))'''

	    proc=subprocess.Popen('curl -d \'{"auth":{"tenantName": "demo", "passwordCredentials": {"username": "demo", "password": "root"}}}\' -H "Content-type: application/json" http://controller:5000/v2.0/tokens', shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	    out, err = proc.communicate()
	    proc.wait()
	    code = proc.returncode
	    if code == 0:
      		print "Generated Token"
    	    else:
	    	print "Token Generation Failed"

	    start = out.find('{')
	    substr= out[start:len(out)]
	  
	    id = json.loads(substr)['access']['token']['id']
	    print id
	    self.request.send(json.dumps({'id':id}))
	    proc=subprocess.Popen('curl -i  http://controller:8774/v2/ce5024d32fc54680a0f1fe6bd6d5be7a/servers -X POST -H "X-Auth-Project-Id: admin" -H "Content-Type: application/json" -H "Accept: application/json" -H "X-Auth-Token:'+id+'" -d '+'\''+data+'\'', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
	    

	    '''  proc=subprocess.Popen('curl -i  http://controller:8774/v2/ce5024d32fc54680a0f1fe6bd6d5be7a/servers -X POST -H "X-Auth-Project-Id: admin" -H "Content-Type: application/json" -H "Accept: application/json" -H "X-Auth-Token:'+id+'" -d \'{"jobId":"95677090","Operation":"create VM","operationType":"client","server": {"name": "webalizer", "imageRef": "2022fc15-3a3a-4e29-848c-b3a931d61a8e", "key_name": "hadoop", "flavorRef": "2", "max_count": 1, "min_count": 1, "networks": [{"uuid": "47f63ef5-0173-4b76-992e-e89d0b3a5552"}] , "security_groups": [{"name": "default"}]}}\'', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	    '''
	    out, err = proc.communicate()
	    proc.wait()
	    print out
	    start = out.find('{')
            substr= out[start:len(out)]

            id = json.loads(substr)['server']['id']
            print id

	    code = proc.returncode
	    if code == 0:
      		print "VM created"

    	    else:
	    	print "VM creation Failed"

            lo.writreToSuccess(str(self.client_address[0]),str(self.client_address[1]),str(data)) # update log file

        except Exception, e:
            print "Exception wile receiving message: ", e
	    lo.writreOnError(str(self.client_address[0]),str(self.client_address[1]),str(e)) # write log file
class Calling():
    def calling(self,HOST,PORT):
       	  server = MyTCPServer((HOST,PORT), MyTCPServerHandler)	#create handler function object
          server.serve_forever()	# serve the request
