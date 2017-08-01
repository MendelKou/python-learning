# '''
# Python内置了一个WSGI服务器，这个模块叫wsgiref
# '''
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from cont import application

# 创建一个服务器
httpd = make_server('localhost',8000,application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
