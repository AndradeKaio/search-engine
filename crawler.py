import urllib3
#from urllib.parse import urlparse
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					print(name, '=', value)



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

r = http.request('GET', 'https://www.google.com')

data = r.data.decode('latin-1')

parser = MyHTMLParser()

parser.feed(data)