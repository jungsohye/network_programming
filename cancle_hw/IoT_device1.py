from socket import *
import random
import schedule

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 2017))
s.listen(5)
print('Please wating..')

def sensingData(client):
    temp = str(random.randrange(0, 41))
    illum = str(random.randrange(70, 151))
    humid = str(random.randrange(0, 101))
    total = temp + ' ' + humid + ' ' + illum
    client.send(total.encode())

client, addr = s.accept()
print('Connection from ', addr)

while True:
    msg = client.recv(1024)
    if msg.decode() == 'Register':
        break

schedule.every(3).seconds.do(sensingData, client)

while True:
    schedule.run_pending()