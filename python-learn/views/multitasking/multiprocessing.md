> 1 导入进程包

```
import multiprocessing
import time
import os

# tasks
def sing(name, title):
  show_tuple_info(name, title)
  # 获取父进程编号
  print('sing_process_parent_id-', os.getppid())
  # 获取当前进程（子进程）的编号
  print('sing_process_id-', os.getpid())
  for i in range(5):
    print("唱歌..."+  str(i))
    time.sleep(1)

def listen(age, area):
  show_dictionary_info({'age': age, 'area': area})
  listen_process_id = os.getpid()
  #
  print('listen_process_id-', listen_process_id)
  #
  print('current_process-', listen_process_id, multiprocessing.current_process())
  for i in range(5):
    print("听..." + str(i))
    time.sleep(1)
    # 根据进程编号强制杀死指定进程
    os.kill(listen_process_id, 9)

# 元组方式传参
def show_tuple_info(name, title):
  print(name, title)
# 字典方式传参
def show_dictionary_info(obj):
  print(obj)
  
sing_process = multiprocessing.Process(target=sing, name='sing_process', args=('igor', 'test'))
listen_process = multiprocessing.Process(target=listen, name='listen_process', kwargs={'age': 20, 'area': 'china'})

def main():
  print('main_process_id-', os.getpid())
  sing_process.start()
  listen_process.start()


if __name__ == "__main__":
    main()
```

> Process进程类的说明

__Process([group[, target[, name[, args [, kwargs]] ]]])__

- group: 指定进程组，目前只能使用None
- target: 执行的目标任务名
- name: 进程的目标任务名
- args： 以元组的方式给执行任务传参
- kwargs: 以字典方式给执行任务传参

<br>

__Process创建的实例对象的常用方法__

- start(): 启动子进程实例（创建子进程）
- join(): 等待子进程执行结束
- terminate(): 不管任务是否完成，立即终止子进程

<br>

__Process创建的实例对象的常用属性：__

- name: 当前进程的别名，默认Process-N，N为从1开始的递增整数

<br>
- 父进程
- 子进程
- 传参
  - 元组
  - 字典
  - 注意： 进程之间不共享全局变量

