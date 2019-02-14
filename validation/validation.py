def prompt(lower = 0, upper = 100):
	while True:
		i = input('Please input a number between {0} and {1}: '.format(lower, upper))
		dots = 0
		digits = 0 
		hyphens = 0 
		for c in i:
			if c == '.':
				dots += 1
			if c.isnumeric(): 
				digits += 1
			if c == '-':
				hyphens += 1 
		if dots <= 1 and hyphens <= 1 and digits + dots + hyphens == len(i):

			if dots == 1: 
				val = float(i)
			else: 
				val = int(i)

			if lower <= val <= upper: 
				return val 
			else: 
				print("That number was out of range.", end = " ")
		else: 
			print("That wasn't a number.", end = " ")

		print("Try again")

# prompt()


def subjects(l):
	for i in range(len(l)): 
		l[i] = l[i].lower()
	i = input("Which subject? ")
	if i.lower() not in l:
		print("not recognised")
	else:
		print("that's in there")

# subjects(["maths", "computing", "biology"])

def postcodes(pc):
	# check the length
	if len(pc) >= 6 and len(pc) <= 8:
		# check that it begins with a letter 
		if pc[0].isalpha():
			# now check that it ends with a space, followed by a number, followed by two letters 
			if pc[-1].isalpha() and pc[-2].isalpha() and pc[-3].isdigit() and pc[-4] == ' ':
				# either the second character is a number
				if pc[1].isdigit():
					# in which case the third character can be a number, letter or a space 
					return pc[2].isdigit() or pc[2].isalpha() or pc[2] ==' '
				# or the second character is a digit, in which case the third character MUST be a number
				if pc[1].isalpha() and pc[2].isdigit():
					# in which case the fourth character can be a number, letter or a space 
					return pc[3].isdigit() or pc[3].isalpha() or pc[3] ==' '
	return False


print(postcodes("SW13 9JT"))
print(postcodes("S1B 99T"))
print(postcodes("SW1A 1AA"))
print(postcodes("W2 1GB"))
print(postcodes("EC2A 1HQ"))
print(postcodes("W1N 4DJ"))
print(postcodes("W123 4DJ"))


