import socket
import CLI
import logging

def connect(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return sock
	
def send_cmd(sock, msg):
	sock .sendall(bytes(msg, 'utf-8'))

def recv_cmd(sock):
    ret = sock.recv(1024)
    ret = str(ret, 'utf-8')
    return ret

def test(sock):
    
    with open('test.jpg', 'rb', buffering=4096) as f:
        content = f.read()
        sock.sendall(bytes('upload test.jpg {}'.format(len(content)), 'utf-8'))
        sock.sendall(content)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    ip, port = 'localhost', 8888
    sock = connect(ip, port)
    message = CLI.connect
    logging.debug(type(sock))
    while True:
        send_cmd(sock, message)
        rec_cmd = recv_cmd(sock)
        print(rec_cmd)
        message = input('>>>')
        if message == 'exit':
            send_cmd(sock, 'exit')
            sock.shutdown()
            sock.close()
            break
        elif message == 'test':
            test(sock)	
