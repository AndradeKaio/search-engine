from urllib.request import urlopen
from parse import Parser
from general import *

class Crawler:

    directory = ''
    base_url = ''
    domain_name = ''

    un_visit_file = ''
    visit_file = ''

    un_visit = set()
    visit = set()
    
    def __init__(self, directory, base_url, domain_name):
        Crawler.directory = directory
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name

        Crawler.un_visit_file = Crawler.directory+'/naovisitados.txt'
        Crawler.visit_file = Crawler.directory +'/visitados.txt'
        self.start()
        self.crawl_page('Main Thread.', Crawler.base_url)

    @staticmethod
    def start():
        # Cria uma pasta para o dominio em questao.
        create_dir(Crawler.directory)
        # Cria os arquivos de visitados e nao visitados para este dominio
        create_files(Crawler.directory, Crawler.base_url)
        # Carrega as urls para memoria
        Crawler.un_visit = file_to_set(Crawler.un_visit_file)
        Crawler.visit = file_to_set(Crawler.visit_file)

    @staticmethod
    def crawl_page(thread_name, page_url):

        if page_url not in Crawler.visit:
            #print(thread_name + 'crawling' + page_url)
            #print('Links visitados' + str(len(Crawler.visit)))
            #print('Link nao visitados' + str(len(Crawler.un_visit)))

            #obtem os links da pagina em questao
            links  = Crawler.get_links(page_url)
            # atualiza a lista de nao visitados com os links obtidos
            Crawler.update_un_visit(links)
            # remove o link visitado
            Crawler.un_visit.remove(page_url)
            #adciona na lista de visitados os link visitado
            Crawler.visit.add(page_url)
            #atualiza os arquivos de visitados e nao visitados
            Crawler.update_files()

    @staticmethod
    def get_links(page_url):
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                data = response.read().decode('latin-1')

            parser = Parser(Crawler.base_url, page_url)
            parser.feed(data)
        except:
            print("Erro ao conectar a pagina " + page_url)
            return set()
        return parser.page_links()
            

    @staticmethod
    def update_un_visit(links):
        for link in links:
            if link in Crawler.visit or link in Crawler.un_visit:
                continue
            if Crawler.domain_name not in link:
                continue
            Crawler.un_visit.add(link)

    @staticmethod
    def update_files():
        set_to_file(Crawler.visit, Crawler.visit_file)
        set_to_file(Crawler.un_visit, Crawler.un_visit_file)
        



           
