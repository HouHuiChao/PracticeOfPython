#client.py
#!/usr/bin/env python
import socket
import time
 
def Client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',8080))
    str = raw_input("Command:");
    while str != "quit":
    	client.send(str.encode('utf-8'))
    	s = client.recv(512)
    	print s
    	time.sleep(1)
    	str = raw_input("Command:");
    client.close()
     
if __name__=='__main__':
    Client()
 