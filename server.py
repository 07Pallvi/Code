# import the socket module
from socket import *
# record with IP address and
c_name_record = {
    "youtu.be" : "www.youtube.com",
    "lnkd.in" : "www.linkedin.com",
    "google.com" : "www.google.com",
    "pin.it" : "www.pinterest.com",
    "fb.com" : "www.facebook.com",
}
a_record = {
    "youtu.be" : "216.58.192.238",
    "lnkd.in" : "108.174.10.10",
    "google.com" : "142.250.65.78",
    "pin.it" : "151.101.192.84",
    "fb.com" : "31.13.71.36",
}
# define server port number
serverPort = 13500
# create server socket and bind to the port
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind(('', serverPort))

# display message on terminal indicating that server is running
print("The server is listening")

while True:
    # receives message from client
    message, clientAddress = serversocket.recvfrom(2048)
    clientmessage = message.decode()
    # checks if the client message is in the server's record and send appropriate reply
    if clientmessage in c_name_record and a_record:
        clientsendmessage = "Domain name: " + c_name_record[clientmessage] + " , IP Address: " + a_record[clientmessage]
    else:
        clientsendmessage = "Data not found"
    serversocket.sendto(clientsendmessage.encode(), clientAddress)
