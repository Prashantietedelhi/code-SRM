import SocketServer
import json
import MySQLdb 
import sys
from socket import *
from db import *
import time
from log import *

class DBServer:
        def queryVMIP(self,jobid):
            log=Log();
            try:
                cnx= mysql.connector.connect(user=username,password=password,host=hostip,database=database)
                cursor=cnx.cursor()
                query=("select distinct vmIP from pandaas where job_id='"+jobid+"'")
                cursor.execute(query)
                vmip=(cursor.fetchone())#.rstrip().lstrip()
                print vmip[0]
                return vmip[0]
            except Exception, e:
                print e
                #log.writreOnError(str(ip),str(port),str(e))

            finally:
                cnx.commit()
                #time.sleep(1)
                cursor.close()
                cnx.close()
        def insertJobData(self,jobid,operationType,status):
            log = Log();
            try:
                cnx = mysql.connector.connect(user=username, password=password,host=hostip,database=database)
                cursor = cnx.cursor()
                currentTime=datetime.now()
                tt = currentTime.timetuple()
                x=""
                i=0;
                delim=""
                for it in tt:
                    if(i>0 and i<3):
                        delim="/"
                    if(i==3):
                        delim="  "
                    if(i>3):
                        delim=":"
                    if(i==6):
                        break
                    if(i<3):
                        x=x+delim+str(it)
                    else:
                        x=x+delim+str(it)
                    i=i+1
                delim="'";
                args = {
                'jobid':jobid,
                'operationType':operationType,
                'status':status
                }
                query = ("INSERT INTO jobList " "(jobId,operationType, status ) " "VALUES (%(jobid)s, %(operationType)s, %(status)s)")
                cursor.execute(query, args)
            except Exception, e:
                print e
                log.writreOnError(str(ip),str(port),str(e))

            finally:
                cnx.commit()
                #time.sleep(1)
                cursor.close()
                cnx.close()
                
        def updateJobData(self,jobid,operationType,status):
            log = Log();
            try:
                cnx = mysql.connector.connect(user=username, password=password,host=hostip,database=database)
                cursor = cnx.cursor()
                currentTime=datetime.now()
                tt = currentTime.timetuple()
                x=""
                i=0;
                delim=""
                for it in tt:
                    if(i>0 and i<3):
                        delim="/"
                    if(i==3):
                        delim="  "
                    if(i>3):
                        delim=":"
                    if(i==6):
                        break
                    if(i<3):
                        x=x+delim+str(it)
                    else:
                        x=x+delim+str(it)
                    i=i+1
                delim = "'"
                time = x

                #print type(jobid1),type(time),type(status1),type(operationType1),type(vmIP1),type(vmID1)
                
                #print args
                #   print args;
                #cursor.execute("update users set last_logon=? where user_id=?", now, user_id).rowcount
                cursor.execute ("UPDATE jobList SET status=%s WHERE jobId='%s' " % (status,jobid))
                #query = ("update jobList set  time=?,status=?, operationType=?, vmIP=?, vmID=? where job_id= ?",time,status,operationType,vmIP,vmID,jobid)
                #print query;
                #cursor.execute(query)
            except Exception, e:
                log.writreOnError(str(vmIP),"port",str(e))

            finally:
                cnx.commit()
                #time.sleep(1)
                cursor.close()
                cnx.close()
                
        def insertDataToDB(self,jobid, ip, port,process,status,operationType):
            log = Log();
            try:
                cnx = mysql.connector.connect(user=username, password=password,host=hostip,database=database)
                cursor = cnx.cursor()
                currentTime=datetime.now()
                tt = currentTime.timetuple()
                x=""
                i=0;
                delim=""
                for it in tt:
                    if(i>0 and i<3):
                        delim="/"
                    if(i==3):
                        delim="  "
                    if(i>3):
                        delim=":"
                    if(i==6):
                        break
                    if(i<3):
                        x=x+delim+str(it)
                    else:
                        x=x+delim+str(it)
                    i=i+1
                delim="'";
                args = {
                'jobid':jobid,
                'time': x,
                'ip': str(ip),
                'port':port,
                'process':process,
                'status':status,
                'operationType':operationType
                }
                #   print args;
                query = ("INSERT INTO pandaas " "(job_id, time, ip, port, process, status, operationType) " "VALUES (%(jobid)s, %(time)s, %(ip)s,%(port)s,%(process)s,%(status)s, %(operationType)s)")
                print query;
                print '\n\n\n'
                cursor.execute(query, args)
            except Exception, e:
                print e
                log.writreOnError(str(ip),str(port),str(e))

            finally:
                cnx.commit()
                #time.sleep(1)
                cursor.close()
                cnx.close()

        def updateDB(self,jobid, status, operationType,vmIP,vmID):
            log = Log();
            try:
                cnx = mysql.connector.connect(user=username, password=password,host=hostip,database=database)
                cursor = cnx.cursor()
                currentTime=datetime.now()
                tt = currentTime.timetuple()
                x=""
                i=0;
                delim=""
                for it in tt:
                    if(i>0 and i<3):
                        delim="/"
                    if(i==3):
                        delim="  "
                    if(i>3):
                        delim=":"
                    if(i==6):
                        break
                    if(i<3):
                        x=x+delim+str(it)
                    else:
                        x=x+delim+str(it)
                    i=i+1
                delim = "'"
                time = x
                query = ("update pandaas set  time='"+time+"',status='"+status+"', operationType='"+operationType+"', vmIP='"+vmIP+"', vmID='"+vmID+"' where job_id='"+jobid+"'")
                print query;
                cursor.execute(query)
                print "chandrakant"
            except Exception, e:
                print e
                print "error in update"
                log.writreOnError(str(vmIP),"port",str(e))

            finally:
                cnx.commit()
                #time.sleep(1)
                cursor.close()
                cnx.close()


            
            # if cursor.lastrowid:
            #     print('last insert id', cursor.lastrowid)
            # else:
            #     print('last insert id not found')
            
            
