
def linecount():
	handle = open("waroftheworlds.txt", "r")
	count = 0 
	while True:                           
	    nextline = handle.readline()  
	    if len(nextline) == 0:             
	        break                         
	    if len(nextline) > 1:
		    count += 1

	handle.close()
	return count 

print("{0} lines with text on.".format(linecount()))

def noncharacters():
	li = []
	handle = open("waroftheworlds.txt", "r")
	while True:                           
	    nextline = handle.readline()  
	    if len(nextline) == 0:             
	        break                         

	    for c in nextline:
	    	if not c.isalpha() and not c in li:
	    		li.append(c)

	handle.close()
	return li 

print("{0} - unique non-alphabetic characters.".format(noncharacters()))

def wordcount():
	handle = open("waroftheworlds.txt", "r")
	everything = handle.read()
	for ch in noncharacters():
		everything.replace(ch,'')
	words = everything.split()
	
	return len(words)

print("{0} words.".format(wordcount()))

def popularwords(n):
	handle = open("waroftheworlds.txt", "r")
	everything = handle.read()
	for ch in noncharacters():
		everything.replace(ch,'')
	words = [w.lower() for w in everything.split()]
	
	unique = list(set(words))
	counts = [0] * len(unique)
	for i in range(len(words)):
		for j in range(len(unique)):
			if words[i] == unique[j]:
				counts[j] += 1
				break

	sortedcounts = sorted(list(set(counts)), reverse=True)
	
	li = []
	for i in range(n):
		for j in range(len(counts)):
			if counts[j] == sortedcounts[i]:
				li.append((unique[j], counts[j]))

	return li

s = 20
print("{0} are the {1} most popular words.".format(popularwords(s), s))

