from test import test 

def is_power(a, b):
	if a == 1: 
		return True
	if a < 1: 
		return False
	return is_power(a/b, b)

test(is_power(32,2))
test(not is_power(33,2))