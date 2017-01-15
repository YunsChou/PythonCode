
import pymongo
from flask import Flask, request, jsonify
import json


app = Flask(__name__)

@app.route('/')
def function():
	return 'hello world'


@app.route('/meinv', methods = ['GET'])
def findMeinv():
	con = pymongo.MongoClient()
	db = con['picture']
	col = db['meinv']
	items = []
	res = col.find().skip(0).limit(10)
	for item in res:
		print(dict(item))
		items.append({'title':item['title'],'imgsrc':item['imgsrc'], 'link':item['link']})
	return jsonify(items)

if __name__ == '__main__':
	app.run()