# TCP Server
from socket import *
serverPort = 12000

# create socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

serverSocket.listen()
print ('The TCP server is ready to recieve')

ls = []
def handeler():
    number = 10000
    numberOfPackets = 0

    for i in ls:
        if int(i) > number:
            if (int(i) - number) == 1:
                number = int(i)
                numberOfPackets += 1
                print("Packet number: " + str(number) + " received")
                if numberOfPackets == 1000:
                    print("All packets have been received")
                    continue
            else:
                print("Packet number:" + sequenceNumber + " didn't come in order")

connectionSocket, addr = serverSocket.accept()

print("Receiving packets please wait...")
while True:
    message = connectionSocket.recv(1500).decode()
    sequenceNumber = message[:5]
    ls.append(sequenceNumber)
    if "????" in message:
        break

handeler()
