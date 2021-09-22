#!/usr/bin/python3

import crypt

def crackPass(cryptWord):
	salt = cryptWord[0:2]
	dict = open('dictionary.txt', 'r')
	for word in dict.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word,salt)
		if cryptWord == cryptPass:
			print('[+]Password Found: ' + word)
			exit()




def main():
	passFile = open('cryptpass.txt' , 'r')
	for line in passFile.readlines():
		if ':' in line:
			user = line.split(':')[0]
			cryptWord = line.split(':')[1].strip(' ').strip('\n')
			print ('[*]Cracking Password for: ' + user)
			crackPass(cryptWord)

main()
