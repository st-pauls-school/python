# Password Exercise 2: Checking for Character Types
# Passwords are stronger when they contain a mix of character types:
#   uppercase letters  (A-Z)
#   lowercase letters  (a-z)
#   digits             (0-9)
#   special characters (!, @, #, $ ...)

# Python has built-in methods to test a single character:
c = 'A'
print(c.isupper())    # True
print(c.islower())    # False

# The output above just prints True or False, which isn't very descriptive.
# Adding = inside an f-string prints both the expression and its result:
print(f"{c=}")

# and we can do that for function calls too
print(f"{c.isdigit()=}")    # c.isdigit()=False
print(f"{c.isalpha()=}")    # c.isalpha()=True  (any letter, upper or lower)

# To check whether a password contains at least one digit, we loop over it.
# We use a flag variable that starts False and flips to True if we find one.
password = "hello123"
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break          # no need to keep looking once we've found one

if has_digit:
    print("Contains a digit - good!")
else:
    print("No digits found")

# A special character is anything that is neither a letter nor a digit.
# We can check that by combining isalpha() and isdigit() with 'not' and 'and':
password = "hello!23"
has_special = False
for char in password:
    if not char.isalpha() and not char.isdigit():
        has_special = True
        break

print("Has special character:", has_special)

# We can check all four types in a single loop using four flags:
password = "Hello1!"
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

print("Upper:", has_upper, "  Lower:", has_lower,
      "  Digit:", has_digit, "  Special:", has_special)


# --- Exercises ---

# 1. Write code that checks whether a password contains at least one uppercase letter.
#    Print "Has uppercase" or "No uppercase found".
#    Test with: "allowercase", "HasUpper", "ALLCAPS"

# 2. Write code that checks all four character types and prints which are
#    present and which are missing, e.g.:
#       uppercase : present
#       lowercase : MISSING
#       digit     : present
#       special   : MISSING
#    Test with: "Password1!", "password", "P@SSW0RD"

# 3. Spaces in a password are unusual and sometimes not allowed.
#    Write code that checks whether the password contains any spaces.
#    Test with: "nospace", "has space", "   "

# 4. The more character types a password uses, the larger the pool of possible
#    characters an attacker must try for each position:
#       lowercase only              ->  26 characters
#       + uppercase                 ->  52 characters
#       + digits                    ->  62 characters
#       + special characters (~20)  ->  82 characters
#
#    Using the flags from the example above (has_upper, has_lower, has_digit, has_special),
#    write code that builds up a charset_size variable by starting at 0 and adding:
#       26 if has_lower is True
#       26 if has_upper is True
#       10 if has_digit is True
#       20 if has_special is True
#    Then calculate charset_size ** len(password) to get the number of combinations,
#    divide by 1_000_000_000 to get seconds, and convert to minutes, hours, and days
#    using integer division. Print each value using the :_ format specifier.
#    Test with: "hello", "Hello", "Hello1", "Hello1!", "H3ll0W0rld!"
#    What difference does adding each character type make?


# --- Challenge A ---

# Write code that checks all four types AND no spaces, then counts how many
# of the five rules the password passes and prints a score out of 5.
# Test with: "hello", "Hello1", "Hello1!", "Hello 1!", "H3ll0W0rld!"


# --- Challenge B: updated brute force estimate ---

# Extend your answer to exercise 4 into a full brute force estimator.
# For a given password, detect which character types are present, calculate
# the charset size, then print the estimated time to crack it at
# 1_000_000_000 guesses per second in seconds, minutes, hours, and days.
# Use the :_ format specifier for all large numbers.
#
# Run it on the same password at each stage below and note how the estimate changes:
#   "hellothere"    (lowercase only)
#   "HelloThere"    (+ uppercase)
#   "HelloThere1"   (+ digit)
#   "HelloThere1!"  (+ special)
#
# How does adding character types compare to adding length?
# Try "hell0!" (6 chars, 3 types) vs "hellothere" (10 chars, 1 type).
# (This challenge continues in later exercises.)


# --- Challenge C: three-word passwords revisited ---

# In file 1 we checked whether a password used the three-word style (e.g. "correct-horse-battery").
# Now we can think about how the choice of delimiter and structure affects the character types
# present, and therefore the brute force estimate from Challenge B.
#
# Write code that checks which of these three passwords is hardest to brute force,
# by detecting character types, calculating charset size, and estimating crack time:
#
#   "correct-horse-battery"     (three words, hyphen delimiter)
#   "correct!horse!battery"     (three words, special delimiter)
#   "correct-horse-2025"        (two words + a number instead of the third word)
#
# Which has the largest charset size? Which takes longest to crack?
# Does swapping one word for a number help or hurt? Why?
#
# Extension: try replacing the delimiter with a digit instead of a special character:
#   "correct3horse3battery"
# How does that compare to using a special character as the delimiter?
