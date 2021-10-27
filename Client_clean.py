import socket
import sys
from time import sleep




class client:
    def __init__(self, ip='127.0.0.1', port:int=2004,data='Grille1',grille=[],username='Dom'): #ip + port = adresse serveur
        self.ip=ip 
        self.port=port
        self.data=data
        self.grille=grille
        self.username=username
        
    def get_data(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #def socket
        sock.connect((self.ip, self.port))
        data_username={self.username:''}
        data_username=str(data_username)
        sock.send(data_username.encode('utf-8'))
        data=sock.recv(2048)
        data = data.decode('utf-8') #réponse
        self.grille = eval(data)
        print(self.grille)
   
    def send_data(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #def socket
        sock.connect((self.ip, self.port))
        data_username={self.username:self.data}
        data_username=str(data_username)
        sock.send(data_username.encode('utf-8'))
        data=sock.recv(2048)
        data = data.decode('utf-8') #réponse
        self.grille = eval(data)
        print(self.grille)
        
client1=client()
client1.get_data()
# client1.send_data()
  