#   43. Threading

import threading
from queue import Queue
import time

print_lock = threading.Lock()
q = Queue()

def examplejob(task):
    with print_lock:
        print(threading.current_thread().name, task)
    time.sleep(5)

def threader():
    while True:
        task = q.get()
        examplejob(task)
        q.task_done()

for _workers in range(5): #number of available workers(threads)
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

start = time.time()
for task in range(20): #number of tasks
    q.put(task)

q.join()
print('Entire job took:', time.time()-start)
