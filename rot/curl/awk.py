import subprocess
from string import whitespace

def associateIP(vm,ipaddress):
         print "Associating IP "+ipaddress+" for VM ",vm
	 process=subprocess.Popen("nova list | grep "+vm+" | awk 'NR==1{print $10; exit}", shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
         vmStatus,error=process.communicate()
         process.wait()
	 if vmStatus == 'Running':
            proc=subprocess.Popen("nova floating-ip-associate "+vm+" "+ipaddress, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	    out,err=proc.communicate()
            proc.wait()
	    print out
 	 else:
	    print "VM not Running: Please check ID"

def floatingPointIP(vm):  
  try:
    NW="ext-net"
    proc=subprocess.Popen("nova floating-ip-create "+NW+"| grep 203 | awk 'NR==1{print $2; exit}'", shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    ip,err=proc.communicate()
    proc.wait()
    #print out
    if ip.startswith('203'):
	print "floating ip created for vm :" + ip
	associateIP(vm,ip)
    else:
	#count = nova floating-ip-list | awk '{ print } END { print NR }'
	process=subprocess.Popen("nova floating-ip-list | grep '| -' | awk 'NR==1{print $2; exit}'", shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        ip,listErr=process.communicate()
        process.wait()
        #print listOut
	if ip.startswith('203'):
		print "floating ip selected for vm from the ip list :"+ ip
		associateIP(vm,ip)
	else:
		print "IP not availbale in the pool"
    #print grep
    #code = proc.returncode
    #if code == 0:
    print "Finished Successfully"
    #else:
    #  print "Process Failed"
	return ip
  except:
    print "exception"
    raise

'''def associateIP(ipaddress):
	 proc=subprocess.Popen("nova floating-ip-associate "+ipaddress+" 46de3b92-cbbe-47ec-80cc-19ab09effacf", shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	 ip,err=proc.communicate()
	 proc.wait()
	 print ip
	 #nova floating-ip-associate 46de3b92-cbbe-47ec-80cc-19ab09effacf'''
