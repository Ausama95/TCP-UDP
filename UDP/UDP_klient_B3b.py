# UDP Client
# Anders Nelsson BTH
# Exempel från kursbok

import time
from socket import *
serverName = '192.168.1.76'
serverPort = 12000

letter = "A"
# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get input from keyboard
seq = 10000

for i in range(0, 1000):
    seq += 1
    message = ((str(seq)) + letter * 1400 + '####')
    clientSocket.sendto(message.encode(),(serverName, serverPort))

# close the socket
clientSocket.close()
