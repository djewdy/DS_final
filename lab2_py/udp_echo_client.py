import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello from Python UDP client"
sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

data, addr = sock.recvfrom(1024)
print(f"Server replied: {data.decode()}")

sock.close()
