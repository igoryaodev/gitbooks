import multiprocessing
import time

g_list = list()

def set_list():
  for i in range(5):
    g_list.append(i)
    print('add', g_list)
    time.sleep(0.5)

def read_list():
  print('read', g_list)

def main():
  add_process = multiprocessing.Process(target=set_list)
  read_process = multiprocessing.Process(target=read_list)
  add_process.start()
  add_process.join()
  read_process.start()
  print('main', g_list)


if __name__ == "__main__":
  main()