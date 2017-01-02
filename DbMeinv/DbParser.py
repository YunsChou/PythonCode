
from bs4 import BeautifulSoup
import urllib.parse
import re

class Parser(object):
	
	def parse(self, url, html):
		soup = BeautifulSoup(html, 'html.parser')
		new_url = self.parse_new_url(url, soup)
		new_data = self.parse_new_data(html, soup)
		return new_url, new_data

	def parse_new_url(self, url, soup):
		li = soup.find('li', class_ = 'next next_page')
		page = li.find('a')['href']
		new_url = urllib.parse.urljoin(url, page)
		return new_url

	def parse_new_data(self, html, soup):
		datas = []
		divs = soup.findAll('div', class_ = 'img_single')
		for div in divs:
			a = div.find('a')
			img = a.find('img')
			data = {}
			data['link'] = a['href']
			data['title'] = img['title']
			data['imgsrc'] = img['src']
			datas.append(data)
		return datas
