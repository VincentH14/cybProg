
#!/user/bin/python

from socket import *
import optparse
from threading import *

def checkVulns(banner,filename):
        f = open(filename, "r")
        for line in f.readlines():
                if line.strip("\n") in banner:
                        print '[+] Server is vulnerable: ' + banner.strip("\n")


def retBanner(tgtHost,tgtPort):
        try:
                socket.setdefaulttimeout(2)
                s = socket.socket()
                s.connect((tgtHost,tgtPort))
                banner = s.recv(1024)
		print banner
                return banner
        except:
                return

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print '[+] %d/tcp Open' %tgtPort
	except:
		print '[-] %d/tcp Closed' %tgtPort


def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print '[!!] Unkown Host %s' %tgtHost
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '[+] Scan Results for: ' + tgtIP
	except:
		print '[+] Scan Results for: ' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args = (tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('Usage of Program: ' + '-H <target host> -p <target port> -f <filename.txt>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports sperated by comma')
	parser.add_option('-f', dest='filename', type='string', help='specify filename')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	filename = options.filename
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)

	retBanner(tgtHost,tgtPorts)
	banner = retBanner(tgtHost, tgtPorts)
	print tgtHost + str(tgtPorts)
	portScan(tgtHost, tgtPorts)

	if banner:
		print '[+] ' + tgtHost + "/" + str(tgtPorts) + " : " + banner
                checkVulns(banner, filename)



if __name__ == '__main__':
	main()
