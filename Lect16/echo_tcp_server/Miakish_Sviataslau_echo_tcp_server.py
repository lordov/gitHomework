import socket


HOST = '127.0.0.1'
PORT = 65432
toSend = bytes('OK, и тебе привет клиент,', 'utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Соединение по адерсу {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'),
                  ' <-- Вот это сообщение СЕРВЕР принял!')
            print(str(toSend, 'utf-8'),
                  ' <-- Вот это сообщение СЕРВЕР отправил в ответ')
            conn.sendall(toSend)
