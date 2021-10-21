import socket
import sys
from time import sleep

HOST, PORT = "localhost", 3288
data = "hello"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.send(data.encode('utf8'))
    received = sock.recv(1024)
    print(received)

    sleep(3)

    sock.send(data.encode('utf8'))
    received = sock.recv(1024)
    print(received)

    sleep(3)

    sock.send(data.encode('utf8'))
    received = sock.recv(1024)
    print(received)

finally:
    sock.close()