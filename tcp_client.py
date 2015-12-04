#tcp_client.py

import socket
import time,threading

def tcpclient(no):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('127.0.0.1',9999))
    # 接收欢迎消息:
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.send(data)
        print('thread ',no,s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

for i in range(0,200):
    t = threading.Thread(target=tcpclient,args=(i,))
    t.start()