#handler
#!/usr/bin/env python
import os,sys
import datetime

class handler(object):
	"""docstring for handler"""
	def __init__(self, arg):
		super(handler, self).__init__()
		self.cmd = arg
	def CmdHandle():
		f = open('./log.txt','a+',encoding='utf-8')
		timeStr = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
		logStr = timeStr + self.cmd
		print logStr
		f.write(logStr)
		f.close()

		