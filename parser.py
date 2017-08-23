from html.parser import HTMLParser




class MyHTMLParser(HTMLParser):
	urls = []

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


	def valid_url(self, url):
		pass

parser = MyHTMLParser()
parser.feed('<html> <a href="kaio.com"> </a> </html>')
print(parser.urls)
