# -*- coding:utf-8 -*- 


#!/usr/bin/env python2.7
#import pyjsonrpc
import jsonrpclib
import time
import os
import sys
import simplejson as json





myname = os.path.abspath(__file__)
all_dict=None

def myadd(a,b):
	return a+b

def getbyname(name):
	ret=[]
	print(name)
	for node in all_dict:
		if(node == name):
			#print()
			ret.append(all_dict[node])	
	return ret

def getbylocation(location):
	ret = []
	for node in all_dict:
		if(all_dict[node]['location'] == location):
			ret.append(all_dict[node])
	return ret

def getbyyear(location, year):
	ret = []
	for node in all_dict:
		if((all_dict[node]['location'] == location) and (int(all_dict[node]['year']) == int(year))):
			ret.append(all_dict[node])
	return ret

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


if __name__ == "__main__":

	port=int(sys.argv[1])
	fname=sys.argv[2]
	with open(fname,'r') as load_f:
		all_dict = json.load(load_f)
	print(all_dict)

	server = SimpleJSONRPCServer(('localhost', port))
	server.register_function(pow)
	server.register_function(lambda x,y: x+y, 'add')
	server.register_function(myadd)
	server.register_function(lambda x,y: x*y, 'times')
	server.register_function(lambda x: x, 'ping')

## register my function --- 

	server.register_function(getbyname)
	server.register_function(getbylocation)
	server.register_function(getbyyear)

	server.serve_forever()
