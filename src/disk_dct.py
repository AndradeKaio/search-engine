import shelve
import os
from nltk.corpus import stopwords

class Indexer:

    #inverted_index = {int : [ { int : [] } ] }


    VOCABULARY = 'vocabulary'
    INVERTED_INDEX = 'index'
    
    
    vocabulary = shelve.open(VOCABULARY, writeback=True)
    inverted_index = shelve.open(INVERTED_INDEX, writeback=True)

    document_count = 0
    term_id = 0

    indexed_words = 0

    stopwords_pt = stopwords.words('portuguese')
    stopwords_en = stopwords.words('english')

    def __init__(self):
        pass


    @staticmethod
    def init_new_indexer():
        try:
            os.remove(Indexer.INVERTED_INDEX)
            os.remove(Indexer.VOCABULARY)
        except IOError:
            print("voc or index not found")



    @staticmethod
    def update_voc(text):
        for word in str(text).split(' '):
            if word not in Indexer.vocabulary:
                doc_id = len(Indexer.vocabulary) + 1
                Indexer.vocabulary[word] = doc_id

    @staticmethod
    def update_index(text):
        Indexer.document_count += 1
        doc_id = Indexer.document_count
        if type(text) is str:
            # Para cada palavra no texto recebido
            for index, word in enumerate(text.split(' ')):
                
                # Se a palavra nao existe no indice, cria nov entrada para ela
                if len(word) > 1 and word not in Indexer.vocabulary.keys():
                #if word not in Indexer.inverted_index.keys():
                    Indexer.term_id += 1
                    Indexer.vocabulary[word] = Indexer.term_id
                    
                    Indexer.inverted_index[str(Indexer.vocabulary[word])] = [ {doc_id : [index] } ] 
                # Se palavra existe, incrementar a posicao que ela ocupa no mesmo doc
                else:
                    term_id = Indexer.vocabulary[word]
                    # Para cada documento da mesma palavra
                    # print(word)
                    # print(Indexer.inverted_index[word_n])
                    for i, j in enumerate(Indexer.inverted_index[str(term_id)]):
                        if doc_id in j.keys():
                            x = Indexer.inverted_index[str(term_id)][i][doc_id][-1]
                            Indexer.inverted_index[str(term_id)][i][doc_id].append(index-x)
                            find = True
                            k = j
                            break;
                    
                    if find is False:
                        Indexer.inverted_index[str(term_id)].append({doc_id : [index]})
                    find = False
        Indexer.inverted_index.sync()




    @staticmethod
    def word_update(word, index):
        doc_id = Indexer.document_count
        find = False
        x = 0
        if word in Indexer.vocabulary.keys() and word not in Indexer.stopwords_pt and word not in Indexer.stopwords_en:
            term_id = Indexer.vocabulary[word]
            for i, j in enumerate(Indexer.inverted_index[str(term_id)]):
                if doc_id in j.keys():
                    l = Indexer.inverted_index[str(term_id)][i][doc_id]
                    if len(l) > 1:
                        Indexer.inverted_index[str(term_id)][i][doc_id].append(index-l[0])
                        Indexer.inverted_index[str(term_id)][i][doc_id][0] = index

                    elif len(l) == 1:
                        Indexer.inverted_index[str(term_id)][i][doc_id].append(l[0])
                        Indexer.inverted_index[str(term_id)][i][doc_id][0] = index
                        Indexer.inverted_index[str(term_id)][i][doc_id].append(index - l[-1])                            
                    
                    find = True
                    break;
            del(l)
            if find is False:
                Indexer.inverted_index[str(term_id)].append({doc_id : [index]})
            find = False
        else:
            Indexer.term_id +=1
            Indexer.vocabulary[word] = Indexer.term_id
            Indexer.inverted_index[str(Indexer.vocabulary[word])] = [ {doc_id : [index] } ]

        Indexer.indexed_words+=1
        if Indexer.indexed_words > 10000:
            #print("sync.")
            Indexer.indexed_words = 0
            Indexer.inverted_index.sync()
            Indexer.vocabulary.sync()


    # Print the vocabulary
    @staticmethod
    def print_voc():
        for key, value in Indexer.vocabulary.items():
            print(value, ":", key)

    # Return the vocabulary size
    @staticmethod
    def voc_size():
        return len(Indexer.vocabulary)
    # Return the index size
    @staticmethod
    def index_size():
        return len(Indexer.inverted_index)
    # Print the inverted index
    @staticmethod
    def print_ii():
        for key, value in Indexer.inverted_index.items():
            print(key, " - ", value)


    @staticmethod
    def query_docs(text):
        result = list()
        for word in text.split(' '):
            if word not in Indexer.vocabulary.keys():
                return "missing documents"
            else:
                pass
'''
doc1 = "jesus caogipapj eajpgaep prihpajpge aoej oejo hjeao joej hoaojho ej oheoj"
doc2 = "o joao foi comprar pao na casa do pedro jesus a lalbal  joej alalalabdub jejejejejejj"
#Indexer.update_index(text)
#Indexer.update_index(text)

with open("teste", 'rt') as f:
    data = f.read()
    f.close()

for index, word in enumerate(data.split(' ')):
    if word not in Indexer.stopwords_pt:
        Indexer.word_update(word, index)


Indexer.print_ii()
#Indexer.print_voc()

corpus = [doc1, doc2]
for doc in corpus:
    Indexer.document_count += 1
    for index, word in enumerate(doc.split(' ')):
        Indexer.word_update(word, index)

Indexer.print_ii()
Indexer.print_voc()
Indexer.inverted_index.close()
#print(Indexer.inverted_index)
#print(Indexer.vocabulary)
#Indexer.print_voc()
#Indexer.print_ii()
Indexer.inverted_index.sync()
Indexer.vocabulary.sync()
Indexer.inverted_index.close()
Indexer.vocabulary.close()
'''
