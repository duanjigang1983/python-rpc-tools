# -*- coding:utf-8 -*- 


#!/usr/bin/env python2.7
import jsonrpclib
import time
import sys
import simplejson as json
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


if __name__ == "__main__":
	port = sys.argv[1]
	print("URL:http://localhost:%s" % (port))
	server = jsonrpclib.Server('http://localhost:%s' % (port))
	
	## Test for name
	print(server.getbyname("carrie"))
	print(server.getbyname("tarrie"))
	print(server.getbyname("sarrie"))

	## Test for location
	print(server.getbylocation("Los Angeles"))
	print(server.getbylocation("Miami"))
	print(server.getbylocation("Newyork"))

	## Test for year
	print(server.getbyyear("Los Angeles", 2006))
	print(server.getbyyear("Miami", 2009))
	print(server.getbyyear("Newyork", 2004))
