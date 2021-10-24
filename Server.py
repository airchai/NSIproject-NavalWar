import socket
import os
from _thread import *

ServerSideSocket = socket.socket() #cree un socket avec librairie
host = '127.0.0.1' #pour instant localhost mais bientot heberge sur pi+ port forwarding
port = 2004 
ThreadCount = 0 #compteur de connections
try:
    ServerSideSocket.bind((host, port)) # essaye de bind le serveir et si marche pas renvoie erreur 
except socket.error as e:
    print(str(e))

print('Socket is listening..') 
ServerSideSocket.listen(5) #serveur attends connections (écoute)

def multi_threaded_client(connection):
    """Permet la connection de plusieurs clients sur le même serveur"""
    global ThreadCount # récupère la variable threadcount
    connection.send(str.encode('Server is working:')) # A la connection du client le serveur renvoie qu'il fonctionne
    while True: 
        try: #execute tant que client est connecté 
            data = connection.recv(2048) #reçois la data du client
            response = 'Server message: ' + data.decode('utf-8') #réponse
            print(data.decode('utf-8')) #affiche la data décodée en UTF-8
            data_list.append(data.decode('utf-8')) #ajoute a la liste de data les datas (va bientot etre utilisées pour les grilles)
        except socket.error:#si error threadcount - 1 car on perd un client
            ThreadCount -=1 
            pass
        if not data: #si error threadcount - 1 car on perd un client
            ThreadCount -=1
            break
        try:
            connection.sendall(str.encode(response)) #essaye de renvoyer une reponse au client
        except socket.error: #si error threadcount - 1 car on perd un client
            ThreadCount -=1
            pass
        
    connection.close() #ferme connection quand fini

data_list=[]
while True:
    Client, address = ServerSideSocket.accept() #accepte les connections
    print('Connected to: ' + address[0] + ':' + str(address[1])) #affiche les ip / port des clients connectes 
    start_new_thread(multi_threaded_client, (Client, )) #lance la connection de plusieurs clients sur 1 serveur
    ThreadCount += 1 #ajoute 1 client
    print('Thread Number: ' + str(ThreadCount)) #affiche nombre clients connectes
    data_list = list(filter(None, data_list)) #retire vide de la data_list (genere quand client se deconnecte)
    print(data_list) #affiche la data en memoire


