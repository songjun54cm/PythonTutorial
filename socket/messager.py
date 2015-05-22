#coding=utf-8
#!/usr/bin/jython

def recvMessage(clientSocket):
        message = []
        headlength = 10
        buffer_size = 1024
        # receive the head of the message which is the length of the message
        current_message = clientSocket.recv(headlength)
        meg_len = int(current_message)
        # print meg_len

        message_len = 0
        while True:
                if message_len<meg_len:
                        current_message = clientSocket.recv(buffer_size)
                        # print current_message
                        message += current_message
                        message_len += len(current_message)
                else:
                        break
        return message

def sentMessage(message, current_socket):
        headlength = 10
        meg_len = str(len(message))
        llen = len(meg_len)
        headbits='0'*headlength
        # append the length of message at the first headlength bytes
        headbits = headbits[0:headlength-llen]+meg_len
        message = headbits+message
        try:
                current_socket.sendall(message)
        except:
                print 'Error happened!'