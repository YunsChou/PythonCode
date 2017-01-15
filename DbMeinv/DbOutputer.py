
import pymongo



class Outputer(object):
	
	def __init__(self):
		self.datas = []
		con = pymongo.MongoClient()
		db = con['picture']
		self.col = db['meinv']
		

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
			# print(is_exist)
			if is_exist == None:
				self.col.insert(data)
		# 	print(data)
			# print('link : %s, title : %s, imgsrc : %s' %(data['link'], data['title'], data['imgsrc']))
			# girl = {"title":data['title'],"link":data['link'],"imgsrc":data['imgsrc']}
			
		# self.col.insert(girls)
		
		