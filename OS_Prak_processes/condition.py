from threading import Condition, Thread
from queue import Queue
from time import sleep


cv = Condition()
q = Queue()


# Consumer function for order processing
def order_processor(name):
   while True:
       with cv:
           # Wait while queue is empty
           while q.empty():
               cv.wait()

           try:
               # Get data (order) from queue
               order = q.get_nowait()               
               print(f"{name}: {order}")               

               # If get "stop" message then stop thread
               if order == "stop":  
                   print(f"{name} остановка...")                 
                   break               

           except:
               pass

           sleep(0.5)

# Run order processors
Thread(target=order_processor, args=("Поток 1",)).start()
Thread(target=order_processor, args=("Поток 2",)).start()
Thread(target=order_processor, args=("Поток 3",)).start()
Thread(target=order_processor, args=("Поток 4",)).start()
sleep(5)
# Put data into queue
for i in range(50):
   q.put(f"order {i}")
   

# Put stop-commands for consumers
for _ in range(4):
   q.put("stop")
# Notify all consumers
print("Оповестим всех клиентов")
with cv:
   cv.notify_all()