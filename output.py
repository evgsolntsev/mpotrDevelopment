from __future__ import print_function
import os
import sys

#for interactive
class Displaier:
    def __init__(self):
        self.history = ""  #store history of messagies

#logging
    def log(self, s):
        self.clear()
        sys.stderr.write(s + "\n")

#system messagies
    def system(self, s):
        self.clear()
        print("System: " + s)
        print(self.history, end="")
        print(">", end="")
        sys.stdout.flush()


#clear terminal
    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

#this way we hide user's commands
    def redisplay(self):
        self.clear()
        print(self.history + ">", end="")
        sys.stdout.flush()

#when user type message, we should hide it
    def display(self, author, mess):
        s = author + " said: " + mess
        self.history += s + "\n"
        self.redisplay()
