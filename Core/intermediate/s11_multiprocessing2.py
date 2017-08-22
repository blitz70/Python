import multiprocessing
import time


def job(param):
    time.sleep(1)
    return param*2

if __name__ == "__main__":
    start = time.time()
    p = multiprocessing.Pool(processes=500)
    data1 = p.map(job, range(1000))
    data2 = p.map(job, [i for i in range(1000)])
    data3 = p.map(job, ["alpha", "beta", "gamma"])
    print(data1)
    print(data2)
    print(data3)
    p.close()
    print(time.time()-start)
