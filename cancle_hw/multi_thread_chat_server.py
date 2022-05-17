from socket import *
import threading
import time

port = 3333
BUFFSIZE = 1024

clients = []

def sendTask(conn):
    while True:
        data = conn.recv(BUFFSIZE)

        if 'quit' in data.decode():
            if addr in  clients:
                print(addr, 'exited')
                clients.remove(addr)
                continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        for client in clients:
            if client != conn:
                client.send(data)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

while True:
    conn, addr = sock.accept()

    if addr not in clients:
        print('new client', addr)
        clients.append(conn)
        
    th = threading.Thread(target=sendTask, args=(conn,))
    th.start()