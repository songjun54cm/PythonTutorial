#coding=utf-8
#!/usr/bin/jython
import thread
from messager import sentMessage, recvMessage
import socket, sys
def FactExtractionThread(clientSocket):
        sentence = recvMessage(clientSocket)
        # print sentence
        facts = extractFactsFromSentence(sentence)
        sentMessage(facts, clientSocket)
        clientSocket.close()
        print facts

def extractFactsFromSentence(sentence):
	try:
		# print sentence
		return 'receive : ' + ''.join(sentence)
	except:
		print "Error: unable to start thread."
		info=sys.exc_info()  
		print info[0],":",info[1]
		print 'after'
		return 'error'

def main():
	s = socket.socket()
	s.bind(('127.0.0.1',8888))
	s.listen(100)
	while 1:
		cs, address = s.accept()
		try :
			thread.start_new_thread(FactExtractionThread, (cs,))
		except:
			print "Error: unable to start thread."
			info=sys.exc_info()  
			print info[0],":",info[1]
			print 'after'
			return

if __name__ == '__main__':
    main()