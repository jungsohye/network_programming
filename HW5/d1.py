from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(3)
print('waiting..')

while True:
    c, addr = s.accept()
    print('Connection from ', addr)
    while True:
        Data = c.recv(1024)
        if not Data:
            break
        Data = Data.decode()
        print(Data)
        if Data == 'Request':
            temp = str(random.randrange(0, 41))
            humidity = str(random.randrange(0, 101))
            illumin = str(random.randrange(70, 151))
            
            total = temp + ' ' + humidity + ' ' + illumin
            print(total)
            c.send(total.encode())
        elif Data == 'quit':
            break
    if Data == 'quit':
        break

    c.close()
