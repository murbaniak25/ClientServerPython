# First Stage

## Description

Create very basic client-server architecture using socket library.

### Server
- creates TCP/IP socket
- binds the socket to localhost endpoint
- starts listening
- accepts one connection
- prints input from Client

### Client
- creates TCP/IP socket
- connects to the server localhost endpoint
- sends message

client_socket <--- TCP/IP ---> connection_socket
server_socket is used only for accepting new connections

# Second Stage

## Description

Add bidirectional TCP client-server communication.

### Server

- sends response with socket info to client 

### Client

- receives response from server and displays both client socket info and server socket info used for communication
