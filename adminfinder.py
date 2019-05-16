#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n: ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print " i Found it : ",req_link

def Credit():
	Space(9); print "                                        "
	Space(9); print "                                        "
	Space(9); print "         [+]  By NAV HACK  [+]            "
	Space(9); print "          Twitter @NavAlhazmi              "
	Space(9); print "[+] DKU : DNU : BOOD : DmarKu : Bo6re5m [+]              "

       
Credit()
findAdmin()
