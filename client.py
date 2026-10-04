import socket

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 5000))

client_socket_endpoint = client_socket.getsockname()

client_socket.sendall(b"Hello server :)")

response_bytes = client_socket.recv(1024)
response = response_bytes.decode()

print(f"Client socket endpoint: {client_socket_endpoint}\nServer response: {response}")

client_socket.close()
