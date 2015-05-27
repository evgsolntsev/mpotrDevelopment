import glib, sys, os, fcntl

class Input(object):
    def __init__(self, displaier, sendMess, sendShutdown):
        self.buffer = ''
        self.line_callback = self.commandSwitch
        self.sendMess = sendMess
        self.displaier = displaier
        self.sendShutdown = sendShutdown
        flags = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
        flags |= os.O_NONBLOCK
        fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, flags)
        glib.io_add_watch(sys.stdin, glib.IO_IN, self.io_callback)

    def io_callback(self, fd, condition):
        chunk = fd.read()
        for char in chunk:
            if char == '\n':
                self.line_callback(self.buffer)
                self.buffer = ''
            else:
                self.buffer += char
        return True

    #Process chat commands
    def processCommand(self, command):
        self.displaier.redisplay()
       	global loop
        c = command[1:]
    	if (c == "exit"):
            self.sendShutdown()
            loop.quit()
        elif (c == "cat"):
            self.displaier.log("\n /\\___/\\\n( o   o )\n(  =^=  )\n(        )\n(         )\n(          )))))))))))))))\n")
        else:
            self.displaier.log("Unknown command: " +  c)

    #Process command or send message
    def commandSwitch(self, message):
        global context, account, chat, purple
        if (message[0] == '!'):
            self.processCommand(message)
        else:
            self.sendMess(message)
            self.displaier.redisplay()

