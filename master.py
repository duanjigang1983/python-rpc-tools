# -*- coding:utf-8 -*- 


#!/usr/bin/env python2.7
import pyjsonrpc
import jsonrpclib
import time
import simplejson as json


bs_list = []



def index_name(name):
	set1="abcdefghijklm"
	pos=set1.find(name[:1])
	if(pos >= 0):
		return 0 # server 1
	else:
		return 1 # server2

def getbyname(name):
	return bs_list[index_name(name)].getbyname(name)

def getbylocation(location):
	res=[]
	for func in bs_list:
		ret = func.getbylocation(location)
		if(len(ret) > 0):
			res.append(ret)
		
	return res

def getbyyear(location, year):
	res=[]
	for func in bs_list:
		ret = func.getbyyear(location, year)
		if(len(ret) > 0):
			res.append(ret)
		
	return res


from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


if __name__ == "__main__":
	server = SimpleJSONRPCServer(('localhost', 23000))

	back_server=[{"addr":"localhost", "port":"23001"},{"addr":"localhost", "port":"23002"}]
	for i in back_server:
		bs=jsonrpclib.Server('http://%s:%s' % (i['addr'], i['port']))
		bs_list.append(bs)
	#server.register_function(pow)
	#server.register_function(lambda x,y: x+y, 'add')
	#server.register_function(lambda x,y: x*y, 'times')
	#server.register_function(lambda x: x, 'ping')

## register my function --- 

	server.register_function(getbyname)
	server.register_function(getbylocation)
	server.register_function(getbyyear)
	server.serve_forever()
