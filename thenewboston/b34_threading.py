#threading using class

import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(20):
            print(threading.current_thread().getName())

th1 = Messenger(name='Sender------->')
th2 = Messenger(name='----->Receiver')

th1.start()
th2.start()