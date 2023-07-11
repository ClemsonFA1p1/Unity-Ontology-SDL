import socket
import time

server_socket = socket.socket()
host = 'localhost'
port = 5000

server_socket.bind((host, port))
server_socket.listen(1)

print('Waiting for a client to connect...')

client_socket, client_address = server_socket.accept()
print('Client connected:', client_address)

strings = ['Hello', 'World', 'Python', 'C#']

try:
    for string in strings:
        # Send each string
        print(string)
        client_socket.send(string.encode())
        time.sleep(.01)

finally:
#     Close the socket
        client_socket.close()
        server_socket.close()
# #

