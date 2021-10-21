import socketserver
import threading


class MyTCPHandler(socketserver.BaseRequestHandler): #cree class mytcpHandler (le serveur reste ouvert)
    def handle(self):
        while 1: #tjrs
            self.data = self.request.recv(1024) #data max recues ( en bytes)
            if not self.data: #quitte si ne sont pas donnees recues 
                break
            self.data = self.data.strip() #formalise le texte
            print (str(self.client_address[0]) + " wrote: ") #dis qui a ecris quoi
            print (self.data) #donnees
            print(self.data.decode('utf-8')) #données decodées en UTF-8
            self.request.send(self.data.upper()) #envoies donnees recus en majusucule


if __name__ == "__main__": #execute si c le fichier principal 
    HOST, PORT = "localhost", 3288 #parametre HOST + PORT (>1083 = pas secu os)
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler) #parametre le serveur avec les fonctionnalités utiles
    server.serve_forever() #receptionne les demandes tant que pas de shutdown()

