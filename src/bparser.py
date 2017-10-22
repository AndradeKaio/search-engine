from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import urlopen
import re
import unicodedata

class BeautifulParser:

    def __init__(self, web_page):
        self.links = set()
        self.web_page = web_page
        self.soup = BeautifulSoup(web_page, 'html.parser')
        


    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True
    
    def text_from_html(self):
        texts = self.soup.find_all(text=True)
        visible_text = filter(self.tag_visible, texts)
        texts =  u" ".join(t.strip() for t in visible_text)
        texts = unicodedata.normalize('NFKD', texts).lower()
        #texts = re.sub('[^a-zA-Z0-9 \\\]', '', texts)
        texts = re.sub('[^a-zA-Z \\\]', '', texts)
        texts = re.sub(r'\n+', ' ', texts)
        #texts = re.sub(r'\s+', ' ', texts)
        texts = re.sub(' +', ' ', texts)
        return texts

    '''
    def text_from_html(self, web_page):
        soup = BeautifulSoup(web_page, 'html.parser')
        texts = self.soup.find_all(text=True)
        visible_text = filter(self.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_text)
    '''
    def normalize(self, text):
        text = unicodedata.normalize('NFD', text).lower().encode('ASCII', 'ignore')
        return re.sub('[^a-zA-Z0-9 \\\]', '', text)

    def remove_trash(self, text):
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(' +', ' ', text)
        return text

    def get_links(self):
        for link in self.soup.find_all('a', href=True):
            self.links.add(link['href'])

'''
parser = BeautifulParser("<html> \n \n \n \n           </html>")
print(parser.text_from_html())
'''