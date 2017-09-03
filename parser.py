from html.parser import HTMLParser




class MyHTMLParser(HTMLParser):
	urls = []
	page = None

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					# Para cada URL encontrada que
					# nao esteja na lista de nao visitas, insira em nao visitas
					if value not in self.urls:
						self.urls.append(value)

						

	def handle_endtag(self, tag):
		pass


	def handle_data(self, data):
		print(data.strip("\n"))


	def valid_url(self, url):
		pass

parser = MyHTMLParser()
f = open('doc1.html')
data = f.read()

parser.feed(data)
# print(parser.urls)
