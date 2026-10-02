import socket

HOST = "10.110.36.89"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to server")

while True:

    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())

    response = client.recv(1024).decode()

    print("Server:", response)

client.close()