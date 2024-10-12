import threading
import time
import random

mutex_d1 = threading.Lock()
potok_num = 0



def dot1():
    global potok_num
    p0 = 0
    print(f'{threading.current_thread().name} подошёл к точке 1')
    mutex_d1.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 1')
    t_sleep = random.randint(1,5)
    print(f'{threading.current_thread().name} уснул на ', t_sleep)
    time.sleep(t_sleep)
    
    threads = []
    thread = threading.Thread(target=dot2, name = "Поток B", daemon=True)
    threads.append(thread)
    thread.start()
    thread = threading.Thread(target=dot2, name = "Поток C", daemon=True)
    threads.append(thread)
    thread.start()
    thread = threading.Thread(target=dot2, name = "Поток I", daemon=True)
    threads.append(thread)
    thread.start()
    thread = threading.Thread(target=dot4, name = "Поток J", daemon=True)
    threads.append(thread)
    thread.start()

    for thread in threads:
        thread.join()
    
    potok_num += 1
    mutex_d1.release()
    print(f'{threading.current_thread().name} завершил работу в точке 1 ', potok_num)


mutex_d2 = threading.Lock()

def dot2():
    global potok_num
    p2 = 0
    print(f'{threading.current_thread().name} подошёл к точке 2')
    mutex_d2.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 2')
    time_sleep = random.randint(1,5)
    print(f'{threading.current_thread().name} уснул на ', time_sleep )
    time.sleep(time_sleep)
    if p2 == 0:
        p2 = 1
        thread0 = []
        thread = threading.Thread(target=dot3, name = "Поток D", daemon=True)
        thread0.append(thread)
        thread.start()
        thread = threading.Thread(target=dot3, name = "Поток E", daemon=True)
        thread0.append(thread)
        thread.start()
        thread = threading.Thread(target=dot3, name = "Поток F", daemon=True)
        thread0.append(thread)
        thread.start()

        for thread in thread0:
            thread.join()

    potok_num += 1
    mutex_d2.release()
    print(f'{threading.current_thread().name} завершил работу в точке 2 ', potok_num)

mutex_d3 = threading.Lock()

def dot3():
    global potok_num
    p3 = 0
    print(f'{threading.current_thread().name} подошёл к точке 3')
    mutex_d3.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 3')
    t_sleep = random.randint(1,5)
    time.sleep(t_sleep)
    if p3 == 0:
        p3 = 1
        thread1 = []
        thread = threading.Thread(target=dot4, name = "Поток G", daemon=True)
        thread1.append(thread)
        thread.start()
        thread = threading.Thread(target=dot4, name = "Поток H", daemon=True)
        thread1.append(thread)
        thread.start()

        for thread in thread1:
            thread.join()
    potok_num += 1
    mutex_d3.release()
    print(f'{threading.current_thread().name} завершил работу в точке 3 ', potok_num)

mutex_d4 = threading.Lock()

def dot4():
    global potok_num
    p4 = 0
    print(f'{threading.current_thread().name} подошёл к точке 4')
    mutex_d4.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 4')
    t_sleep = random.randint(1,5)
    time.sleep(t_sleep)
    if p4 == 0:
        p4 = 1
        thread = threading.Thread(target=out, name = "Поток К", daemon=True)
        thread.join()

    potok_num+=1
    mutex_d4.release()
    print(f'{threading.current_thread().name} завершил работу в точке 4 ', potok_num)

mutex_out = threading.Lock()

def out():
    global potok_num
    print(f'{threading.current_thread().name} подошёл к выходу')
    mutex_out.acquire()
    print(f'{threading.current_thread().name} получил доступ на выходе')
    t_sleep = random.randint(1,5)
    print(f'{threading.current_thread().name} уснул на ', t_sleep)
    time.sleep(t_sleep)

    potok_num += 1
    mutex_out.release()
    print(f'{threading.current_thread().name} завершил работу на выходе ', potok_num)

###
thread = threading.Thread(target=dot1, name = 'Поток A',daemon=True)
thread.start()
thread.join()

print(potok_num)


