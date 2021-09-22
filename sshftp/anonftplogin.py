#!/usr/bin/python3

import ftplib

def anonLogin(host):
	try:
		ftp = ftplib.FTP(host)
		ftp.login('anonoymus', 'anonoymus')
		print ('[+] ' + host + 'FTP Anonoymus login succeded')
		ftp.quit
		return True;
	except:
		print ('[!!]Could not login Anonymusly')

host = input('Enter IP Address: ')
anonLogin(host)
