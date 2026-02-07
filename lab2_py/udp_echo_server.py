import socket

IP = "0.0.0.0"
PORT = 9001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"UDP Echo Server listening on {IP}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
    sock.sendto(data, addr) 
