import socket

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 5000))

while True:

    message = input("> ")
    client_socket.sendall(message.encode())

    if message == 'exit':
        break

    elif not message:
        continue

    response_bytes = client_socket.recv(1024)
    response = response_bytes.decode("utf-8")

    print(f"Server response: {response}")

client_socket.close()
