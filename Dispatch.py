# coding=utf-8

import threading, time, sys, argparse
from Worker import Worker


uriTemplate = '/?s=top&p=%d'

class Dispatch():
	def __init__(self, limit=20, start=1, end=sys.maxint):
		self.current = start
		self.limit = limit
		self.end = end

	def runloop(self):
		while self.current <= self.end:
			remainLimit = self.limit - threading.activeCount()
			if remainLimit > 0:
				for x in xrange(1, remainLimit):
					uri = uriTemplate % (self.current,)
					self.current += 1
					worker = Worker(uri=uri)
					worker.daemon = True
					worker.start()
					# worker.join()
			
			time.sleep(2)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-threads', help='limit the max threads number to use', type=int, default=10)
	parser.add_argument('-start', help='set the start page number', type=int, default=1)
	parser.add_argument('-end', help='set the end page number', type=int, default=sys.maxint)

	args = parser.parse_args()
	Dispatch(limit=args.threads, start=args.start, end=args.end).runloop()
