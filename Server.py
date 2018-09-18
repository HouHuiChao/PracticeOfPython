#server.py
#!/usr/bin/env python
from multiprocessing import Process
import os
import socket
import datetime

def CmdHandle(cmd):
    f = open('./log.txt','a+')
    timeStr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logStr = timeStr +"\t" + cmd + "\n"
    print logStr
    f.write(logStr)
    f.close()

def Server():
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8080))
    sock.listen(5)
    while True:
        connection, address=sock.accept()
        try:
            connection.settimeout(500)
            while True:
                buf=connection.recv(512)
                if not buf:
                    raise socket.timeout
                print buf
                p = Process(target=CmdHandle, args=(buf,))
                p.start()
                p.join()
                connection.send('Done!'.encode('utf-8'))
                CmdHandle('Done!')
        except socket.timeout:
            print 'socket error'
            connection.send('socket error!'.encode('utf-8'))
            CmdHandle('socket error!')
            connection.close()
            break
    sock.close()

if __name__=='__main__':
    Server()
