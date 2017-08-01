import socket,threading,os
client_config = {
    'server_ip' : '127.0.0.1',
    'server_post' : 9000,
    'encoding' : 'utf-8',
    'buf_size' : 1024
}
#接收消息的线程处理过程
def recv_proc(client_socket):
    try:
        while True:
            print(client_socket.recv(client_config['buf_size']).decode(client_config['encoding']))
    except ConnectionResetError as e:
        print(e)
        os._exit(0)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client_socket.connect((client_config['server_ip'],client_config['server_post']))
    recv_thread = threading.Thread(target=recv_proc,args=(client_socket,),daemon=True)
    recv_thread.start()
    while True:
        msg = input().strip()
        if msg != '':
            client_socket.sendall(msg.encode(client_config['encoding']))
            if msg == 'exit':
                break

except ConnectionResetError as e:
    print(e)
finally:
    client_socket.close()
