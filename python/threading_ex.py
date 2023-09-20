"""
In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:

An executable program.
The associated data needed by the program (variables, work space, buffers, etc.)
The execution context of the program (State of process)


A thread is an entity within a process that can be scheduled for execution. 
Also, it is the smallest unit of processing that can be performed in an OS (Operating System). 
In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code. 
For simplicity, you can assume that a thread is simply a subset of a process! A thread contains all this information in a 
Thread Control Block (TCB):


Thread Identifier: Unique id (TID) is assigned to every new thread
Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
Program counter: a register which stores the address of the instruction currently being executed by thread.
Thread state: can be running, ready, waiting, start or done.
Thread’s register set: registers assigned to thread for computations.
Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.

Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

In a simple, single-core CPU, it is achieved using frequent switching between threads. 
This is termed as context switching. In context switching, 
the state of a thread is saved and state of another thread is loaded whenever 
any interrupt (due to I/O or manually set) takes place. 
Context switching takes place so frequently that all the threads appear to be running parallelly 
(this is termed as multitasking).

"""


import threading



def add(start, n, ans=None):
    sum_ = 0
    for i in range(start, n):
        sum_ += i
        
    if not ans:
      return sum_
    ans.append(sum_)



if __name__=="__main__":
  
    n = 1000000
    #n = 100
    thread_no = 10
    
    num = n // thread_no
    
    print("num", num)
    
    if num == 0:
      print(add(0, n+1))
    else:
      ans = [0] * thread_no
      threads = []
      for i in range(thread_no):
        curr_num = (i * num) + 1
        end_num = curr_num + num
        threads.append(threading.Thread(target=add, args=(curr_num, end_num, ans)))
      
      for i in threads:
        i.start()
        i.join()
      
      sum_ = 0
      for i in ans:
        sum_ += i
      
      print(sum_)


"""
Thread synchronization is defined as a mechanism which ensures that two or more 
concurrent threads do not simultaneously 
execute some particular program segment known as critical section.

Critical section refers to the parts of the program where the shared resource is accessed.


threading module provides a Lock class to deal with the race conditions. Lock is implemented using a 
Semaphore object provided by the Operating System.

A semaphore is a synchronization object that controls access by multiple processes/threads 
to a common resource in a parallel programming environment. It is simply a value in a designated place 
in operating system (or kernel) storage that each process/thread can check and then change. 
Depending on the value that is found, the process/thread can use the resource or will find that 
it is already in use and must wait for some period before trying again. Semaphores can be binary (0 or 1) 
or can have additional values. Typically, a process/thread using semaphores checks the value and then, 
if it using the resource, changes the value to reflect this so that subsequent semaphore users will know to wait.

"""



import threading


x = 0


def increment():
  global x
  x += 1

def increment_func(lock):
  for i in range(10000):
    lock.acquire()
    increment()
    lock.release()

def main_task():
  global x
  x = 0
  
  lock = threading.Lock()
  
  t1 = threading.Thread(target=increment_func, args=(lock,))
  t2 = threading.Thread(target=increment_func, args=(lock,))
  
  t1.start()
  t2.start()
  
  t1.join()
  t2.join()

if __name__=="__main__":
  
  for i in range(10):
    main_task()
    print("Iteration", i, "x", x)
  




import multiprocessing



def square_func(lis, result, square_sum):
  
  for i in range(len(lis)):
    result[i] = lis[i] * lis[i]
    
  square_sum.value = sum(result)



def main_task():
  
  
  lis = [1,2,3,4]
  
  result = multiprocessing.Array('i', 4)
  square_sum = multiprocessing.Value('i')
  
  
  p1 = multiprocessing.Process(target=square_func, args=(lis, result, square_sum))
  p2 = multiprocessing.Process(target=square_func, args=(lis, result, square_sum))

  
  p1.start()
  p2.start()
  
  p1.join()
  p2.join()
  
  print("Result(in main program): {}".format(result[:]))
  # print square_sum Value
  print("Sum of squares(in main program): {}".format(square_sum.value))
  
  
if __name__ == "__main__":
  main_task()