# import the socket module
from socket import *
# define the port number and IP address of server
serverPort = 13500
serverName = "192.168.56.1"
# create the UDP client socket
clientsocket = socket(AF_INET, SOCK_DGRAM)
print("Client: Pallvi (2110994824)")

while True:
    # ask user to input the alias name and send the query message to the server
    message = input("Enter the query (alias name): ")
    clientsocket.sendto(message.encode(), (serverName, serverPort))
    print("Query sent to the server.")
    # receive response from server and print it
    servermessage, serverAddress = clientsocket.recvfrom(2048)
    print("Response from server: " + servermessage.decode())

    # ask user whether to continue or not
    message = input("Would you like to continue(y/n): ")
    # if no then close the client socket
    if message.lower() == "n":
        print("Disconnected from server")
        break

# close the client socket
clientsocket.close()