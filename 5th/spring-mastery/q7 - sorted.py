from test import test 


def is_sorted(l): 
	if l[0] < l[-1]:
		return going_up(l)
	if l[0] > l[-1]:
		return going_down(l)
	return equals(l)

def going_up(l):
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			return False
	return True

def going_down(l):
	for i in range(len(l)-1):
		if l[i] < l[i+1]:
			return False
	return True

def equals(l):
	for i in range(len(l)-1):
		if l[i] != l[i+1]:
			return False
	return True

test(is_sorted([5,4,3,2,1]))
test(is_sorted([1,3,5,6,9]))
test(not is_sorted([5, 1,3,5,6,9]))
test(not is_sorted([15, 1,3,5,6,9]))
test(not is_sorted([15, 1,3,5,6,9,15]))
test(is_sorted([3, 3, 3, 3, 3]))