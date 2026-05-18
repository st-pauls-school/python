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

