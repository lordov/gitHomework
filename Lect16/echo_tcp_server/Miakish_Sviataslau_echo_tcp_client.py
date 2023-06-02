import socket


HOST = '127.0.0.1'
PORT = 65432
toSend = bytes('Привет, сервер', 'utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(toSend)
    print(str(toSend, 'utf-8'),
          ' <-- Вот это сообщение КЛИЕНТ отправил!')
    data = s.recv(1024)

print('\n Вот это сообщение КЛИЕНТ получил в ответ!')
print(f'Получил вот то --', str(data, 'utf-8'))
