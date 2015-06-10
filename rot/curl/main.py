from server_new import *
import thread
if __name__ == "__main__":
	f=open('config.txt','r')
	HOST=(f.readline().split("=")[1].rstrip())
	PORT=int(f.readline().split("=")[1].rstrip())
	obj= Calling()
	thread.start_new_thread(obj.calling(HOST,PORT))
