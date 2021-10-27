import socket
import os
from _thread import *


ServerSideSocket = socket.socket() #cree un socket avec librairie
host = '127.0.0.1' #pour instant localhost mais bientot heberge sur pi+ port forwarding
port = 2004 

try:
    ServerSideSocket.bind((host, port)) # essaye de bind le serveur et si marche pas renvoie erreur 
except socket.error as e:
    print(str(e))

print('Socket is listening..') 
ServerSideSocket.listen(5) #serveur attends connections (écoute)

data_list={}
connected=[]

def multi_threaded_client(connection):
    """Permet la connection de plusieurs clients sur le même serveur"""
    global data_list
    connection.send(str(data_list).encode('utf-8')) # A la connection du client le serveur renvoie qu'il fonctionne
    while True: 
        try: #execute tant que client est connecté *

            data = connection.recv(2048) #reçois la data du client
            data = data.decode('utf-8') #réponse
            data_list = eval(data) #ajoute a la liste de data les datas (va bientot etre utilisées pour les grilles)
            
            
        except socket.error:#si error threadcount - 1 car on perd un client 
            pass
        try:
            connection.sendall(str(data_list).encode('utf-8')) #essaye de renvoyer une reponse au client
        except socket.error: #si error threadcount - 1 car on perd un client
            pass
        
    connection.close() #ferme connection quand fini




while True:
    Client, address = ServerSideSocket.accept() #accepte les connections
    print('Connected to: ' + address[0] + ':' + str(address[1])) #affiche les ip / port des clients connectes 
    start_new_thread(multi_threaded_client, (Client, )) #lance la connection de plusieurs clients sur 1 serveur
    print(data_list)
    connected=[k for k,v in data_list.items()]
    print(connected) 

    