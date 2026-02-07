import socket
import struct

MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

def main():
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # 👇 The key part: allow multiple processes to bind to the same port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    except (AttributeError, OSError):
        # Some systems don’t support it — ignore if not available
        pass

    # Bind to all interfaces (required before joining group)
    sock.bind(('', PORT))

    # Join multicast group
    group = socket.inet_aton(MULTICAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(f"👂 Listening for multicast messages on {MULTICAST_GROUP}:{PORT}...\n")

    try:
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"[{addr[0]}] {data.decode()}")
    except KeyboardInterrupt:
        print("\nListener closed.")
    finally:
        sock.close()

if __name__ == '__main__':
    main()
