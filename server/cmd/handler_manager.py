from . import connect_handler as connect
from . import error_handler as err_handler
from . import exit_handler
from . import upload_handler as upload

import logging as log


handlers = {}
handlers[connect.cmd] = connect.handle
handlers[exit_handler.cmd] = exit_handler.handle
handlers[upload.cmd] = upload.handle

def handle(cmd, sock):
    cmds = cmd.split()
    cmd = cmds[0]
    if cmd in handlers.keys():
        handler = handlers[cmd]
        handler(sock, data=cmds[1:])
    else:
        err_handler.handle(404, sock, data={"cmd":cmd})
