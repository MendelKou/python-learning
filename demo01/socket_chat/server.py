import socket,threading
server_config = {
    'addr' : '127.0.0.1',
    'port' : 9000,
    'max_conn' : 6,
    'encoding' : 'utf-8',
    'buf_size' : 1024
}
client_sockets = {}
lock = threading.Lock() #创建锁
#与客户端交互的过程
def client_handler(client_socket,client_addr):
    client_sockets[client_addr] = client_socket # 加入用户字典
    greeting = 'Welcome '+str(client_addr)
    client_socket.sendall(greeting.encode(server_config['encoding']))
    sendMsg(client_addr,str(client_addr)+' connected')
    try:
        while True:
            data = client_socket.recv(server_config['buf_size'])
            msg = data.decode(server_config['encoding']).strip()
            if msg and msg != 'exit':
                msg = str(client_addr)+':'+msg
                sendMsg(client_addr,msg) #将消息发送给其它人
                print(msg)
            else:
                break
        msg = str(client_addr)+' disconnected'
        sendMsg(client_addr,msg) #广播此人已离线
        print(msg)
        del client_sockets[client_addr]
    except ConnectionResetError as e:
        print(e)

#将消息发给除指定地址外的用户
def sendMsg(except_client_addr,msg):
    try:
        lock.acquire()
        for client_addr in client_sockets:
            if client_addr != except_client_addr:
                client_sockets[client_addr].sendall(msg.encode(server_config['encoding']))
    finally:
        lock.release()

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((server_config['addr'],server_config['port']))
server_socket.listen(server_config['max_conn'])
print('Server is running...')
while True:
    client_socket,client_addr = server_socket.accept()
    print(str.format('Connected by {0}',client_addr))
    # 创建新的线程处理此客户端的交互
    client_thread = threading.Thread(target=client_handler,args=(client_socket,client_addr))
    client_thread.start()
server_socket.close()
print('Server closed')
