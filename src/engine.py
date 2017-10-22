import threading
from queue import Queue
from crawler import Crawler
from domain_resolver import *
from general import *
import sys
import os

PROJECT_NAME = 'corpus'


QUEUE_FILE = PROJECT_NAME +'/naovisitados.txt'
CRAWLED_FILE = PROJECT_NAME+'/visitados.txt'

MAX_THREADS = 8

thread_queue = Queue()
seed = set()

# Cria as Threads 
def create_threads():
	for i in range(MAX_THREADS):
		t = threading.Thread(target=processing)
		t.daemon = True
		t.start()

def processing():
	while True:
		url = thread_queue.get()
		#print(threading.current_thread().name + " crawling the " + url)
		Crawler.crawl_page(threading.current_thread().name, url)
		if thread_queue.qsize() == 0:
			start_engine()
		thread_queue.task_done()

def start_engine():
	links = file_to_set(QUEUE_FILE)
	for link in links:
		thread_queue.put(link)
	thread_queue.join()



if len(sys.argv) < 3:
	print("Error: Missing arguments!")
	print("Please, type engine.py seed.txt new/old")
else:
	if sys.argv[2] is 'new':
		if os.path.exists('corpus'):
			os.remove('corpus')
			os.remove('vocabulary.dat')
			os.remove('vocabulary.dir')
			os.remove('index.bak')
			os.remove('index.dat')
	with open(sys.argv[1], 'rt') as f:
		data = f.read()
		f.close()
	for link in data.split("\n"):
		seed.add(link)

	Crawler(PROJECT_NAME, seed)
	create_threads()
	start_engine()






