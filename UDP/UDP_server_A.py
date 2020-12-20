# UDP Server
# Anders Nelsson BTH
# Exempel från kursbok

from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The UDP server is ready to recieve")

number = 10000
numberOfPackets = 0

while True:
    # read client's message and remember client's address (IP and port)
        message, clientAddress = serverSocket.recvfrom(1500)
        sequenceNumber = message[:5].decode()
        sequenceNumber = int(sequenceNumber)
        between = sequenceNumber - number
        if sequenceNumber > number:
            if between == 1:
                number = int(sequenceNumber)
                numberOfPackets += 1
                print("Packet number: " + str(number) + " received")
                if numberOfPackets == 50:
                    print("All packets have been received")
                continue
            else:
                print("Packet number:" + str(sequenceNumber) + " didn't come in order")
