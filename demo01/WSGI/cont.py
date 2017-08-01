'''
实现WSGI的接口以响应HTTP请求的函数
'''
# 第一个参数包含请求信息
def application(environ,start_response):
    # start_response函数只能调用一次 用于设置响应头信息
    start_response(
        '200 OK',
        [
            ('Content-Type','text/html'),
        ]
    )
    return [b'<h1>Hello, web!</h1>',str(environ).encode('utf-8')]
