
import os
print('%s' % os.getpid())
## 跨平台版本的Process
from multiprocessing import Process
from multiprocessing import Pool
def child_running(args):
    print('running')
if __name__=='__main__':
   p=Process(target=child_running(),args=('test',))
   p.start()
   p.join()

## 进程池的方式
import  time,random
def long_time_task(name):
    start=time.time()
    time.sleep(random.random*3)
    end=time.time()
    print('执行了%.2f' % (name,start-end))
if __name__=='__main__':
   p=Pool(4)
   for i in range(5):
       p.apply_async(long_time_task,args=(i,))
   p.close()
   p.join() ##  对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()

## 进程间的相互通信
from multiprocessing import Queue,Process
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
###------------------------多线程--------------------------------##
import threading
t=threading.Thread(target=child_running,name='log_thread')
t.start()
t.join()

### Lock 多线程安全的模块
banlan=1
lock=threading.Lock()
def run_thread():
    for i in range(50):
        # 获取锁
        lock.acquire()
        try:
            banlan=33+banlan
        finally:
            lock.release()

### ThreadLocal 的线程安全类 每个线程都只能读写自己线程的独立副
local_sch=threading.local()


### r 就是转义的标志
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

re.split(r'[\s\,\;]+', 'a,b;; c  d')

















