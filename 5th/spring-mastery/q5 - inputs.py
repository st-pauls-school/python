from test import test 

def wrapper():
	inputs = []
	i = int(input("next: "))
	while i >= 0:
		inputs.append(i)
		i = int(input("next: "))
	return inputs

def summarise(l):
	return min(l), max(l), sum(l)/len(l)

def print_out(m1, m2, mean):
	print("minimum: {0}, maximum: {1}, mean: {2}".format(m1, m2, mean))

test(summarise([2,4,6,8,10]) == (2, 10, 6))

a,b,c = summarise([2,4,6,8,10])
print_out(a,b,c)