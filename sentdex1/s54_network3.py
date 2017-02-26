#   54. Sockets - Port scanner

import socket
import time

def portScan(server,port):
    try:
        s.connect((server,port))
        return True
    except Exception as e:
        return False

startTime = time.time()
server = 'hackthissite.org'
#server = 'localhost'

s = socket.socket()
print(server, 'port info...')
for port in range(1,26):
    if portScan(server,port) == True:
        print(port,'OPEN !!!!!')
    else:
        print(port,'closed')
s.close()

print('Scan took', time.time()-startTime,'s')
