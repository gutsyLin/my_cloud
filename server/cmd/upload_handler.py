import logging as log
import hashlib

cmd = 'upload'

def handle(sock, data):
    sha256 = hashlib.sha256()
    filename, data_len = data
    data_len = int(data_len)
    log.debug((filename, data_len))
    
    byte_list = []
    while data_len > 0:
        recv = sock.recv(4096)
        byte_list.append(recv)
        data_len -= 4096
    with open(filename, 'wb', buffering=4096) as f:
        for b in byte_list:
            f.write(b)
            sha256.update(b)
    log.debug('digest():' + str(sha256.hexdigest()))
    sock.sendall(bytes('ok', 'utf-8'))
