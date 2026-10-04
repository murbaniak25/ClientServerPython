import socket

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 5000))

server_socket.listen()

print("Waiting for a connection...")

connection_socket, client_address = server_socket.accept()

data_bytes = connection_socket.recv(1024)
data = data_bytes.decode("utf-8")

print(f"Received from client: {data}")

server_socket_endpoint = connection_socket.getsockname()

response = f"Hello Client, my socket: {server_socket_endpoint}"

connection_socket.send(response.encode())

server_socket.close()
connection_socket.close()


