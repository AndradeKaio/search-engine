import os



def create_files(directory_name, base_url):
    un_visited = os.path.join(directory_name, 'naovisitados.txt')
    visit = os.path.join(directory_name, 'visitados.txt')
    if not os.path.isfile(un_visited):
        write_file(un_visited, base_url)
    if not os.path.isfile(visit):
        write_file(visit, '')


def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def create_dir(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except Exception as e:
        print("Erro ao criar arquivo")

def add_file(path, data):
    with open(path, 'a') as file:
        file.write(data+'\n')

def file_to_set(file):
    results = set()
    with open(file, 'rt') as f:
        data = f.read()
        for line in data.split('\n'):
            results.add(line)
    return results


def set_to_file(links, file):
    # delete file
    for link in sorted(links):
        add_file(file, link)

def write_file(path, file_data):
    with open(path, 'w') as f:
        f.write(file_data)