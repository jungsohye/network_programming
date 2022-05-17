import select
from socket import *

socks = []
BUFFERSIZE = 1024
PORT = 3333

s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print("holy")

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print('Client ({}) connected'.format(addr))
        else:
            data = s.recv(BUFFERSIZE)
            if not data:
                s.close()
                socks.remove(s)
                continue
            print("Received:", data.decode())

            for client in socks:
                if client != s_sock and client != s:
                    client.send(data)