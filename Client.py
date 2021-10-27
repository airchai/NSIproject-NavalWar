import socket
import sys
from time import sleep

HOST, PORT = "localhost", 2004
data = "liste1" #donnees a envoyer

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #def socket


sock.connect((HOST, PORT))
while True: 
    a=input()
    if a=='a':#envoyer les donnees si input=a
        sock.send(data.encode('utf8'))
        received = sock.recv(2048)
        print(received) #afficher reponse serveur
        sleep(3)
    if a=='b':
        sock.recv(2048) #afficher
    if a =='c':
        sock.shutdown(1)
        break
