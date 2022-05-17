<<<<<<< HEAD
from socket import *
from collections import defaultdict

port = 2018
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID") :')
    msglist = msg.split(' ')
       
    if msglist[0] == 'send':
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())
    elif msglist[0] == 'receive':
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())
    else:
        sock.sendto('quit'.encode(), ('localhost', port))
    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
=======
from socket import *
from collections import defaultdict

port = 2018
BUFFSIZE = 1024
sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID") :')
    msglist = msg.split(' ')
       
    if msglist[0] == 'send':
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())
    elif msglist[0] == 'receive':
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFFSIZE)
        print(data.decode())
    else:
        sock.sendto('quit'.encode(), ('localhost', port))
    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
>>>>>>> 44e3bae56d2d495afcd441b59aafa04e983de8fa
        break