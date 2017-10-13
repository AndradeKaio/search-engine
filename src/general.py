import os




def create_files(directory_name, base_url):
    un_visited = os.path.join(directory_name, 'naovisitados.txt')
    visit = os.path.join(directory_name, 'visitados.txt')
    if not os.path.isfile(un_visited):
        write_file(un_visited, base_url)
    if not os.path.isfile(visit):
        write_file(visit, '')

def create_corpus(directory_name, seeds):
    un_visited = os.path.join(directory_name, 'naovisitados.txt')
    visit = os.path.join(directory_name, 'visitados.txt')
    if not os.path.isfile(un_visited):
        with open(un_visited, "wt") as f:
            for seed in seeds:
                f.write(seed+"\n")
            f.close()
    if not os.path.isfile(visit):
        write_file(visit, '')




def create_dir(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except Exception as e:
        print("Erro ao criar arquivo")

def add_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data+'\n')
        file.close()

def file_to_set(file):
    results = set()
    with open(file, 'rt') as f:
        data = f.read()
        for line in data.split('\n'):
            results.add(line)
    return results


def set_to_file(links, file):
    # delete file
    with open(file, "wt") as f:
        for link in links:
            f.write(link + "\n")

def write_file(path, file_data):
    with open(path, 'w') as f:
        f.write(file_data)
        f.close()


def read_seed(file_name):

    with open(file_name, 'rt') as f:
        data = f.read()
        f.close()
    return data