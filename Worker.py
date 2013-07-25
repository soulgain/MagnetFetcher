# coding=utf-8

import threading
from MagnetFetcher import MagnetFetcher

class Worker(threading.Thread):
	def __init__(self, uri):
		threading.Thread.__init__(self)

		self.uri = uri

	def run(self):
		fetcher = MagnetFetcher(uri=self.uri)
		fetcher.start()

if __name__ == '__main__':
	for x in xrange(1,10):
		worker = Worker(uri='?s=top')
		try:
			worker.start()
		except Exception, e:
			worker.start()
		
	
