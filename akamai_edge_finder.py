#!/usr/bin/python
import socket
import time
import Queue
import threading

error_count = 0;

l = 0x62
a = 0;
w = 0;
q = Queue.Queue()

addr = "";

ips = []
outfile="akami-ips.txt"

f = open(outfile, "a")

def thread_job():

	q.put(doit(q,a,w, letter1, letter))

def doit(q, a, w, l1, l):

	global error_count

	time.sleep(w)
	addr = chr(l1) + str(a) + '.' + chr(l) +'.akamai.net';
	
	try:
		saddr = socket.getaddrinfo( addr, 80)
	except:
		print "\033[1;31m[!]\033[0m Error on host %s" % addr
		error_count = error_count + 1
		return

	for s1 in saddr:
		cur_ip = s1[4][0];
		if cur_ip not in ips:
			ips.append(cur_ip)
			f.write(cur_ip+"\n")
			print "\033[1;32m[+]\033[0m '%s' found." % cur_ip
		else:
			return
	

count = 0
count2 = 0

for letter1 in range(0x61, 0x7a):
	for letter in range(0x61, 0x7a):

		print "\033[1;31m[+]\033[0m letter: %s" % chr(letter)		

		for a in range (1, 1000):

			count = count + 1

			if (count == 100):
				count2 = count2 + 1
				p = count2 * 10.0
				p2 = (p / 1000.0) * 100.0

				print "\033[1;31m[ Progress: %d%s]\033[0m" % ( p2, chr(0x25) ) 
				count = 0

			t = threading.Thread(target=thread_job(), args=(q,a,w, letter1, letter))
			t.daemon = True
			t.start()

			if error_count == 200:
				error_count = 0
				count2 = 0
				break

		count2 = 0
