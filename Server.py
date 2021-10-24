import socket
import os
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    global ThreadCount
    connection.send(str.encode('Server is working:'))
    while True:
        try:
            data = connection.recv(2048)
            response = 'Server message: ' + data.decode('utf-8')
            print(data.decode('utf-8'))
            data_list.append(data.decode('utf-8'))
        except socket.error:
            ThreadCount -=1
            pass
        if not data:
            ThreadCount -=1
            break
        try:
            connection.sendall(str.encode(response))
        except socket.error:
            ThreadCount -=1
            pass
        
    connection.close()

data_list=[]
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    data_list = list(filter(None, data_list))
    print(data_list)


