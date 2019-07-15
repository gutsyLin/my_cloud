import logging as log

cmd = 'exit'


def handle(sock, data):
    sock.close()
