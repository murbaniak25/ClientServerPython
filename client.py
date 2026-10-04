import socket

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 5000))

client_socket.sendall(b"Hello server :)")

client_socket.close()
