import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def strip(x):
	last = x[-1]
	num = x[0:-1]
	if not(last.isnumeric())  and num.isnumeric():
		return int(num), last

def highest_common(n, d): 
	if d < n: 
		return highest_common(d, n)
	if d == 1 or d == n:
		return 1
	if d %n == 0: 
		return n 
	return highest_common(d % n, n)

def mixed(n, d, simplify, variable=''): 
	negative = n*d < 0 

	n = abs(n) 

	whole = n // d
	numerator = n % d  

	if simplify:
		hcf = highest_common(n, d)
		numerator, d = numerator // hcf, d // hcf

	fraction = "{0}/{1}".format(numerator, d)

	return "{0}{1}{2}{3}{4}{5}".format(
			'-' if negative else '', 
			whole if whole > 0 and not (whole == 1 and numerator == 0 and len(variable) > 0) else '', 
			' ' if whole > 0 and numerator > 0 else '', 
			fraction if numerator > 0 else '', 
			' ' if (len(variable) > 0 and numerator > 0) else '', 
			variable if len(variable) > 0 else ''
		) 

def topheavy(n, d, simplify=False):
	if type(n) == int and type(d) == int:
		return mixed(n, d, simplify)
	separated = strip(n)
	if len(separated) == 2:
		return mixed(separated[0], d, simplify, separated[1])
	return

def topheavyS(n,d):
	return topheavy(n,d,True)


test(highest_common(9, 36) == 9)
test(highest_common(9, 37) == 1)
test(highest_common(4, 18) == 2)


test(topheavy(22, 6) == "3 4/6")
test(topheavy(147, 20) == "7 7/20")
test(topheavy(72, 10) == "7 2/10") 
test(topheavy(38, 4) == "9 2/4")
test(topheavy(212, 7) == "30 2/7")
test(topheavy(5, 6) == "5/6")
test(topheavy(12, 3) == "4")
test(topheavy(54, 13) == "4 2/13")
test(topheavy(-25, 7) == "-3 4/7")
test(topheavy("45a", 10) == "4 5/10 a")

test(topheavyS(22, 6) == "3 2/3")
test(topheavyS(147, 20) == "7 7/20")
test(topheavyS(72, 10) == "7 1/5") 
test(topheavyS(38, 4) == "9 1/2")
test(topheavyS("45a", 10) == "4 1/2 a")
test(topheavyS("30a", 10) == "3a")
test(topheavyS("10a", 10) == "a")

