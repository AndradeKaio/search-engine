import os


def add_file(path, data):
    with open(path, 'a') as file:
        file.write(data+'\n')

def file_to_set(file):
    results = set()
    with open(file, 'rt') as f:
        for line in f.split('\n'):
            results.add(line)
    return results


def set_to_file(links, file):
    # delete file
    for link in sorted(links):
        add_file(file, link)
