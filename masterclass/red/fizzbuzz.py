target = 100 # int(input("How high? "))

for i in range(1, target+1):
	output = ""
	if i % 3 == 0: 
		output += "Fizz"
	if i % 5 == 0: 
		output += "Buzz"
	if i % 7 == 0: 
		output += "Bang"
	if output == "":
		output = str(i)
	print(output)
