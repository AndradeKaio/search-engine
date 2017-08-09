import urllib3
from html.parser import HTMLParser



class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					print(name, "=", value)

		print("Start tag: ", tag)

	def handle_endtag(self, tag):
		print("End tag: ", tag)

	def handle_data(self, data):
		print("Data: ", data)



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

r = http.request('GET', 'http://google.com')

print(r.data.decode('utf-8'))

parser = MyHTMLParser()
parser.feed('<html> teste </html>')