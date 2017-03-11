#   56. Sockets - Sockets binding and listening
#   57. Sockets - Client server system
#   enable telnet client on windows to test 56
#   change to normal threaded version

import socket
from _thread import *

host = ''
port = 5555
s = socket.socket()

try:
    s.bind((host,port))
except Exception as e:
    print(str(e))

s.listen(5)
print('Waiting for connection...')

def threaded_server(conn):
    conn.send(str.encode('Welcome user! type bye to exit\n\r'))
    _reply = ''
    while True:
        data = conn.recv(2048).decode('utf-8')
        if not data:
            print('no data')
            break
        elif _reply == 'bye':
            conn.sendall(str.encode('Server output: Good bye'))
            print('Good bye')
            break
        elif '\n' in data:
            reply = 'Server output: '+ _reply
            _reply = ''
            conn.sendall(str.encode(reply+'\n\r'))
        else:
            _reply += data
    conn.close()

while True:
    conn, addr = s.accept()
    print('connected to...')
    print(addr[0], addr[1])
    print(conn)
    start_new_thread(threaded_server,(conn,))

