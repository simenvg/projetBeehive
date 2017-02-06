from socket import *
from threading import Thread
import io
from datetime import datetime
import json
import string

#432

Client_adresses = []

def clientHandler():
	conn, addr = s.accept()
	global Client_adresses
	Client_adresses.append(addr)
	print addr, "is connected" 
	filepath = '/Users/Simen/Documents/Kode/Melding/' + str(addr[0]) + '.txt'	

	while(1):
		data = conn.recv(4096)
		data_loaded = json.loads(data) ##pi
		if data:
			print data_loaded['timestamp'], " - ", addr, "sent:", ", Temp: ", data_loaded['temperature'], ", Humidity:", data_loaded['humidity']
			fileobject = open(filepath, 'a')
			fileobject.write(data_loaded['timestamp'] + "," +  data_loaded['temperature'] + "," + data_loaded['humidity'] + '\n')
			fileobject.close()

			#with open(filepath, 'a') as outfile:
			#	json.dump(data, outfile)

		else: break	


HOST = '' #Local host
PORT = 40017
num_of_clients = 3

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(num_of_clients)

print "Server is running......"

for i in range(num_of_clients):
	Thread(target=clientHandler).start()


s.close()

