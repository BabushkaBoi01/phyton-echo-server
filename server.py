import socket

serverSocket = socket.socket()
print("Server is up and running")
serverSocket.bind(("localhost", 1084))
serverSocket.listen(3)
print("Waiting for connection")
while True:
    c, addr = serverSocket.accept()
    name = c.recv(1024).decode()
    print(f"{name} connected with {addr}")
    c.send(bytes("Welcome to Amir's Server", "utf-8"))
    while True:
        msg = c.recv(1024).decode()
        if msg == "exit":
            break
        print(f"Received from {name} : {msg}")
        c.send(bytes(msg, "utf-8"))

    c.close()
    # c.send(bytes("Enter Message : ","utf-8"))
