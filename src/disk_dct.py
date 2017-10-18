import shelve
import os
class Indexer:

    '''vocabulary = dict()
    inverted_index = dict()'''

    INDEXER_VOCABULARY = 'vocabulary'
    INDEXER_INVERTED_INDEX = 'index'

    vocabulary = shelve.open(INDEXER_VOCABULARY, writeback=True)
    inverted_index = shelve.open(INDEXER_INVERTED_INDEX, writeback=True)

    #inverted_index = {int : [ { int : [] } ] }
    document_count = 0
    

    def __init__(self):
        init_new_indexer()


    @staticmethod
    def init_new_indexer():
        try:
            os.remove(INDEXER_INVERTED_INDEX)
            os.remove(INDEXER_VOCABULARY)
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
        ii = Indexer.document_count
        if type(text) is str:
            # Para cada palavra no texto recebido
            for index, word in enumerate(text.split(' ')):
                # Se a palavra nao existe no indice, cria nov entrada para ela
                if word not in Indexer.vocabulary.keys():
                #if word not in Indexer.inverted_index.keys():
                    doc_id = len(Indexer.vocabulary)+1
                    Indexer.vocabulary[word] = doc_id
                    Indexer.inverted_index[str(Indexer.vocabulary[word])] = [ {ii : [index] } ] 
                # Se palavra existe, incrementar a posicao que ela ocupa no mesmo doc
                else:
                    word_n = Indexer.vocabulary[word]
                    # Para cada documento da mesma palavra
                    # print(word)
                    # print(Indexer.inverted_index[word_n])
                    for i in Indexer.inverted_index[str(word_n)]:
                        if ii not in i.keys(): 
                            Indexer.inverted_index[str(word_n)].append({ii : [index]})
                        elif index not in i[ii]:
                            i[str(ii)].append(index)

    @staticmethod
    def print_ii():
        pass
    @staticmethod
    def print_voc():
        for key, value in Indexer.vocabulary.items():
            print(value, ":", key)

    @staticmethod
    def voc_size():
        return len(Indexer.vocabulary)

    @staticmethod
    def index_size():
        return len(Indexer.inverted_index)

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
            
#text = "jesus caogipapj eajpgaep prihpajpge aoej oejo hjeao joej hoaojho ej oheoj"
#print(Indexer.inverted_index)
#print(Indexer.vocabulary)
#Indexer.print_voc()
#Indexer.print_ii()
Indexer.inverted_index.close()
Indexer.vocabulary.close()

