from socket import *
from tkinter.ttk import setup_master
import time

f = open('.Data.txt', 'a')

sd1 = socket(AF_INET, SOCK_STREAM)
sd1.connect(('localhost', 7777))
sd2 = socket(AF_INET, SOCK_STREAM)
sd2.connect(('localhost', 7707))



while True:
    msg = input('Enter the device to get data from.\n')
    if msg == 'quit':
        sd1.send(b'quit')
        sd2.send(b'quit')
        break
    elif msg == '1':
        sd1.send(b'Request')
        rsp = sd1.recv(1024).decode()
        Data = rsp.split(' ')
        temp = Data[0]
        humidity = Data[1]
        illumin = Data[2]
        t = time.asctime()
        line = t + ':' + ' ' + 'Device1: ' + '온도= ' + temp + ', 습도= ' + humidity + ', 조도= ' + illumin + '\n'
        print(line)
        f.write(line)
    elif msg == '2':
        sd2.send(b'Request')
        rsp  = sd2.recv(1024).decode()
        Data = rsp.split(' ')
        hb = Data[0] 
        steps = Data[1]
        cal = Data[2]
        t = time.asctime()
        line = t + ':' + ' ' + 'Device2: ' + '심박수= ' + hb + ', 걸음수= ' + steps + ', 소모칼로리= ' + cal + '\n'
        print(line)
        f.write(line)
    # print('Get data: ', rsp)

sd1.close()
sd2.close()
f.close()
