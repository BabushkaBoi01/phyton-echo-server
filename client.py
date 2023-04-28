import socket

c = socket.socket()
c.connect(("localhost", 1084))
name = input("Enter name : ")
c.send(bytes(name, "utf-8"))
print(c.recv(1024).decode())

while True:
    msg = input("Enter message : ")
    if msg == "exit":
        c.send(bytes(msg, "utf-8"))
        break
    c.send(bytes(msg, "utf-8"))
    print("Server echo : ", c.recv(1024).decode())

#msg = input("Enter message : ")
#c.send(bytes(msg, "utf-8"))
