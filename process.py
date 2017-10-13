

voc = dict()
lis = ([])


def gen_vocabulary(file_name):
    count = 0
    global_c=1
    with open(file_name, 'rt') as f:
        data = f.read()
        for word in data.split(' '):
            count+=1
            if word not in voc:
                word_id = len(voc)+1
                voc[word] = word_id
            lis.append([word_id, global_c, count])



def order_triples(triples):
    for triple in triples:
        for element in triple:
            print(element)
        
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html)
text = soup.get_text()
print(text)
'''

gen_vocabulary('texto.txt')
print(lis)
order_triples(lis)
