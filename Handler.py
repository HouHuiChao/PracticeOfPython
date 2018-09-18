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
		f = open('./log.txt','a+')
		timeStr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		logStr = timeStr + "\t" + self.cmd + "\n"
		print logStr
		f.write(logStr)
		f.close()

		