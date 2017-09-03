from unicodedata import normalize




index = {str : {str : int}}

def format_file(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII').lower().strip(".")


def processing_file(file):
	try:
		with open(file, 'r') as f:
			data = f.read()
	except Exception as e:
		raise e

	data = format_file(data)
	
	name_file = f.name
	
	for word in data.split(" "):
		if word not in index:
			index[word] = {name_file: 1}
		else:
			index[word][name_file] = index[word][name_file] + 1
	



processing_file("doc1.txt")
print(index)

