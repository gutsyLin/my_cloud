import config

def handle(code, sock, msg='', data={}):
    if code == 404:
        bytes_out = bytes('{}: Command not found!'.format(data['cmd']), 'utf-8')
        sock.sendall(bytes_out)
