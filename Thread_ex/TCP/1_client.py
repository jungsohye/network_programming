import socket
HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

#키보드로 입력한 문자열 서버로 전송
#서버에서 에코되어 돌아오는 메시지를 받으면 화면에 출력
#qiut 입력할때까지 반복
while True:
    m = input('Enter Message : ')
    if m == 'quit':
        break
    client_socket.send(m.encode())
    data = client_socket.recv(1024)

    print('Received from the server : ', repr(data.decode()))

client_socket.close()