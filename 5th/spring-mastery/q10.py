from test import test 

def digitsum(n):
	ds = 0 
	while n > 0: 
		ds += n % 10
		n //= 10
	return ds

def valid(num, exp):
	return digitsum(num**exp) == num


test(digitsum(123) == 6)
test(digitsum(103) == 4)
test(digitsum(1) == 1)
test(digitsum(999) == 27)

test(not valid(9,3))
test(valid(9,2))
test(not valid(8,2))
test(valid(8,3))
test(valid(7,4))
test(not valid(7,2))


def go(n):
	c = 0
	num = 2 
	while True:
		for ee in range(2, 100):
			if valid(num, ee):
				c += 1
				print("{3}: {0}^{1} = {2}".format(num, ee, num**ee,c))
				if c == n:
					return
		num += 1

go(250)