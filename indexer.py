from unicodedata import normalize




index = {}

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII').lower().strip(".")


def processing_file(file):
	try:
		with open(file, 'r') as f:
			data = f.read()
			data = remover_acentos(data)
			name_file = f.name
			for word in data.split(" "):
				if word not in index:
					index[word] = name_file
	except Exception as e:
		raise e




processing_file("doc1.txt")

for i in index:
	print(index[i])


