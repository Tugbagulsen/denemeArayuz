"""import socket

T_PORT = 5006
TCP_IP = '192.268.137.28'
BUF_SIZE = 1024

MSG = "Hello karl"

# k isminde bir obje yaratıyoruz

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((TCP_IP, T_PORT))
k.send(MSG)
data = k.recv(BUF_SIZE)
k.close"""

# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())
# close the connection
s.close()

