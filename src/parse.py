from html.parser import HTMLParser
from urllib import parse



class Parser(HTMLParser):

    def __init__(self, page_url):
        super().__init__()

        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    #print(name)
                    url = parse.urljoin(self.page_url, value)
                    #print(url)
                    self.links.add(url)



                    
    def page_links(self):
        return self.links
                    
    def error(self, message):
        pass

