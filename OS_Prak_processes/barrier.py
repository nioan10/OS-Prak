from threading import Barrier, Thread
from time import sleep, time


br = Barrier(3)
store = []


def f1(x):
   print("Calc part1")
   store.append(x*5)
   sleep(0.5)
   br.wait()


def f2(x):
   print("Calc part2")
   store.append(x*2)
   sleep(1)
   br.wait()


Thread(target=f1, args=(3,)).start()
Thread(target=f2, args=(7,)).start()

sleep(5)
br.wait()

print("Result: ", sum(store))