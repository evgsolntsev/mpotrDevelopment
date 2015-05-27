import os


#for interactive
class Displaier:
    def __init__(self):
        self.history = ""  #store history of messagies

#system messagies
    def log(self, s):
        print "System: " + s

#clear terminal
    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

#this way we hide user's commands
    def redisplay(self):
        self.clear()
        print self.history

#when user type message, we should hide it
    def display(self, author, mess):
        s = author + " said: " + mess
        self.history += s + "\n"
        self.redisplay()
