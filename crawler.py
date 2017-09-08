# Simple Python Crawler.
# Dependencias
import urllib3
import graph

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


	def __init__(self, seedfile, maxurl):
		# Thread handle.
		self.http = urllib3.PoolManager()
		# Inicializa o parser
		self.parser = MyHTMLParser()
		# Atributos #
		self.seedfile = seedfile
		self.maxurl = maxurl

		self.webGraph = graph.WebGraph()


	def start(self):
		# Abri o arquivo de sementes
		with open(self.seedfile) as file:
			seed = file.read()

		# Inicialmente coleta a primeira url do arquivo
		# E coleta a pagina.
		data = self.get_urls(seed.split('\n')[0])

		# Alimenta o parser com a url coletada
		self.parser.feed(data)

		for i in range(self.maxurl):
			data = self.get_urls(unVisitUrl.pop(0))

	def get_urls(self, url):
		visitUrl.append(url)
		# Request HTML source
		response = self.http.request('GET', url)
		# Decodifica os dados de byte para str
		data = response.data.decode('latin-1')
		return data



	def robots_resolver(self, url):
		result = {"Allowed":[], "Desallowed": []}

		data = self.get_urls(url + "/robots.txt")

		user_agent = False

		for line in data.split('\n'):
			if line.startswith('User-agent'):
				if line.split(': ')[1] == '*':
					user_agent = True
				else:
					user_agent = False
			elif user_agent == True:		
				if line.startswith('Allow'):
					result['Allowed'].append(line.split(': ')[1])
				elif line.startswith('Disallow'):
					result['Desallowed'].append(line.split(': ')[1])


		return result

		


	def print_visit_urls(self):
		for url in visitUrl:
			print(url)

	def print_unvisit_urls(self):
		for url in unVisitUrl:
			print(url)








crawler = Collector("seed.txt", 0)

crawler.start()
# data = crawler.robots_resolver("www.google.com")
# print(data)
crawler.print_visit_urls()
# print('\n')
crawler.print_unvisit_urls()
