# coding=utf-8

import threading, time
from Worker import Worker

uriTemplate = '/?s=top&p=%d'

class Dispatch():
	def __init__(self, limit=20):
		self.count = 1
		self.limit = limit

	def runloop(self):
		while True:
			remainLimit = self.limit - threading.activeCount()
			for x in xrange(1,remainLimit):
				uri = uriTemplate % (self.count,)
				self.count+=1
				Worker(uri=uri).start()
			time.sleep(2)

if __name__ == '__main__':
	test = Dispatch(limit=4)
	test.runloop()