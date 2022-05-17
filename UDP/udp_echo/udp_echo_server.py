import socket
port = 2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

md = {}
while True:
    msg, addr = sock.recvfrom(BUFFSIZE)
    if msg[:3] == "send":
        print('Received: ', msg.decode())
        sock.sendto("ok", addr)

    elif msg[:6] == "receive":
        sock.sendto = (md[msg.split()[1]].pop(),addr)

    elif msg == "quit":
        sock.close()
        break