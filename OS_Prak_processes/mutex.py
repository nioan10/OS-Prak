import threading
import time
 
mutex = threading.Lock()
shared_resource = 0
 
def access_resource():
    global shared_resource
    print(f'{threading.current_thread().name} ожидает доступ к ресурсу')
    mutex.acquire()
    print(f'{threading.current_thread().name} получил доступ к ресурсу')
    time.sleep(3)
    shared_resource += 1
    mutex.release()
    print(f'{threading.current_thread().name} освободил ресурс')
 
threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource, daemon=True)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
 
print(f'Значение shared_resource: {shared_resource}')