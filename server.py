import socket

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 5000))

server_socket.listen()

print("Waiting for a connection...")

connection_socket, client_address = server_socket.accept()

while True:

    data_bytes = connection_socket.recv(1024)

    if not data_bytes:
        break

    message = data_bytes.decode("utf-8")

    if message == "exit":
        break

    print(f"Received from client: {message}")

    response = f"Received: {message}"

    connection_socket.send(response.encode())

server_socket.close()
connection_socket.close()


