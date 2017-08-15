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
					# Para cada URL encontrada que
					# nao esteja na lista de nao visitas, insira em nao visitas
					if value not in unVisitUrl:
						unVisitUrl.append(value)



class Collector():


	def __init__(self, initurl, maxurl):
		# Thread handle.
		self.http = urllib3.PoolManager()
		# Inicializa o parser
		self.parser = MyHTMLParser()
		# Atributos #
		self.initurl = initurl
		self.maxurl = maxurl


	def start(self):
		# Coleta as urls da url inicial
		self.get_urls(self.initurl)

		for i in range(self.maxurl):
			self.get_urls(unVisitUrl.pop(0))

	def get_urls(self, url):
		visitUrl.append(url)
		# Request HTML source
		response = self.http.request('GET', url)
		# Decodifica os dados de byte para str
		data = response.data.decode('latin-1')
		# Invoca o parser
		self.parser.feed(data)


	def print_visit_urls(self):
		for url in visitUrl:
			print(url)

	def print_unvisit_urls(self):
		for url in unVisitUrl:
			print(url)


crawler = Collector("https://www.google.com", 3)

crawler.start()
crawler.print_visit_urls()
print('\n')
crawler.print_unvisit_urls()