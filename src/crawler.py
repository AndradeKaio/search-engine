from urllib.request import urlopen
from time import ctime
from bparser import *
from general import *
from robots import *
from bs4 import BeautifulSoup


class Crawler:

    directory = ''
    base_url = ''

    un_visit_file = ''
    visit_file = ''

    discovered_urls = 0
    crawled_urls = 0

    store = 500

    seed_file = list()
    un_visit = set()
    visit = set()
    
    def __init__(self, directory, seed_file):
        Crawler.directory = directory
        Crawler.base_url = seed_file.pop()
        Crawler.seed_file = seed_file
        Crawler.un_visit_file = Crawler.directory+'/naovisitados.txt'
        Crawler.visit_file = Crawler.directory +'/visitados.txt'

        for seed in seed_file:
            Crawler.un_visit.add(seed)

        self.start()
        self.crawl_page('Main Thread.', Crawler.base_url)

    @staticmethod
    def start():
        # Cria uma pasta para o dominio em questao.
        create_dir(Crawler.directory)
        # Cria os arquivos de visitados e nao visitados para este dominio
        #create_files(Crawler.directory, Crawler.base_url)
        create_corpus(Crawler.directory, Crawler.seed_file)
        # Carrega as urls para memoria
        Crawler.un_visit = file_to_set(Crawler.un_visit_file)
        Crawler.visit = file_to_set(Crawler.visit_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Crawler.visit:
            if robot_check(page_url):
                #print(thread_name + 'crawling' + page_url)
                #print('Links visitados' + str(len(Crawler.visit)))
                #print('Link nao visitados' + str(len(Crawler.un_visit)))

                #obtem os links da pagina em questao
                links  = Crawler.get_links(page_url)
                Crawler.crawled_urls +=1
                Crawler.discovered_urls+=len(links)
                #print(ctime(), " ", Crawler.discovered_urls)
                # atualiza a lista de nao visitados com os links obtidos
                Crawler.update_un_visit(links)
                # remove o link visitado
                #adciona na lista de visitados os link visitado
                Crawler.visit.add(page_url)

            Crawler.un_visit.remove(page_url)
            #atualiza os arquivos de visitados e nao visitados
            Crawler.update_files()

    # obtem os links da @page_url atraves do parse.
    @staticmethod
    def get_links(page_url):
        try:
            #requisicao http
            response = urlopen(page_url)
            #descarta qualquer arquivo diferente de html
            if 'text/html' in response.getheader('Content-Type'):
                data = response.read().decode('latin-1')
            #invoca o parser 
                
            parser = BeautifulParser(data)
            parser.get_links()

            #parser = Parser(page_url)
            #parser.feed(data)
        except:
            print("Erro ao conectar a pagina " + page_url)
            return set()
        return parser.links
            
    # Metodo usado sempre que urls sao coletadas.
    # Atualiza o conjunto de URLS ainda nao visitadas.
    @staticmethod
    def update_un_visit(links):
        for link in links:
            if link in Crawler.visit or link in Crawler.un_visit:
                continue
            '''if Crawler.domain_name not in link:
                continue'''
            if link.startswith("http") is False:
                continue
            Crawler.un_visit.add(link)

    # Atualiza os arquivos de visitados e nao visitados
    @staticmethod
    def update_files():
        set_to_file(Crawler.visit, Crawler.visit_file)
        set_to_file(Crawler.un_visit, Crawler.un_visit_file)

'''
p = BeautifulParser()
response = urlopen("http://www.google.com")
p.get_links(response)
print(p.links)
'''