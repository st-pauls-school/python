# Password Exercise 1: Length Checking
# The simplest password rule is minimum length. Most sites require at least 8 characters.

password = "hello"
if len(password) >= 8:
    print("Long enough")
else:
    print("Too short - needs at least 8 characters")

# We can also tell the user exactly how many characters they are short by:
password = "hello"
minimum = 8
if len(password) < minimum:
    shortfall = minimum - len(password)
    print("Password is too short by", shortfall, "characters")
else:
    print("Password length is OK")

# We can give more detailed feedback by using elif:
password = "hello"
if len(password) < 6:
    print("Very weak - far too short")
elif len(password) < 8:
    print("Weak - a bit too short")
elif len(password) <= 16:
    print("OK length")
else:
    print("Good - long password")

# The ** operator raises a number to a power:
print(2 ** 10)    # 1024
print(26 ** 4)    # 456976  (all 4-character lowercase passwords)
print(26 ** 8)    # 208827064576

# Large numbers are hard to read. Writing them with underscores in the code
# makes them clearer - Python ignores the underscores:
guesses = 1_000_000_000
print(guesses)    # 1000000000

# We can also print a number with underscores using the :_ format specifier
# inside an f-string, so the output is just as readable as the code:
combinations = 26 ** 8
print(f"26 ** 8 = {combinations:_}")    # 26 ** 8 = 208_827_064_576


# --- Exercises ---

# 1. Write code that checks if a password is between 8 and 20 characters.
#    Print "too short", "good length", or "too long" as appropriate.
#    Test with: "hi", "correcthorse", "averylongpasswordthatistoolong"

# 2. Write code that prints one of four messages based on length:
#      fewer than 6 characters  -> "very weak"
#      6 or 7 characters        -> "weak"
#      8 to 11 characters       -> "OK"
#      12 or more characters    -> "strong"
#    Test with: "abc", "hello!", "password", "correcthorse"

# 3. Write code that asks the user to enter a password with input() and
#    keeps asking until they enter one that is at least 8 characters long.
#    Each time they fail, tell them how many more characters are needed.


# 4. The count() method returns the number of times a character appears in a string:
#       password = "correct-horse-battery"
#       print(password.count('-'))   # prints 2
#    Write code that counts the hyphens in a password and prints the result.
#    Then write code that prints "likely a word-based password" if there is
#    at least one hyphen, or "no hyphens found" if there are none.
#    Test with: "password", "correct-horse", "correct-horse-battery", "a-b-c-d"


# --- Challenge A: three-word passwords ---

# The NCSC (National Cyber Security Centre) actually recommends using three
# random words joined together as a password (e.g. "correct-horse-battery").
# This can make long passwords that are easier to remember.
# Write code that:
#   - Uses count('-') to check how many hyphens the password contains
#   - Checks whether the password has at least 2 hyphens (i.e. 3 words) AND at least 12 characters
#   - Prints whether the password meets the "three words" rule
# Test with: "horse", "correct-horse", "correct-horse-battery", "a-b-c"


# --- Challenge B: how long to brute force? ---

# A brute force attack tries every possible combination until it finds the password.
# If we assume the password only uses lowercase letters (a-z), there are 26 choices
# for each character, so the total number of combinations is 26 to the power of the length.
# In Python, ** is the power operator:  26 ** 8  gives 208,827,064,576
#
# A modern attacker can make around 1,000,000,000 (one billion) guesses per second.
# We can use integer division (//) to convert a number of seconds into larger units:
#
#   seconds = combinations // guesses_per_second
#   minutes = seconds // 60
#   hours   = minutes // 60
#   days    = hours   // 24
#
# Write code that:
#   - Takes a password length (e.g. 5, 8, 12)
#   - Calculates 26 ** length to get the number of combinations
#   - Divides by 1_000_000_000 to get seconds
#   - Converts seconds to minutes, hours, and days using integer division
#   - Prints each value on its own line, formatted with underscores as thousands separators
#     so large numbers are easy to read, matching how we write them in code.
#     Use an f-string with the :_ format specifier:
#       print(f"Combinations: {combinations:_}")   ->  Combinations: 208_827_064_576
#
# Try lengths 5, 8, 12 and 16. What do you notice about how quickly the number grows?
# (This challenge will be extended in later exercises as we add more character types.)
