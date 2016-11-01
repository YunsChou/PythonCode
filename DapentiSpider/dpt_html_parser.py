#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import re
import dpt_html_downloader
import time

class Parser(object):
	
	def __init__(self):
		self.downloader = dpt_html_downloader.Downloader()

	def parse(self, root_url, html):
		if html is None:
			return

		soup = BeautifulSoup(html, 'html.parser')
		self.parse_title(root_url, soup)

	def parse_title(self, root_url, soup):
		links = soup.find('div', align = 'left').find('ul').findAll('li')
		testNum = 0
		for link in links:
			a_tag = link.find('a')
			href = a_tag['href']
			title = a_tag.string
			newsid = self.parse_newsid(href)
			content = self.parse_content(root_url, href)
			print('href : %s, title : %s, newsid : %s, content : %s' %(href, title, newsid, content))
			testNum = testNum + 1
			if testNum > 3:
				break

	def parse_newsid(self, href):
		newsid = re.findall(r'&id=(\d*)', href)[0]
		return newsid

	def parse_content(self, root_url, href):
		content_url = root_url + href
		# print('content_url : %s' %content_url)
		time.sleep(1)
		content_html = self.downloader.download(content_url)
		soup = BeautifulSoup(content_html, 'html.parser')
		contents = soup.find('div', class_ = 'oblog_text').strings
		if contents is None:
			contents = soup.find('div', class_ = 'WB_info').strings
		content_text = ''
		for content in contents:
			if len(content.string) > 0:
				content_text += content.string
		
		return content_text


	def parse_tupian(self, html):
		soup = BeautifulSoup(html, 'html.parser',  from_encoding='utf-8')
		title_nodes = soup.findAll('span', class_ = 'style1')
		img_nodes = soup.findAll('tr')

		tupianSrc = []
		for img_node in img_nodes:
			img = img_node.find('img')
			if img is not None:
				src = img.attrs['src']
				if len(src) > 0:
					tupianSrc.append(src)

		for i in range(len(title_nodes)):
			title_node = title_nodes[i]
			a_tag = title_node.find('a')
			href = a_tag['href']
			title = a_tag.string
			newsid = self.parse_newsid(href)
			print('href : %s, title : %s, newsid : %s' %(href, title, newsid))

			src = tupianSrc[i + 1]
			print('src : %s' %src)