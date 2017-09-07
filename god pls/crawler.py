from urllib.request import urlopen
from parse import Parser
from general import *

class Crawler:

    project_name = ''
    base_url = ''
    domain_name = ''

    un_visit_file = ''
    visit_file = ''

    un_visit = set()
    visit = set()
    
    def __init__(self, project_name, base_url, domain_name):
        Crawler.project_name = project_name
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name

        Crawler.un_visit_file = Crawler.project_name+'/quere.txt'
        Crawler.visit_file = Crawler.project_name = '/crawled.txt'
        self.start()
        self.crawl_page('Main Thread.', Crawler.base_url)

    @staticmethod
    def start():
        create_project_dir(Crawler.project_name)
        crate_data_files(Crawler.project_name, Crawler.base_url)
        Crawler.un_visit = file_to_set(Crawler.un_visit_file)
        Crawler.visit = file_to_set(Crawler.visit_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Crawler.visit:
            #print(thread_name + 'crawling' + page_url)
            #print('Links visitados' + str(len(Crawler.visit)))
            #print('Link nao visitados' + str(len(Crawler.un_visit)))
            Crawler.update_visit(Crawler.get_links(page_url))
            Crawler.un_visit.remove(page_url)
            Crawler.visit.add(page_url)
            Crawler.update_files()

    @staticmethod
    def get_links(page_url):
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                data = response.read().decode('latin-1')
            parser = Parser(Crawler.base_url, page_url)
            parser.feed(data)
        except:
            print("Erro ao conectar a pagina")
            return set()
        return parser.page_links()
            

    @staticmethod
    def update_visit(links):
        for link in links:
            if link in Crawler.visit:
                pass
            if link in Crawler.un_visit:
                pass
            if Crawler.domain_name not in link:
                pass
            Crawler.visit.add(link)

    @staticmethod
    def update_files():
        set_to_file(Crawler.visit, Crawler.visit_file)
        set_to_file(Crawler.un_visit, Crawler.un_visit_file)
        



           
