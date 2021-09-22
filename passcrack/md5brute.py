#!/usr/bin/python3

from termcolor import colored
import hashlib

def tryOpen(wordlist):
	try:
		pass_file = open(wordlist, 'r')
		return pass_file
	except:
		print ('[!!]Unable to Open File!')
		quit()

pass_hash = input('[*]Enter MD5 Hash: ')
wordlist = input('[*]Enter Path to File: ')


for word in tryOpen(wordlist):
	print (colored('[-]Trying: ' + word.strip('\n'), 'red'))
	enc_word = word.encode('utf-8')
	md5Digest = hashlib.md5(enc_word.strip()).hexdigest()

	if md5Digest == pass_hash:
		print (colored('[+]Password Found: ' + word, 'green'))
		quit()
print ('[!!]Password not found!')
