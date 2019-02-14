
from q8 import palindromic_number 
from q8 import partial_palindrome

for i in range(10,1000000):
	if partial_palindrome(i, 4):
		if partial_palindrome(i+1, 5):
			if palindromic_number(((i+2) % 100000)//10): 
				if palindromic_number(i+3):
					for j in range(4):
						print(i+j, end=" ")
					print()

