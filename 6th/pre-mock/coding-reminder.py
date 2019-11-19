import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} successful.".format(linenum)
    else:
        msg = "Test at line {0} failed.".format(linenum)
    print(msg)

def sum_to(li):
	tally = 0 
	for item in li: 
		tally += item
	return tally 

test(sum_to([1,2,3,4,6]) == 16)

def find_hypot(a,b):
	return (a**2 + b**2)**0.5

test(find_hypot(12,5)==13)

def is_rightangled(a,b,c):
	return find_hypot(a,b)==c or find_hypot(a,c)==b or find_hypot(b,c)==a

test(is_rightangled(12,5,13))
test(is_rightangled(5,4,3))
test(not is_rightangled(5,5,3))

def how_many_rightangled(l):
	return len([x for x,y,z in l if is_rightangled(x,y,z)])

test(how_many_rightangled([(1,3,2),(3,4,5),(12,13,5), (5,4,6)]) == 2)

def to_secs(h,m,s):
	return (((h*60)+m)*60)+s

test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)

def since_2000(s):
	def day_calc():
		return 24 * 60 * 60

	def year_calc(y):
		return (365 + (1 if y % 4 == 0 else 0)) * day_calc()

	def month_calc(m, y):
		f = 29 if y%4 == 0 else 28
		return [31,f,31,30,31,30,31,31,30,31,30,31][m] * day_calc()

	y = 2000 
	while s > year_calc(y):
		s -= year_calc(y)
		y +=1 

	m = 0
	while s > month_calc(m,y):
		s-= month_calc(m,y)
		m+= 1
	d = (s // day_calc()) + 1
	e = 'th'
	if d in [1,21,31]:
		e = 'st'
	elif d in [2,22]:
		e = 'nd'
	elif d in [3,23]:
		e = 'rd'
	return "{day}{ending} {month}, {year}".format(ending=e,day=d,year=y,month=['January','February','March','April','May','June','July','August','September','October','November','December'][m])

print(since_2000(1000000))
print(since_2000(10000000))
print(since_2000(100000000))

