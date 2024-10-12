import threading
import random
import time

###

potok_num = 0
mutex_d1 = threading.Lock()
p2, p3, p4 = 0, 0, 0

def dot1():
    global potok_num
    print(f'{threading.current_thread().name} подошёл к точке 1')
    mutex_d1.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 1')
    t_sleep = random.randint(1,20)
    print(f'{threading.current_thread().name} уснул на ', t_sleep)
    time.sleep(t_sleep)
    
    threads = []
    thread = threading.Thread(target=dot2, name = "Поток B", daemon=True)
    threads.append(thread)
    print(f'{threading.current_thread().name} запустил поток B')
    thread.start()
    thread = threading.Thread(target=dot2, name = "Поток C", daemon=True)
    threads.append(thread)
    print(f'{threading.current_thread().name} запустил поток C')
    thread.start()
    thread = threading.Thread(target=dot2, name = "Поток I", daemon=True)
    threads.append(thread)
    print(f'{threading.current_thread().name} запустил поток I')
    thread.start()
    thread = threading.Thread(target=dot4, name = "Поток J", daemon=True)
    threads.append(thread)
    print(f'{threading.current_thread().name} запустил поток J')
    thread.start()

    for thread in threads:
        thread.join()
    
    potok_num += 1
    mutex_d1.release()
    print(f'{threading.current_thread().name} завершил работу в точке 1 ', potok_num)

###
    
mutex_d2 = threading.Lock()

def dot2():
    global potok_num
    global p2
    print(f'{threading.current_thread().name} подошёл к точке 2')
    mutex_d2.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 2')
    time_sleep = random.randint(1,20)
    print(f'{threading.current_thread().name} уснул на ', time_sleep )
    time.sleep(time_sleep)

    if p2 == 0:
        p2 = 1
        threads1 = []
        thread = threading.Thread(target=dot3, name = "Поток D", daemon=True)
        threads1.append(thread)
        print(f'{threading.current_thread().name} запустил поток D')
        thread.start()
        thread = threading.Thread(target=dot3, name = "Поток E", daemon=True)
        threads1.append(thread)
        print(f'{threading.current_thread().name} запустил поток E')
        thread.start()
        thread = threading.Thread(target=dot3, name = "Поток F", daemon=True)
        threads1.append(thread)        
        print(f'{threading.current_thread().name} запустил поток F')
        thread.start()

        for thread in threads1:
            thread.join()

    potok_num += 1
    mutex_d2.release()
    print(f'{threading.current_thread().name} завершил работу в точке 2 ', potok_num)

###
    
mutex_d3 = threading.Lock()

def dot3():
    global potok_num
    global p3
    print(f'{threading.current_thread().name} подошёл к точке 3')
    mutex_d3.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 3')
    t_sleep = random.randint(1,20)
    print(f'{threading.current_thread().name} уснул на ', t_sleep )
    time.sleep(t_sleep)

    if p3 == 0:
        p3 = 1        
        threads2 = []
        thread = threading.Thread(target=dot4, name = "Поток G", daemon=True)
        threads2.append(thread)        
        print(f'{threading.current_thread().name} запустил поток G')
        thread.start()
        thread = threading.Thread(target=dot4, name = "Поток H", daemon=True)
        threads2.append(thread)        
        print(f'{threading.current_thread().name} запустил поток H')
        thread.start()

        for thread in threads2:
            thread.join()
            
    potok_num += 1
    mutex_d3.release()
    print(f'{threading.current_thread().name} завершил работу в точке 3 ', potok_num)



###
    
mutex_d4 = threading.Lock()

def dot4():
    global potok_num
    global p4
    print(f'{threading.current_thread().name} подошёл к точке 4')
    mutex_d4.acquire()
    print(f'{threading.current_thread().name} получил доступ в точке 4')
    t_sleep = random.randint(1,20)
    print(f'{threading.current_thread().name} уснул на ', t_sleep )
    time.sleep(t_sleep)
    
    if p4 == 0:
        p4 = 1
        thread = threading.Thread(target=dot5, name = "Поток К", daemon=True)
        thread.start()
        print(f'{threading.current_thread().name} запустил поток K')
        thread.join()

    potok_num+=1
    mutex_d4.release()
    print(f'{threading.current_thread().name} завершил работу в точке 4 ', potok_num)

###
    
mutex_out = threading.Lock()

def dot5():
    global potok_num
    print(f'{threading.current_thread().name} подошёл к выходу')
    mutex_out.acquire()
    print(f'{threading.current_thread().name} получил доступ на выход и ждёт отработки остальных потоков')

###

thread = threading.Thread(target=dot1, name = 'Поток A',daemon=True)
thread.start()
thread.join()


T = True
while T == True:
    if potok_num == 10:
        T = False
        potok_num+=1
        mutex_out.release()
        print('Завершение работы программы', potok_num)

print(potok_num)