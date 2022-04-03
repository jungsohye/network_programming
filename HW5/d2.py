from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7707))
s.listen(5)
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
            hb = str(random.randrange(40, 141))
            steps = str(random.randrange(2000, 6001))
            cal = str(random.randrange(1000, 4001))
            total = hb + ' ' + steps + ' ' + cal
            print(total)
            c.send(total.encode())
        elif Data == 'quit':
            break
    if Data == 'quit':
        break

    c.close()