import socket
from threading import Thread


def wait_response(s):
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            data = data.decode('utf-8')
            print('Recived from client:' + data)


def main():
    host = ''
    port = 5000
    server = ('localhost', 8880)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    d = Thread(target=wait_response, args=(s, ))
    d.setDaemon(True)
    d.start()

    message = input('\n --> ')
    while message != 'q':
        s.sendto(bytes(message.encode('utf-8')), server)
        message = input('-> ')
    s.close()


if __name__ == '__main__':
    main()
