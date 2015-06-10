
from Tserv import *

f=open('Configure.txt','r')
cache=f.readlines()
f.close()
hostip = (cache[2].split('=')[1]).rstrip().lstrip()
hostPort = int((cache[4].split('=')[1]).rstrip().lstrip())
server1 = Server(hostip, hostPort)
RMIP=(cache[5].split('=')[1]).rstrip().lstrip()
RMPort=int((cache[6].split('=')[1]).rstrip().lstrip())
while 1:
    print "###############  Server is listening for connections ###############\n"
    clientsocket, clientaddr = server1.serversocket.accept()
    thread.start_new_thread(server1.handler, (clientsocket, clientaddr,RMIP,RMPort));
server1.serversocket.close()
