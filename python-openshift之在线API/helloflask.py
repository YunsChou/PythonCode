#-*- coding:utf-8 -*-

from flask import Flask
from flask import jsonify
import hellospider

app = Flask(__name__)

@app.route('/')
def hello_flask():
	return 'hello_flask!'

@app.route('/hot')
def spider_hot():
	# 1、传入URL
	root_url = 'http://www.pythontab.com/'
	spider = hellospider.SpiderMain()
	# 2、返回数据
	hot_datas = spider.Crawl(root_url)
	return jsonify(hot_datas)

if __name__ == '__main__':
	app.run()