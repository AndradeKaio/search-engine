with open("logs.txt", "rt") as f:
	data = f.read()
	f.close()

with open("hora.txt", "wt") as f:
	for line in data.split('\n'):
		f.write(line.split(' ')[0]+'\n')
	f.close()
with open("url.txt", "wt") as f:
	for line in data.split('\n'):
		f.write(line.split(' ')[1]+'\n')
	f.close()