import socket
import threading
import socketserver
import logging as log
from tcp_request_handler import TCPRequestHandler as RequestHandler

class ThreadTcpServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    log.basicConfig(level=log.DEBUG)

    host, port = "localhost", 8888
    server = ThreadTcpServer((host, port), RequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    log.debug('Server started in {}:{}! '.format(host, port))
    input()
    server.shutdown()
