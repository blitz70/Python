#   53. Sockets - intro

import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s = socket.socket()
#s = socket.socket(socket.AddressFamily.AF_INET, socket.SocketKind.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'
#server = 'localhost'
#port = 80
port = 443

serverIP = socket.gethostbyname(server)
print (serverIP)

#request = 'GET\nHost:'+server+'\n\n'
request = 'GET / HTTP/1.1\nHost:'+server+'\n\n'
print(request)

#server uses https -> use ss in place of s
ss = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
ss.connect((server,port))
ss.send(request.encode())
result = ss.recv(4096)
print(result.decode())
while (len(result)>0):
    print(result.decode())
    result = ss.recv(4096)
ss.close()
s.close()
