import urllib.request


class Fetcher:

	def __init__(self):
		# Thread handle.
		# self.http = urllib3.PoolManager()
		self.unVisitUrl = []
		self.visitUrl = []

	def start(self, file):
		with open(file) as f:
			seeds = f.read()
		f.close()
		# Dispara Threads para coleta distribuida
		self.unVisitUrl.append(seeds.split('\n')[0])

		'''
		for seed in seeds.split('\n'):
			dispara thread get_page(seed)

		'''

		page = self.get_page(self.unVisitUrl.pop(0))


	def get_page(self, url):
		self.visitUrl.append(url)
		# Coleta web page
		response = urllib.request.urlopen(url)
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


fetcher = Fetcher()

fetcher.start('seed.txt')

# parser = MyHTMLParser()
# parser.feed('<html> <a href="kaio.com"> </a> </html>')