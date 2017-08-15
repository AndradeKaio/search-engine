# Simple Python Crawler.
# Dependencias
import urllib3
from html.parser import HTMLParser


# List
unVisitUrl = []
visitUrl = []





class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					if value not in unVisitUrl:
						unVisitUrl.append(value)



class Collector():


	def __init__(self, initurl, maxurl):
		# Thread handle.
		self.http = urllib3.PoolManager()
		self.parser = MyHTMLParser()
		self.initurl = initurl
		self.maxurl = maxurl


	def start(self):
		self.get_url(self.initurl)
		for i in range(self.maxurl):
			self.get_url(unVisitUrl.pop(0))

	def get_url(self, url):
		response = self.http.request('GET', url)
		visitUrl.append(url)
		data = response.data.decode('latin-1')
		self.parser.feed(data)


	def print_visit_urls(self):
		for url in visitUrl:
			print(url)

	def print_unvisit_urls(self):
		for url in unVisitUrl:
			print(url)


crawler = Collector("https://www.google.com", 3)

crawler.start()