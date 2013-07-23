# coding= utf-8

import DBHandler

class MagnetRes(object):
	def __init__(self, magnetURL, title, DBHandler=None):
		# where to handle the unicode
		if cmp(type(magnetURL), 'str') == 0:
			magnetURL = unicode(magnetURL)

		if cmp(type(title), 'str') == 0:
			title = unicode(title)

		self.magnetURL = magnetURL
		self.title = title
		self.DBHandler = DBHandler

	def toDict(self):
		return {u"magnet":self.magnetURL, u"title":self.title}

	def __repr__(self):
		return 'title: '+self.title+'\tmagnet: '+self.magnetURL

	def put(self):
		if self.DBHandler == None:
			self.DBHandler = DBHandler.MagnetDB()

		if self.DBHandler.containTheMagnet(self.magnetURL) == False:
			self.DBHandler.insert(self.toDict())

if __name__ == '__main__':
	db = DBHandler.MagnetDB()
	testRes = MagnetRes(magnetURL='test_url', title='test_title')
	testRes.put()
	print len(db.dump())