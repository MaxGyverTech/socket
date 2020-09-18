import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))
sock.send(input().encode())

data = sock.recv(1024).decode()
sock.close()

print(data)