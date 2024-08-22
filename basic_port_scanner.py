#!/bin/python3

import sys
import socket
from datetime import datetime

#Define your target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translates host to IPV4
else:
	print("Invalid number of Arguments")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("." * 100)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("." * 100)

#Try checking for open ports to connect to
try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #sets default port scantime to 1 sec
		result = s.connect_ex((target, port)) #gives result after scan of port for the given target/ip
		if result == 0:
			print(f"Port {port} is open") #if port results to zero, the it's open, if 1 port is closed
		s.close #else, close the connection
		
except KeyboardInterrupt:
	print("\n")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Could not connect to server.")
	sys.exit()
