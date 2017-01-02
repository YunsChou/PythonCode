
import pymongo

con = pymongo.MongoClient()
db = con['mongon-test1-db']
col = db['girls']

class Outputer(object):
	
	def __init__(self):
		self.datas = []
		

	def collect_data(self, data):
		if data is None:
			return None
		self.datas.extend(data)

	def output(self):
		print('--------------------------------------------------------')
		# print(self.datas)
		# self.col.insert(self.datas)
		for data in self.datas:
			is_exist = self.col.find_one({'imgsrc':data['imgsrc']})
			print(is_exist)
			if is_exist == None:
				col.insert(data)
		# 	print(data)
			# print('link : %s, title : %s, imgsrc : %s' %(data['link'], data['title'], data['imgsrc']))
			# girl = {"title":data['title'],"link":data['link'],"imgsrc":data['imgsrc']}
			
		# self.col.insert(girls)
		
		