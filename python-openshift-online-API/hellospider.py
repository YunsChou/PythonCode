#-*- coding:utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

# 一、爬虫调度器
class SpiderMain(object):
	# 二、爬虫部分
	def Crawl(self, url):
		# 1、URL管理器
		hot_url = url
		# 2、网页下载器
		if url is None:
			return None
		response = urllib.request.urlopen(hot_url)
		if response.getcode() != 200:
			return None
		htmldata = response.read()
		# 3、网页解析器
		hot_datas = []
		soup = BeautifulSoup(htmldata, 'html.parser')
		links = soup.find('div', class_ = 'news-hot').findAll('a')
		for link in links:
			hot_data = {}
			hot_data['href'] = link['href']
			hot_data['title'] = link.string
			hot_datas.append(hot_data)
		# 三、数据输出
		return hot_datas