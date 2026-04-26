# Password Exercise 4: Using Functions
# Functions let us package a check into a reusable block with a clear name.
# Each check becomes its own function that returns True or False.
# This makes the code easier to read, test, and build on.

def is_long_enough(password, minimum=8):
    return len(password) >= minimum

def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def has_special(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return True
    return False

# Now we can call each function clearly:
password = "Hello123!"
print("Long enough:", is_long_enough(password))
print("Has uppercase:", has_uppercase(password))
print("Has lowercase:", has_lowercase(password))
print("Has digit:", has_digit(password))
print("Has special:", has_special(password))

# The minimum parameter has a default value of 8 but can be overridden:
print(is_long_enough("hello", 4))    # True  (5 >= 4)
print(is_long_enough("hello", 8))    # False (5 < 8)

# We can store the results in a list and count the passes.
# True counts as 1 and False as 0, so sum() gives us the number of passing checks:
checks = [
    is_long_enough(password),
    has_uppercase(password),
    has_lowercase(password),
    has_digit(password),
    has_special(password),
]
score = sum(checks)
print("Passed", score, "out of", len(checks), "checks")


# --- Exercises ---

# 1. Write a function has_no_spaces(password) that returns True if the
#    password contains no spaces. Test it with "nospace", "has space", "   ".

# 2. Write a function count_digits(password) that returns the number of
#    digit characters. Then write a second function is_digit_rich(password)
#    that returns True if the password contains at least 2 digits.
#    Use count_digits inside is_digit_rich rather than repeating the loop.

# 3. Write a function check_all(password) that calls all five functions at
#    the top of this file and prints a line for each check, e.g.:
#       length    : PASS
#       uppercase : PASS
#       lowercase : FAIL
#       digit     : PASS
#       special   : FAIL
#    Test with "hello", "Hello1", "H3ll0W0rld!"


# --- Challenge A ---

# Write a function suggest_improvements(password) that calls the check
# functions and builds a list of advice strings for any failing checks, e.g.:
#   ["Make it at least 8 characters", "Add an uppercase letter"]
# Return the list (return an empty list if everything passes).
# Then print "Your password is strong!" or print each suggestion on its own line.
# Test with: "hello", "Hello1", "H3ll0W0rld!"


# --- Challenge B: crack_time() ---

# Write a function crack_time(password) that:
#   - Uses has_uppercase, has_lowercase, has_digit, and has_special to build a charset size
#     (26 per case type, 10 for digits, 20 for specials)
#   - Calculates combinations as charset_size ** len(password)
#   - Divides by 1_000_000_000 to get seconds, then converts to minutes, hours, and days
#   - Prints each value using the :_ format specifier
#
# Because crack_time calls the check functions rather than repeating the loops itself,
# it is short and easy to read. That is the point of building functions.
#
# Test with: "hello", "Hello1", "H3ll0W0rld!", "correct-horse-battery"
# Then call both suggest_improvements and crack_time on the same password
# so a learner can see strength feedback and estimated crack time together.
