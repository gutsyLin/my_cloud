import time

cmd = 'connect'

welcome_str = ['Login at {time} from {ip}',
        'Welcome to my_cloud service!']
        
        
def handle(sock, data):
    ip, port = sock.getpeername()
    localtime = time.localtime(time.time())
    asctime = time.asctime(localtime)
    fomated_str = welcome_str[0].format(time=asctime, ip=(ip + ':' + str(port)))
    sock.sendall(bytes(fomated_str + "\n" + welcome_str[1], 'utf-8'))
