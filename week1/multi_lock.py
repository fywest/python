import time
from multiprocessing import Process,Value,Lock

def func(val):
    for i in range(50):
        time.sleep(0.01)
        with lock:
            val.value+=1


if __name__=='__main__':
    
    val=Value('i',0)
    lock=Lock()
    procs=[Process(target=func,args=(val,)) for i in range(10)]

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    print(val.value)
