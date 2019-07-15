import threading
import socketserver
import config
import logging as log
from cmd import handler_manager

class TCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        cur_thread = threading.current_thread()
        while True:
            if self.request._closed:
                self.request.close()
                break
            recv = self.request.recv(config.rec_size)
            cmd = str(recv, config.default_encoding).lower()
            log.debug('receive command[{}] in {}'.format(cmd, cur_thread.name))
            handler_manager.handle(cmd, self.request)
