from test import test 

# the idea for this function is to keep on taking the right-most digit from 
# the input number and add it to the left-most bit of the temp value, r, that 
# we've not seen yet (and we get that by left-shifting the current value to 
# make space for it)
def reverse(n):
	r = 0
	while n > 0: 
		r *= 10
		r += n % 10
		n //= 10
	return r



# a palindromic number is a number which is the same backwards as forwards, 
# so let's just create a function to reverse the number and then compare the two 
def palindromic_number(n):
	return list(str(n)) == list(str(n))[::-1]

def partial_palindrome(n, l):
	end = list(str(n))[-l:]
	return end == end[::-1]


test(palindromic_number(1331))
test(not palindromic_number(133))
test(palindromic_number(1))
test(palindromic_number(11))
test(palindromic_number(121))
test(not palindromic_number(1210))
test(not palindromic_number(10))

test(reverse(123) == 321)
test(reverse(1) == 1)
test(reverse(10002) == 20001)
test(reverse(300001) == 100003)

test(partial_palindrome(13443, 4))
test(partial_palindrome(79121, 3))
test(not partial_palindrome(300001, 5))
test(partial_palindrome(300110, 4))


