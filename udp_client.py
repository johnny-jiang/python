#udp_client.py
import socket
import time,threading

def udpclient(no):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.sendto(data, ('127.0.0.1', 9999))
        # 接收数据:
        print('Thread ',no,s.recv(1024).decode('utf-8'))
    s.close()

for i in range(0,500):
    t = threading.Thread(target=udpclient,args=(i,))
    t.start()