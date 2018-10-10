#Write a function timesTable(i) that accepts an integer and prints out the first 12 multiples of that number.
#Extension: format the output nicely, e.g. 1 * 12 = 12 … 12 * 12 = 144 such that all the numbers line up neatly 

def timesTable2(i, m):
	for i in range(i+1):
		print("{:>2} * {:>2} = {:>3}".format(i, m, i*m))

def timesTable(m):
	timesTable2(12, m)
#	for i in range(12+1):
#		print("{:>2} * {:>2} = {:>3}".format(i, m, i*m))

timesTable(5) 

#Write a function timesTable(i, m) that accepts an integer and prints out the first m multiples of that number.
#Extension: re-write your answer to question 1 using this new function 


timesTable2(14, 18) 

#The game FizzBuzz involves counting up from 1, saying the number unless it is divisible by 3 when you should say “Fizz” or it is divisible by 5 when you say “Buzz”.  If divisible by 3 and 5, e.g. 15, say “FizzBuzz”. Write a function fizzBuzz(n) which returns the correct response
#fizzBuzz(2) == “2” 
#fizzBuzz(3) == “Fizz”
#fizzBuzz(5) == “Buzz”
#fizzBuzz(15) == “FizzBuzz”

def FizzBuzz(n):
	for i in range(1,n+1):
		s = ""
		if i%3 == 0:
			s += "Fizz"
		if i%5 == 0:
			s += "Buzz"
		if s == "": 
			print(i)
		else: 
			print(s)

FizzBuzz(30)

#Write a function countdown(n) which counts down from a given integer, as in a rocket launch, finishing with “Blast-off”. (This function is not quiet.) 

def countdown(n):
	for i in range(n, 0, -1):
		print(i)
	print("“Blast-off”")

countdown(10)

#Write a function counter(s, c) which takes a string and a character and returns how many times the character c appears in the string s. 

def counter(phrase, c):
	rv = 0 
	for ch in phrase:
		if ch == c: 
			rv += 1
	return rv
print(counter("hello world", '1') == 3)
print(counter("hello world", '1') == 0)


#Write a function triangular(n) which returns the nth triangular number
def triangular(n):
	return n*(n+1)//2

print(triangular(3) == 6)
print(triangular(12) == 78)

#Write a function Ask(n) to ask the user for n numbers and output the total and the average of the numbers input. (This function is not quiet.) 

