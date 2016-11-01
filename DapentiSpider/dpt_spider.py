#-*- coding:utf-8 -*-

import dpt_url_manager, dpt_html_downloader, dpt_html_parser, dpt_content_outputer

class SpiderMain(object):
	
	def __init__(self):
		self.downloader = dpt_html_downloader.Downloader()
		self.parser = dpt_html_parser.Parser()


	def craw(self, root_url, item_url):
		htmlcontent = self.downloader.download(item_url)
		# print('htmlconte : %s' %htmlcontent)
		# self.parser.parse(rootUrl, htmlcontent)
		self.parser.parse(root_url, item_url, htmlcontent)

if __name__ == '__main__':
	rootUrl = 'http://www.dapenti.com/blog/'
	tushuoUrl = 'http://www.dapenti.com/blog/blog.asp?subjectid=70&name=xilei'
	duanziUrl = 'http://www.dapenti.com/blog/blog.asp?subjectid=137&name=xilei'
	caijingUrl = 'http://www.dapenti.com/blog/blog.asp?name=caijing'
	tupianUrl = 'http://www.dapenti.com/blog/blog.asp?name=tupian'
	spider = SpiderMain()
	spider.craw(rootUrl, tushuoUrl)