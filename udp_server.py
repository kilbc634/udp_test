import socket, traceback

host = '127.0.0.1'
port = 12334

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, int(port)))
print("server strart...")
while True:
    try:
        message, address = s.recvfrom(8192)
        print("Got data from " + str(address) + ": " + str(message))
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()