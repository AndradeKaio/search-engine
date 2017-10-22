import shelve

class Indexer:

    vocabulary = dict()
    inverted_index = dict()
    '''vocabulary = shelve.open('vocabulary', writeback=True)
    inverted_index = shelve.open('index', writeback=True)'''
    #inverted_index = {int : [ { int : [] } ] }
    document_count = 0
    term_id = 0
    
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
                    Indexer.term_id +=1
                    Indexer.vocabulary[word] = Indexer.term_id
                    Indexer.inverted_index[Indexer.vocabulary[word]] = [ {ii : [index] } ] 
                # Se palavra existe, incrementar a posicao que ela ocupa no mesmo doc
                else:
                    term_id = Indexer.vocabulary[word]
                    # Para cada documento da mesma palavra
                    #print(word)
                    #print(Indexer.inverted_index[word_n])
                    for i in Indexer.inverted_index[term_id]:
                        if ii in i.keys(): 
                            Indexer.inverted_index[term_id].append({ii : [index]})
                        elif index not in i[ii]:
                            i[ii].append(index)

    @staticmethod
    def word_update(word, index):
        Indexer.document_count +=1
        doc_id = Indexer.document_count
        if word in Indexer.vocabulary.keys():
            term_id = Indexer.vocabulary[word]
            for i in Indexer.inverted_index[term_id]:
                if doc_id not in i.keys(): 
                    Indexer.inverted_index[term_id].append({doc_id : [index]})
                elif index not in i[doc_id]:
                    i[doc_id].append(index)
        else:
            Indexer.term_id +=1
            Indexer.vocabulary[word] = Indexer.term_id
            Indexer.inverted_index[Indexer.vocabulary[word]] = [ {doc_id : [index] } ]

    

    @staticmethod
    def print_ii():
        pass
    @staticmethod
    def print_voc():
        for key, value in Indexer.vocabulary.items():
            print(value, ":", key)


    @staticmethod
    def query_docs(text):
        result = list()
        for word in text.split(' '):
            if word not in Indexer.vocabulary.keys():
                return "missing documents"
            else:
                pass
            
#text = "jesus caogipapj eajpgaep prihpajpge aoej oejo hjeao joej hoaojho ej oheoj"


#Indexer.update_index(text)
#Indexer.update_index(text)
#print(Indexer.inverted_index)
#print(Indexer.vocabulary)
#Indexer.print_voc()
