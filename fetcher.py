import urllib.request
from html.parser import HTMLParser





class MyHTMLParser(HTMLParser):
	urls = []
	data = []

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
		self.data.append(data)

	def valid_url(self, url):
		pass




class Fetcher:

	def __init__(self):
		# Thread handle.
		# self.http = urllib3.PoolManager()
		self.unVisitUrl = []
		self.visitUrl = []
		self.parser = MyHTMLParser() 


	def start(self, file):

		try:
			with open(file) as f:
				seeds = f.read()
		except (OSError, IOError) as e:
			print(e)

		f.close()
		# Dispara Threads para coleta distribuida
		self.unVisitUrl.append(seeds.split('\n')[0])

		'''
		for seed in seeds.split('\n'):
			dispara thread get_page(seed)

		'''

		page = self.get_page(self.unVisitUrl.pop(0))
		self.parser.feed(page)


	def get_page(self, url):
		self.visitUrl.append(url)
		# Coleta web page

		try:
			response = urllib.request.urlopen(url)
		except request.exceptions.Request.Exception as e:
			print(e)

		data = response.read()
		return data.decode('latin-1')



	def robots_resolver(self, url):
		result = {"Allowed":[], "Desallowed": []}

		data = self.get_page(url + "/robots.txt")

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
		for url in self.visitUrl:
			print(url)

	def print_unvisit_urls(self):
		for url in selfun.VisitUrl:
			print(url)


fetcher = Fetcher()

fetcher.start('seed.txt')

# parser = MyHTMLParser()
# parser.feed('<html> <a href="kaio.com"> </a> </html>')