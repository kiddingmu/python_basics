import multiprocessing
import time

def worker():
    """worker function"""
    print 'worker'
    #time.sleep(2)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
