#   55. Sockets - Threaded port scanner

import socket
import time
import threading
from queue import Queue

printLock = threading.Lock()
server = 'hackthissite.org'
#server = 'localhost'

def portScan(server,myport):#open also checked as closed?
    s = socket.socket()
    try:
        con = s.connect((server,myport))
        with printLock:
            print(myport,'OPEN!!!!')
        con.close()
        s.close
    except Exception as e:
        #with printLock:
        #    print(myport,'closed')
        s.close()
        pass

def threader():
    while True:
        myport = q.get()
        portScan(server,myport)
        q.task_done()

q = Queue()
startTime = time.time()
print(server, 'port info...')

for mythreads in range(1000):#number of threads
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for myport in range(1,70000):#ports to search
    q.put(myport)

q.join()
print('Scan took', time.time()-startTime,'s')

