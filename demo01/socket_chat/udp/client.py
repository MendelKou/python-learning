import socket,os
client_config = {
    'ip' : '127.0.0.1',
    'port' : 9999,
    'buf_size' : 1024,
    'encoding' : 'utf-8'
}
client_socket = None
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    while True:
        msg = input().strip()
        if msg != '':
            client_socket.sendto(msg.encode(client_config['encoding']),(client_config['ip'],client_config['port']))
            data = client_socket.recv(client_config['buf_size'])
            print(data.decode(client_config['encoding']))
        if msg == 'exit':
            os._exit(0)
except ConnectionError as e:
    print(e)
finally:
    if client_socket:
        client_socket.close()
