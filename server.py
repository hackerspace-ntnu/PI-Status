import rsa
import json 
import socket
import time
from adress import adress, port

class Client():
	def __init__(self,mac,ip,date):
		self.mac = mac
		self.ip = ip
		self.date = date

def serverMessage(text):
	print("[" + time.strftime("%H:%M:%S") +  "] - " + text)

def createClientFile():
	c = open("clients.txt","w")
	c.write("[]")
	c.close()

def loadClients():
	clients = []
	#Read client file
	try:
			open("clients.txt","r")
	except:
		createClientFile()

	c = open("clients.txt","r")
	text = c.read()
	c.close()
	
	#do i need json? nah
	data = json.loads(text)

	#create new objects for each exsisting client
	for x in range(0,len(data)):
		cli = Client(data[x]["mac"],data[x]["ip"],data[x]["date"])
		clients.append(cli)

	return(clients)

def updateClients(client,clients):
	new = True

	#check if mac adress is already registered
	for x in range(0,len(clients)):
		if clients[x].mac == client["mac"]:
			new = False
			clients[x].ip = client["ip"]
			clients[x].date = time.strftime("%c")

	#if its a new client, create a new client object
	if new:
		newClient = Client(client["mac"], client["ip"], time.strftime("%c"))
		clients.append(newClient)
	
	#write changes to file
	cli = []
	for x in range(0,len(clients)):
		cli.append(
			{
			"mac" : clients[x].mac,
			"ip"  : clients[x].ip,
			"date": clients[x].date
			}
			)
	c = open("clients.txt","w")
	c.write(json.dumps(cli))
	c.close()

	return clients

def aids():
	clients = []
	c = open("clients.txt","w")
	c.write(json.dumps(clients))
	c.close()
#aids()

def main(host,server_port):

	#load saved clients
	clients = loadClients()

	serversocket = socket.socket()
	host = socket.gethostname() # Get local machine name
	#bind the socket to a public host,
	# and a well-known port
	serversocket.bind((host, server_port))
	#become a server socket
	serversocket.listen(5)
	while 1:
		(clientsocket, address) = serversocket.accept()
		info =clientsocket.recv(128)
		
		#read private key
		fil = open("private.txt","rb")
		t = fil.read()
		fil.close()
		privkey = rsa.PrivateKey.load_pkcs1(t,'PEM')
		message = rsa.decrypt(info,privkey).decode('utf8')
		data = json.loads(message)
		serverMessage("New Update from: " + str(data["mac"]))
		clients = updateClients(data,clients)
		clientsocket.sendall("update recieved".encode('utf8'))





main(adress,port)