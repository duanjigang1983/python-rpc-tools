# -*- coding:utf-8 -*- 


#!/usr/bin/env python2.7
#import pyjsonrpc
import jsonrpclib
import time
import simplejson as json
import sys


bs_list = []



def index_name(name):
	set1="abcdefghijklm"
	pos=set1.find(name[:1])
	if(pos >= 0):
		return 0 # server 1
	else:
		return 1 # server2

def getbyname(name):
	res=[]
	try:
		ret = bs_list[index_name(name)]['func'].getbyname(name)
		if(len(ret) > 0):
			res.append(ret)
	except TypeError:
		return {"success":False, "message": "Error input"}
	except IOError:
		return {"success":False, "message": "worker %s unavailable" % (bs_list[index_name(name)]['url'])}
	return res

def getbylocation(location):
	res=[]
	for node in bs_list:
		## incase of any exception reply to client
		try:
			ret = node['func'].getbylocation(location)
			if(len(ret) > 0):
				res.append(ret)
		except TypeError:
			return {"success": False, "message":"Error input"}
			#print("TypeError")
		except IOError:
			res.append({"success":False, "message": "worker %s unavailable" % node['url']})
		
	return res

def getbyyear(location, year):
	res=[]
	for node in bs_list:
		try:
			ret = node['func'].getbyyear(location, year)
			if(len(ret) > 0):
				res.append(ret)
		except TypeError:
			return {"success": False, "message":"Error input"}
		except IOError:
			res.append({"success":False, "message": "worker %s unavailable" % node['url']})
	return res


from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


if __name__ == "__main__":
	port  = int(sys.argv[1])
	server = SimpleJSONRPCServer(('localhost', port))

	back_server=[{"addr":"localhost", "port":"23001"},{"addr":"localhost", "port":"23002"}]
	for i in back_server:
		url='http://%s:%s' % (i['addr'], i['port'])
		bs=jsonrpclib.Server(url)
		bs_list.append({"url":url, "func" : bs})
	#server.register_function(pow)
	#server.register_function(lambda x,y: x+y, 'add')
	#server.register_function(lambda x,y: x*y, 'times')
	#server.register_function(lambda x: x, 'ping')

## register my function --- 

	server.register_function(getbyname)
	server.register_function(getbylocation)
	server.register_function(getbyyear)
	server.serve_forever()
