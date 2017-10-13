from urllib.request import urlopen
from parse import Parser
from general import *
from robots import *
import threading
from queue import Queue




class Fetcher:

	un_visit = Queue()
	visit = Queue()

	l_unvisit = set()
	l_visit = set()

	count = 1000
	MAX_THREADS = 2

	@staticmethod
	def start(seed_file):

		with open(seed_file, 'rt') as f:
			data = f.read()
			f.close()
		for link in data.split('\n'):
			Fetcher.un_visit.put(link)
			Fetcher.l_unvisit.add(link)

		Fetcher.create_threads()


	def processing():
		while True:
			url = Fetcher.un_visit.get()
			Fetcher.get_link(url)
			Fetcher.count-=1
			Fetcher.un_visit.task_done()

		print("TUIS")

	@staticmethod
	def create_threads():
		for i in range(Fetcher.MAX_THREADS):
			t = threading.Thread(target=Fetcher.processing)
			#t.daemon = True
			t.start()


	def update(data):
		for link in data:
			Fetcher.un_visit.put(link)
			Fetcher.l_unvisit.add(link)

	def get_link(url):
		if url not in Fetcher.l_visit:
			Fetcher.visit.put(url)
			Fetcher.l_visit.add(url)
			Fetcher.l_unvisit.remove(url)

			try:
				response = urlopen(url)
				if 'text/html' in response.getheader('Content-Type'):
					data = response.read().decode('latin-1')
				parser = Parser(url)
				parser.feed(data)
				data = parser.page_links()
				update(data)
			except:
				print("oi")
a = Fetcher()
a.start("seeds.txt")