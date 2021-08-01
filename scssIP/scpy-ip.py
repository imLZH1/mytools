#qingwachong@qq.com
#2020 Jun 15
#
from threading import Thread
from scapy.all import *
import getmyip
import time

start_time = time.time()
#Text color code
r = '\033[34m'
rr = '\033[1;34m'
re = '\033[1;31m'
g = '\033[1;33m'
z = '\033[1;35m'
e = '\033[0m'
z2 = '\033[1;4;35m'
ie = '\033[36m'


#var
num=0

def scweep(n):
    global a

    #global var num(ip numbr)
    global num

    eth = Ether()
    eth.type = 0x0806
    eth.dst='ff:ff:ff:ff:ff:ff'
    arp = ARP()
    arp.pdst=a+str(n)
    try:
        reply = srp1(eth/arp,timeout=4,verbose=0,iface='eth0')
        #print(str(reply.psrc)+"\t\t"+str(reply.hwsrc))
        print(r+'\tIP'+e+':'+z+'{0:20}'.format(str(reply.psrc))+e+r+'MAC:'+e+g+str(reply.hwsrc)+e)
        num+=1
        #print('\t'+z+'{0:17} '.format(str(reply.psrc))+e+g+' '+str(reply.hwsrc)+e)
    except:
        pass

#print('\t{0:17} MAC'.format('IP'))
#print('\t'+'-'*17+' '+'-'*20)
threads = []
try:
    networkname=sys.argv[1]
    a = getmyip.get_ip(str(networkname))
    print('\n┌─['"\033[01;32m*\033[0m"']'"\033[01;33m Start Scaning !\033[0m")
    print('└'+'─'*57)
    for n in range(1,255):
        t=Thread(target=scweep,args=(n,))
        threads.append(t)
        t.start()
except:
    print("\n\tUsage: scssip <network_name>\n")
    exit(0)
for t in threads:
    t.join()
end_time = time.time()
print('┌'+'─'*57)
print('|[\033[01;32m*\033[0m] '+rr+'Network segment:'+e,re+a+'0/24'+e)
print('|[\033[01;32m*\033[0m] '+rr+'Alive IP number:'+e,re+str(num)+e)
print('|[\033[01;32m*\033[0m] '+rr+'Elapsed real time:'+e,re+str(end_time-start_time)[0:4]+' sec'+e)
print("└─[\033[01;32m+\033[0m] "+g+"Scan complete !"+e)
