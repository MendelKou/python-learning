import random,time,queue
from multiprocessing.managers import BaseManager
#创建类似的QueueManager
class QueueManager(BaseManager):
    pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器
server_addr = '127.0.0.1'
print(str.format('Connect to server {0}',server_addr))
#端口与验证码与task_master保持一致
m = QueueManager(address=(server_addr,9001),authkey=b'abc')
#从网络连接
m.connect()
# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()
#从task去任务 并将结果写入result
for i in range(10):
    try:
        n = task.get(timeout=1)
        print(str.format('get task {0}',n))
        r = n*n
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty!')
print('worker exit')
