# Simple Python Crawler.

import urllib3
from html.parser import HTMLParser


unVisitUrl = []
visitidUrl = []

class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					# print(name, '=', value)
					unVisitUrl.append(value)

# Thread handle.
http = urllib3.PoolManager()

# Get request for the initial page.
r = http.request('GET', 'https://www.google.com')
# Converting html page bytes for str
data = r.data.decode('latin-1')

parser = MyHTMLParser()

parser.feed(data)
