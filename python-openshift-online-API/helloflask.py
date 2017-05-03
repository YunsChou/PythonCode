#-*- coding:utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import render_template
import hellospider

app = Flask(__name__)

@app.route('/')
def hello_flask():
	return 'hello flask!'

@app.route('/hot')
def spider_hot():
	# 1、待传入URL
	root_url = 'http://www.pythontab.com/'
	# 2、实例化爬虫对象
	spider = hellospider.SpiderMain()
	# 3、传入URL，接收返回数据
	hot_datas = spider.Crawl(root_url)
	# 4、将接收的数据转为JSON格式输出
	return jsonify(hot_datas)

@app.route('/temp', methods = ['GET', 'POST'])
def temp_flask():
	return render_template('home.html')

if __name__ == '__main__':
	app.run()