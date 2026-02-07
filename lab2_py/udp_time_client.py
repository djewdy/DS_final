import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"time?", (SERVER_IP, SERVER_PORT))

data, addr = sock.recvfrom(1024)
print(f"Server time: {data.decode()}")

sock.close()
