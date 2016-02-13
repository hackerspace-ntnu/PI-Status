import rsa
import socket
import json
import subprocess
from uuid import getnode as get_mac

#doesnt work if not connected directly to internet via cable.
def get_ip():
    p = subprocess.Popen('ip route list', shell=True, stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    return split_data[split_data.index(b'src') + 1].decode('utf-8')


def main(host,server_port):
	ip = get_ip()

	mac = get_mac() #Might not work correctly when having multiple MAC adresses

	obj = {
		"ip":ip,
		"mac":mac,
	}

	fil = open("public.txt","rb")
	t = fil.read()
	fil.close()
	pubkey = rsa.PublicKey.load_pkcs1(t,'PEM')

	j = json.dumps(obj).encode('utf8')

	aes_key = rsa.randnum.read_random_bits(128)
	message = rsa.encrypt(j,pubkey)
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = host
	server_port = server_port
	connection.connect((host,server_port))
	connection.sendall(message)
	print(connection.recv(128).decode('utf8'))

	connection.close()

main('178.62.156.170',800)