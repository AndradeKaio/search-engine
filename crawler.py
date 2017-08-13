# Simple Python Crawler.

import urllib3
from html.parser import HTMLParser


unVisitUrl = []
visitUrl = []





class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					# print(name, '=', value)
					unVisitUrl.append(value)



class Collector():


	def __init__(self, initurl, maxurl):
		# Thread handle.
		self.http = urllib3.PoolManager()
		self.parser = MyHTMLParser()
		self.initurl = initurl
		self.maxurl = maxurl


	def start(self):
		response = self.http.request('GET', self.initurl)

		visitUrl.append(self.initurl)

		data = response.data.decode('latin-1')

		self.parser.feed(data)

		for i in range(self.maxurl):
			pass


crawler = Collector("https://www.google.com", 3)

crawler.start()	