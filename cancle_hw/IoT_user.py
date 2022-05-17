from socket import *
from sqlite3 import connect
import time
import selectors

sel = selectors.DefaultSelector()

s_dev1 = socket(AF_INET, SOCK_STREAM)
s_dev2 = socket(AF_INET, SOCK_STREAM)
s_dev1.connect(('localhost', 2017))
s_dev2.connect(('localhost', 1522))

f = open('.data.txt', 'a')

def writeFileDev1(conn, mask):
        data = conn.recv(1024).decode()
        data = data.split(' ')
        temp = data[0]
        humid = data[1]
        illum = data[2]
        t = time.asctime()
        line = t + ':' + ' ' + 'Device1:' + ' ' + 'Temp=' + temp + ', Humid=' + humid + ', Illum=' + illum + '\n'
        print(line)
        f.write(line)

def writeFileDev2(conn, mask):
        data  = conn.recv(1024).decode()
        data = data.split(' ')
        heartbeat = data[0] 
        steps = data[1]
        cal = data[2]
        t = time.asctime()
        line = t + ':' + ' ' + 'Device2:' + ' ' + 'Heartbeat=' + heartbeat + ', Steps=' + steps + ', Cal=' + cal + '\n'
        print(line)
        f.write(line)        

sel.register(s_dev1, selectors.EVENT_READ, writeFileDev1)
sel.register(s_dev2, selectors.EVENT_READ, writeFileDev2)

msg = 'Register'
s_dev1.send(msg.encode())
s_dev2.send(msg.encode())

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)