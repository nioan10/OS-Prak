import time
import threading
import os

pid = os.getpid()
ppid = os.getppid()

print(f'pid - {pid}, ppid - {ppid}')

semaphore = threading.Semaphore(4)

def access_resource():
    print(f'{threading.current_thread().name} ожидает доступ к ресурсу')
    semaphore.acquire()
    print(f'{threading.current_thread().name} получил доступ к ресурсу')
    time.sleep(5)
    # Тут выполняется работа с ресурсом
    semaphore.release()
    print(f'{threading.current_thread().name} освободил ресурс')

threads = []
for i in range(10):
    thread = threading.Thread(target=access_resource, daemon=True)
    threads.append(thread)
    thread.start()
 
for thread in threads:
    thread.join()