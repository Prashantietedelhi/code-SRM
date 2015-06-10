from datetime import date, datetime, timedelta,time
import time
import os
import json

class Log:

    path="log/"
    dirName=""

    def __init__(self):
        currentTime=datetime.now()
        tt = currentTime.timetuple();
        self.dirName=str(tt[2])+"::"+str(tt[1])+"::"+str(tt[0])
        self.path=self.path+self.dirName
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def  writreToSuccess(self,ip,port,data):
        fileName=os.path.join(self.path,"access.txt")
        fileToWrite = open(fileName, "a")
        fileToWrite.write("\nClient IP: "+ip+"  Client Port: "+port+"\nReceived:")
        json.dump(data,fileToWrite);
        fileToWrite.close()

    def  writreOnError(self, ip, port, msg):
        fileName=os.path.join(self.path,"error.txt")
        fileToWrite = open(fileName, "a")
        fileToWrite.write("\n\nClient IP: "+ip+"  Client Port: "+port+"    Error msg:"+msg)
        fileToWrite.close()
        
