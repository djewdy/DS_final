import socket
import datetime

IP = "0.0.0.0"
PORT = 9002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"UDP Time Server listening on {IP}:{PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received time request from {addr}")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = f"Current server time: {current_time}"
    sock.sendto(response.encode(), addr)
