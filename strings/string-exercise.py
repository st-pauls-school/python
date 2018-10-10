
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def sumOfDigits(s):
	total = 0
	for c in s:
		v = ord(c) - ord('0')
		if 0 < v <= 9:
			total += v
	return total

def listASCII(s):
	rv = []
	for c in s:
		rv.append(ord(c))
	return rv

def distinctList(s):
	l = list(s)
	l.sort()
	letters = []
	previous = ''
	for c in l:
		if c != previous:
			letters.append(c)
		previous = c
	return ''.join(letters)

def countList(s):
	letters = distinctList(s)
	counts = []
	for l in letters:
		counts.append((l, s.count(l)))
	return counts

def listASCIIHex(s):
	rv = []
	for a in listASCII(s): 
		rv.append(hex(a)[2:].upper())
	return rv 

def capitalise(w):
	w = w.lower()
	if ord('a') <= ord(w[0]) <= ord('z'):
		return chr(ord(w[0])+ord('A')-ord('a')) + w[1:]
	return w

def camelcase(s, u):
	l = s.split(' ')
	rv = ""
	i = 0
	if not u:
		rv += l[0].lower()
		i = 1
	for w in l[i:]:
		rv += capitalise(w)
	return rv

def rot13(s):
	return caesar(13, s, False)

def caesar(n, s, sq):
	rv = ""
	for c in s:
		if ord('a') <= ord(c) <= ord('z'):
			rv += chr((ord(c)-ord('a') + n % 26)+ord('a')) 
		elif ord('A') <= ord(c) <= ord('Z'):
			rv += chr((ord(c)-ord('A') + n % 26)+ord('A')) 
		elif not sq: 
			rv += c

	return rv 

def hash(x):
	h = 0
	for c in x:
		val = (h << 5) + (h >> 2) + ord(c)
		h ^= val
	return h

#A function to take a number as a string and return the sum of the digits. 
test(sumOfDigits("12345") == 15) 
test(sumOfDigits("123456")==21)

#For a string, return the list of its ASCII values 
test(listASCII("ABC def") == [65, 66, 67, 32, 100, 101, 102])

# return a distinct list, i.e. any duplicates should be removed 
test(distinctList("ABCABCD") == "ABCD")

#return a distinct list, showing how many of each there were as tuples
test(countList("ABCABCD") == [('A',2),('B',2),('C',2), ('D',1)])

#return the ASCII values in hex, not decimal 
test(listASCIIHex("ABCJ def") == ['41', '42', '43', '4A', '20', '64', '65', '66'])

#Convert a string to CamelCase, where spaces are removed and initial letters are all capitalised, a second parameter indicates whether or not the first letter of the whole string should be capitalised: 
test(camelcase("My String", False) == "myString") 
test(camelcase("upper camel case", True) == "UpperCamelCase") 

#For a given string, implement ROT-13. (Google it.) 
# Your function, rot13(plaintext), should ignore non-alphabetic characters and return the ciphertext 
test(rot13("AbCd EfGh") == "NoPq RsTu") 

test(caesar(1, "abcd", False) == "bcde")
test(caesar(2, "abcd-efgh", False) == "cdef-ghij")
test(caesar(2, "abcd-efgh", True) == "cdefghij")


li = ['hallo', 'hello', 'hullo', 'another', 'an other', 'cheeseboard', 'chessboard']
for w in li: 
	print("'{0}'' hashes to {1}".format(w, hash(w)))