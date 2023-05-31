from socket import*

soc = socket()
print("socket created")
soc.bind(("192.168.56.109",9999))
soc.listen(3)
print("waiting for connections")

while True:
    c, addr = soc.accept()
    print("connected with", addr)
    c.send(bytes('welcome to socket', 'utf-8'))
    c.close()