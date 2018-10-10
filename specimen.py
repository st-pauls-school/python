
def task_1(names, test1scores, test2scores, test3scores):

	valid = [""] * len(names)
	ok1 = [0] * len(names)
	ok2 = [0] * len(names)
	ok3 = [0] * len(names)

	limits = [(test1scores, ok1, 20), (test2scores, ok2, 25), (test3scores, ok3, 35)]

	for i in range(len(names)):
		for s in limits: 
			if s[0][i].isnumeric():
				s[1][i] = int(s[0][i])
				if s[1][i] < 0 or s[1][i] > s[2]: 
					valid[i] = "{0} rejected, {1} is out of range".format(names[i], s[1][i])
			else:
				valid[i] = "{0} rejected, {1} is not a number".format(names[i], s[0][i]) 

	return filter(names, valid), filter(limits[0][1], valid), filter(limits[1][1], valid), filter(limits[2][1], valid)

def filter(source, messages):
	return [source[i] for i in range(len(source)) if len(messages[i]) == 0 ]	

def task_2(names, test1scores, test2scores, test3scores):
	totals = [0] * len(names)

	for i in range(len(names)):
		totals[i] = test1scores[i] + test2scores[i] + test3scores[i]

	return totals, sum(totals)/len(totals)

def task_3(names, totals):
	max_val = max(totals)
	return [names[i] for i in range(len(names)) if totals[i] == max_val], max_val


names = ["A","B","C","D","E","F","G","H","I","J"]
test1n = ["15","12","13","6","8","21","5","-2","fff","17"]
test2n = ["25","24","22","27","-3","12","23","20","-2","dd"]
test3n = ["32","34","23","29","0","5","ee","5","32","12"]
test1ok = ["15","12","13","6","8","19","5","18","18","17"]
test2ok = ["25","24","22","24","3","12","23","20","22","19"]
test3ok = ["32","34","23","29","0","5","31","5","32","12"]

n, s1, s2, s3 = task_1(names, test1n, test2n, test3n)
print(n, s1, s2, s3)
t, a = task_2(n, s1, s2, s3)
print(t, a)
print(task_3(n, t))

n, s1, s2, s3 = task_1(names, test1ok, test2ok, test3ok)
print(n, s1, s2, s3)
t, a = task_2(n, s1, s2, s3)
print(t, a)
print(task_3(n, t))
