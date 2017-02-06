from socket import *

from datetime import datetime
import json


def send(temperature, humidity, socket):
    dict = {'timestamp':datetime.now().strftime("%X"), 'temperature':temperature, 'humidity':humidity}
    message = json.dumps(dict)
    try :
        socket.send(message)
    except :
        socket.close()


s = socket(AF_INET, SOCK_STREAM)
PORT = 40017
s.connect(('', PORT))
while(1):
	temperature = raw_input('Temperature: ')
	humidity = raw_input('Humidity: ')
	send(temperature, humidity, s)
	

s.close()
