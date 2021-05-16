import socket, sys

host = '127.0.0.1'
textport = 12334

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    port = socket.getservbyname(textport, 'udp')
s.connect((host, port))
while True:
    print("Enter data to transmit:")
    data = sys.stdin.readline().strip()
    s.sendall(data.encode(encoding="utf-8"))
    buf = s.recv(2048)
    if not len(buf):
        break
    print("Server replies: ")
    sys.stdout.write(str(buf))
    print("\n")
