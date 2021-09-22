#!/usr/bin/python

import socket
import os
import sys

#Function for returning the banner
def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		#connecting to the ip
		s.connect((ip,port))
		#sends back the banner
		banner = s.recv(1024)
		return banner
	except:
		return

#Function for comparing the banner to a list of vulnerable banners
def checkVulns(banner,filename):
	f = open(filename, "r")
	for line in f.readlines():
		if line.strip("\n") in banner:
			print '[+] Server is vulnerable: ' + banner.strip("\n")


def main():
	#statment for getting the filename for the comparison

	#makes sure there are 2 agruments
	if len(sys.argv) == 2:
		#sets filename as the second arg
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[!!] File Doesnt Exist!'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[!!] Acess Denied!'
			exit(0)
	else:
			print '[!!] Usage: ' + str(sys.argv[0]) + '<filename>'
			exit(0)
	portlist = [21,22,25,80,110,443,445]
	#checks each port for vuln
	for x in range(147,149):
		ip = "192.168.1." + str(x)
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print '[+] ' + ip + "/" + str(port) + " : " + banner
				checkVulns(banner, filename)
main()
