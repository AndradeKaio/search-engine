import urllib




class Fetcher:

	def __init__(self):
		# Thread handle.
		# self.http = urllib3.PoolManager()
		unVisitUrl = []
		visitUrl = []

	def start(self, file):
		with open(file) as f:
			seeds = f.read()

		# Dispara Threads para coleta distribuida
		seed = seeds.split('\n')[0]

		'''
		for seed in seeds.split('\n'):
			dispara thread get_page(seed)

		'''
		unVisitUrl.append(seed)

		page = get_page(seed)


	def get_page(url):
		visitUrl.append(url)
		# Coleta web page
		response = urllib.request.urlopen(url)
		data = response.decode('utf-8')
		return data



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