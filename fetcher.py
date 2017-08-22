import urllib3




class Fetcher:

	def __init__(self):
		# Thread handle.
		self.http = urllib3.PoolManager()

	def start(self, file):
		with open(file) as f:
			seeds = f.read():

		# Dispara Threads para coleta distribuida
		seed = seeds.split('\n')[0]



	def get_page(url):
		# Coleta web page
		page = self.http.request('GET', url)
		# Retorna pagina web decodificada
		return page.decode('latin-1')



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