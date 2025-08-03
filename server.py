import socket

s = socket.socket()
s.bind(('127.0.0.1', 12345))
s.listen(1)
print("Server listening...")

conn, addr = s.accept()
print("Connected by", addr)
conn.sendall(b"Hello from server!")
conn.close()
