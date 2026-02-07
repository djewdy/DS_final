import socket
import struct
import sys

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

def main():
   
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    print(" Multicast Messenger started.")
    print("Type messages and press Enter to send to the group.")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            message = input("> ")
            if not message:
                continue
            sock.sendto(message.encode(), (MULTICAST_GROUP, PORT))
    except KeyboardInterrupt:
        print("\nMessenger closed.")
    finally:
        sock.close()

if __name__ == '__main__':
    main()
