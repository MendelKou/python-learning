import random,time,queue
from multiprocessing.managers import BaseManager
#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()
#从BaseManager继承
class QueueManager(BaseManager):
    pass
# 把两个Queue都注册到网路上 callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
#绑定端口 设置验证码
manager = QueueManager(address=('',9001),authkey=b'abc')
#启动queue
manager.start()
# 获取通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
#放几个任务进去
for i in range(10):
    n = random.randint(0,10000)
    print(str.format('Put {0} into task queue',n))
    task.put(n)
# 从result队列获取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print(str.format('Result: {0}',r))
# 关闭
manager.shutdown()
print('Master exit')
