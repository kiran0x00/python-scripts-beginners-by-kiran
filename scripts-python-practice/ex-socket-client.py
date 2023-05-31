from socket import*
client=socket()
# ip address of the server
client.connect(("192.168.56.109",9999))
name = input("Enter your name : ")
client.send(bytes(name,"utf-8"))
print(client.recv(1024).decode())