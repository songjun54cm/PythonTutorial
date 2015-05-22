import socket
from messager import sentMessage

s=socket.socket()
s.connect(('127.0.0.1',8888))
d = sentMessage('hello world',s)
print 'sent message len' + str(d)
s.close()