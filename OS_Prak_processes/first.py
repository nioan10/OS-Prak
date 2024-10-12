import psutil
import os
import time


pid = os.getpid()
ppid = os.getppid()

print(f'pid - {pid}, ppid - {ppid}')

while 1:
    time.sleep(1)





