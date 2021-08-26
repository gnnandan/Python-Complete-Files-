from threading import *
def show():
    print("This is child thread")
t = Thread(target = show()) # ! this is important to execute the child thread
t.start() # ! it is used to start our thread process
print('This is Parent thread')