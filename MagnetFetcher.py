# coding=utf-8

import urllib2, re
from DataModel import MagnetRes


class MagnetFetcher(object):
	def __init__(self, uri, host='http://bt.shousibaocai.com'):
		self.uri = uri
		self.host = host

	def start(self):
		try:
			# target
			# <a href="/hash/b760f2bfe0c9b25ac402c8c9ebd29c444c44ebcb" target="_blank">CWP-87-AVI</a>
			html = urllib2.urlopen(self.host+self.uri).read()
			# print html
			reobj = re.compile(r'<a href="/hash/(.*)" target="_blank">(.*)</a>')
			matches = re.findall(reobj, html)
			for match in matches:
				magnetRes = MagnetRes(magnetURL='magnet:?xt=urn:btih:'+match[0], title=match[1])
				# print magnetRes
				magnetRes.put()

			print len(magnetRes.DBHandler.dump())
			return True

		except Exception, e:
			print repr(e)+'while handle url: '+self.host+self.uri
			return False	

if __name__ == '__main__':
	fetcher = MagnetFetcher(URI='/?s=top')
	fetcher.start()