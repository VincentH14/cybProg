#!/usr/lib/python3

import pexpect

#Keys used for shell
PROMPT = ['# ', '>>> ', '> ', '\$ ']


#remember child is equal to the return of connect()
def send_command(child,command):
	child.sendline(command)
	#expects the shell keys
	child.expect(PROMPT)
	#prints output of command
	print(child.before)


def connect(user,host,password):
	#key asked when connected
	ssh_newkey = 'Are you sure you want to continue connecting'
	#key for connecting
	connStr = 'ssh ' + user + '@' + host
	#sets child as connstr
	child = pexpect.spawn(connStr)
	#setting var for when ssh_newkey shows up
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
	if ret == 0:
		print ('[!!] Error Connecting')
	if ret == 1:
		#dealing with prompt
		child.sendline('yes')
		ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
		if ret == 0:
			print ('[!!] Error Connecting')
			return
	#sending pass
	child.sendline(password)
	child.expect(PROMPT)
	return child

def main():
	host = '192.168.1.148'
	user = 'msfadmin'
	password = 'msfadmin'
	child = connect(user,host,password)
	send_command(child, 'ls')

main()
