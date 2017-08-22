import multiprocessing
import time


def spawn(no):
    print("Spawned! No.{}".format(no))
    time.sleep(2)

if __name__ == "__main__":
    for i in range(100):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        # p.join()
