#!/usr/bin/python3

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1Hash = input('[*]Enter Sha1 Hash: ')

#opens passlist from url
passList = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for password in passList.split('\n'):
	#because its from the internet we need to add the bytes function and encode it with utf-8(standard encoder) as we did above
	#hex digest makes it sha1 from string
	hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
	if hashguess == sha1Hash:
		print(colored('[+] Password is: ' + str(password), 'green'))
		quit()
	else:
		print(colored('[-]Password ' + str(password) + ' doesnt match, trying next...', 'red'))

print('Password not found')

