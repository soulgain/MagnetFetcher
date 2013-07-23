# coding=utf-8

import pymongo

class MagnetDB(object):
	def __init__(self, host='127.0.0.1', port=1234):
		# no connect
		# that is desp
		try:
			self.db = pymongo.MongoClient(host=host, port=port).magnets
			self.collection = self.db.testCollection
		except:
			print 'fatal error'
			sys.exit(1)

	def containTheMagnet(self, magnetURL):
		if self.collection.find_one({'magnet':magnetURL}):
			return True
		else:
			return False

	def insert(self, dictToInsert):
		self.collection.insert(dictToInsert) 

	def dump(self):
		return list(self.collection.find(max=100))

	def test(self):
		return self.db

	def insertTest(self):
		theRes = {'magnet':'test_magnet_url', 'title':'test_res_title'}

		if self.containTheMagnet(theRes['magnet']) == False:
			return self.collection.insert(theRes.toDict())
		else:
			return None

if __name__ == '__main__':
	testDB = MagnetDB()
	print testDB.test()
	print testDB.insertTest()
	print len(testDB.dump())

