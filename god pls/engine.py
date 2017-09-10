import threading
from queue import Queue
from crawler import Crawler
from domain_resolver import *
from general import *
import sys

PROJECT_NAME = 'corpus'


QUEUE_FILE = PROJECT_NAME +'/naovisitados.txt'
CRAWLED_FILE = PROJECT_NAME+'/visitados.txt'

MAX_THREADS = 4

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
		Crawler.crawl_page(threading.current_thread().name, url)
		thread_queue.task_done()

def start_engine():
	links = file_to_set(QUEUE_FILE)
	for link in links:
		thread_queue.put(link)
	thread_queue.join()



if len(sys.argv) < 2:
	print("Missing seed file.")
else:
	with open(sys.argv[1], 'rt') as f:
		data = f.read()
		f.close()
	for link in data.split("\n"):
		seed.add(link)

	#print(Crawler.un_visit)
	#HOMEPAGE = sorted(list(Crawler.un_visit))[0]
	HOMEPAGE = "https://google.com"
	DOMAIN_NAME = get_domain(HOMEPAGE)

	Crawler(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, seed)
	#create_threads()
	#start_engine()





