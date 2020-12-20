# TCP Client
import time
from socket import *

serverName = '192.168.1.25'
serverPort = 12000

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the connection
clientSocket.connect((serverName, serverPort))

letter = "A"
sequence = 10000
message = ""

for i in range(0, 50):
    sequence += 1
    if i == 49:
        message = ((str(sequence)) + letter * 1400 + "????")
    else:
        message = ((str(sequence)) + letter * 1400 + '####')
    clientSocket.send(message.encode())
    time.sleep(0.05)

# close the socket
clientSocket.close()
