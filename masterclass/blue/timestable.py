

number = 13 # int(input("Which times table would you like? "))
limit = 13 # int(input("How high? "))

digits = 0
product = number * limit 
while product > 0:
	digits = digits + 1
	product = product // 10 

for i in range(limit+1):
	line = ""
	if(i < 10):
		line += " "
	line += str(i)
	line += " * "
	line += str(number)
	line += " = "
	if i * number < 100: 
		line += " "
	if i * number < 10: 
		line += " "
	line += str(i * number)
	print(line)