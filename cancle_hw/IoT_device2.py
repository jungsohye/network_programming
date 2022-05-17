from socket import *
import random
import schedule 

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 1522))
s.listen(5)
print('Please wating..')

def sensingData(client):
    heartbeat = str(random.randrange(40, 141))
    steps = str(random.randrange(2000, 6001))
    cal = str(random.randrange(1000, 4001))
    total = heartbeat + ' ' + steps + ' ' + cal
    client.send(total.encode())

client, addr = s.accept()
print('Connection from ', addr)

while True:
    msg = client.recv(1024)
    if msg.decode() == 'Register':
        break

schedule.every(5).seconds.do(sensingData, client)

while True:
    schedule.run_pending()