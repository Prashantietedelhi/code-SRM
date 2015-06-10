
from __future__ import print_function
from datetime import date, datetime, timedelta,time
import mysql.connector
from mysql.connector import MySQLConnection, Error

f=open('Configure.txt','r')
cache=f.readlines()
f.close()
username=(cache[0].split('=')[1]).rstrip().lstrip()
password=(cache[1].split('=')[1]).rstrip().lstrip()
hostip=(cache[2].split('=')[1]).rstrip().lstrip()
database=(cache[3].split('=')[1]).rstrip().lstrip()

cnx = mysql.connector.connect(user=username, password=password,host=hostip,database=database)
cursor = cnx.cursor()