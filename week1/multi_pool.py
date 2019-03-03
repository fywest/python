from multiprocessing import Pool
import os,time,random

def task(name):
    print('***task {} start, process ID:{}'.format(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('task {} finish, it takes: {:.2f}s'.format(name,(end-start)))


if __name__=='__main__':
    print('current main process ,thread ID: {}'.format(os.getpid()))
    print('-------------------------------------------------')
    p=Pool(4)

    for i in range(1,6):
        p.apply_async(task,args=(i,))

    p.close()
    print('start run child process...')

    p.join()
    print('-------------------------------------------------')
    print('all child process are done,current in main process,process ID: {}'.format(os.getpid()))
