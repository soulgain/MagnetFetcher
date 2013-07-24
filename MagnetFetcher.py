# coding=utf-8

import urllib2, re, threading
from DataModel import MagnetRes

g_lock = threading.Lock()

class MagnetFetcher(object):
	def __init__(self, uri, host='http://bt.shousibaocai.com'):
		self.uri = uri
		self.host = host

	def start(self):
		try:
			html = urllib2.urlopen(self.host+self.uri, timeout=30).read()
			# print html
			reobj = re.compile(r'<a href="/hash/(.*)" target="_blank">(.*)</a>')
			matches = re.findall(reobj, html)
			newCount = 0
			for match in matches:
				magnetRes = MagnetRes(magnetURL='magnet:?xt=urn:btih:'+match[0], title=match[1])
				# print magnetRes
				if magnetRes.put():
					newCount += 1
			
			g_lock.acquire()
			print threading.current_thread(),'total:',len(magnetRes.DBHandler.dump()),self.host+self.uri,' @+%d' % (newCount,)
			g_lock.release()
		except urllib2.HTTPError, e:
			g_lock.acquire()
			print repr(e)+'code:'+str(e.code)+' while handle url: '+self.host+self.uri
			g_lock.release()
			if e.code == 502:
				self.start()
		except urllib2.URLError, e:
			g_lock.acquire()
			print repr(e)+'code:'+str(e.code)+' while handle url: '+self.host+self.uri
			g_lock.release()
			raise(e)

if __name__ == '__main__':
	fetcher = MagnetFetcher(URI='/?s=top')
	fetcher.start()