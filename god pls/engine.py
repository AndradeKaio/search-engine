import threading
from queue import Queue
from crawler import Crawler
from domain_resolver import *
from general import *

PROJECT_NAME = 'google'
HOMEPAGE = 'https://google.com/'
DOMAIN_NAME = get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME +'/naovisitados.txt'
CRAWLED_FILE = PROJECT_NAME+'/visitados.txt'


thread_queue = Queue()

Crawler(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
