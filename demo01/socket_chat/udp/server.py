import socket
server_config = {
    'ip' : '127.0.0.1',
    'port' : 9999,
    'buf_size' : 1024,
    'encoding' : 'utf-8'
}
clients = []
server_socket = None;
# def send_msg(except_addr,msg):
#     for addr in clients:
        # if addr != except_addr:
        # server_socket.sendto(msg.encode(server_config['encoding']),addr)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((server_config['ip'],server_config['port']))
try:
    while True:
        data,addr = server_socket.recvfrom(server_config['buf_size'])
        # if addr not in clients:
        #     clients.append(addr)
        msg = data.decode(server_config['encoding'])
        # if msg == 'exit':
        #     msg = ' exited'
        #     if addr in clients:
        #         clients.remove(addr)
        msg = '%s:%s' % (addr,msg)
        print(msg)
        server_socket.sendto(msg.encode(server_config['encoding']),addr)
        # send_msg(addr,msg)
except ConnectionError as e:
    print(e)
finally:
    if server_socket:
        server_socket.close()
