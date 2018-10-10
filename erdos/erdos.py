def erdos(filename):
	erdosfile = open(filename, "r")
	scenarios = int(erdosfile.readline())
	results = []
	for i in range(scenarios):
		results.append(construct_scenario(erdosfile))
	erdosfile.close()
	return results 

def construct_scenario(handle):
	numbers = [int(x) for x in handle.readline().split(' ')]
	paper_authors = []
	for p in range(numbers[0]):
		paper = handle.readline()
		names = paper[:paper.find(':')].split(', ') 
		joined = []
		for j in range(0, len(names), 2):
			joined.append('{0}, {1}'.format(names[j], names[j+1]))
		paper_authors.append(joined)
	authors = []
	for a in range(numbers[1]):
		authors.append(handle.readline()[:-1])

	return chains(paper_authors, authors, 'Erdos, P.')

def chains(collaborators, authors, erdosname):
	counts = {erdosname:0}
	for i in range(1, 1+len(collaborators)):
		for cs in collaborators: 
			minimum = len(collaborators)+1 	
			for c in cs:
				if c in counts:
					if counts[c] < minimum: 
						minimum = counts[c]
			for c in cs: 
				if not c in counts:
					counts[c] = minimum+1 
	return [(x, counts[x] if counts[x] <= len(collaborators) else "infinity") for x in authors]

print(erdos("erdos_sample.txt"))

