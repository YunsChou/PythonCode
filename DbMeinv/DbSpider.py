
import DbUrlManager, DbDownloader, DbParser, DbOutputer
import time

class SpiderMain(object):
	
	def __init__(self):
		self.urlManager = DbUrlManager.UrlManager()
		self.downloader = DbDownloader.Downloader()
		self.parser = DbParser.Parser()
		self.outputer = DbOutputer.Outputer()

	def craw(self, root_url):
		self.urlManager.add_new_url(root_url)
		count = 1
		try:
			while self.urlManager.has_new_url():
				new_url = self.urlManager.get_new_url()
				html = self.downloader.download(new_url)
				parse_url, parse_data = self.parser.parse(new_url ,html)
				self.outputer.collect_data(parse_data)
				self.urlManager.add_new_url(parse_url)
				time.sleep(2)
				count += 1
				if count > 2:
					break
		except Exception as e:
			print('e : %s' %e)
			raise e
		self.outputer.output()

if __name__ == '__main__':
	root_url = 'http://www.dbmeinv.com/?pager_offset=1'
	spider = SpiderMain()
	spider.craw(root_url)