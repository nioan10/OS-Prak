from threading import Timer
from time import sleep, time
import os

pid = os.getpid()
ppid = os.getppid()

print(f'pid - {pid}, ppid - {ppid}')

def timer_function():
    print("Message from Timer!")

timer = Timer(interval=3, function=timer_function)
timer.start()
