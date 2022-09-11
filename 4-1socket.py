import socket
s = socket.socket()#by default it would be TCP
print("socket created")
s.bind(("localhost",1028))
s.listen(3)
print("waiting for connections")
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode
    print("connected with ",addr,name)
    c.send(bytes("welcome guys",'utf-8'))
    c.close()