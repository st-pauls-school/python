# Password Exercise 5: Full Password Strength Checker
# We now combine all of the previous work into a complete, interactive checker.
# The strength rating is based on how many checks the password passes:
#   0 - 2 checks passed  ->  "weak"
#   3 checks passed      ->  "medium"
#   4 - 5 checks passed  ->  "strong"

# --- Helper functions (from exercise 4) ---

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

# --- Strength function ---

def password_strength(password):
    score = 0
    if is_long_enough(password):
        score += 1
    if has_uppercase(password):
        score += 1
    if has_lowercase(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_special(password):
        score += 1

    if score <= 2:
        return "weak"
    elif score == 3:
        return "medium"
    else:
        return "strong"

# Quick test against several passwords:
test_passwords = ["hi", "password", "Password1", "P@ssw0rd!"]
for p in test_passwords:
    print(p, "->", password_strength(p))

# Interactive version - ask the user for a password and show the rating:
password = input("\nEnter a password to check: ")
rating = password_strength(password)
print("Strength:", rating)


# --- Exercises ---

# 1. Add a "no spaces" check (using a has_no_spaces function) so that a
#    password with spaces can score at most "medium" even if it passes everything else.

# 2. Modify password_strength (or write a new function) so that it also
#    prints feedback explaining what is missing, e.g.:
#       Strength: medium
#       To improve: add a special character, make it longer
#    The feedback should only mention checks that failed.

# 3. Write a main loop that:
#    - asks the user to enter a password
#    - prints the strength and any improvement suggestions
#    - if the password is not "strong", asks them to try again
#    - stops when they enter a strong password (or type "quit" to give up)


# --- Challenge A ---

# Some passwords are technically "strong" by the rules above but are still
# weak because they use well-known words or patterns.
# Add a check against a list of commonly used passwords:
#
#   common = ["password", "123456", "qwerty", "letmein", "dragon",
#             "monkey", "abc123", "iloveyou", "admin", "welcome"]
#
# If the user's password (ignoring case) appears in this list, immediately
# rate it "weak" and tell them why, regardless of the other checks.
# Test with: "Password", "QWERTY", "P@ssw0rd!", "correcthorsebattery"


# --- Challenge B: complete checker ---

# Add your crack_time function from exercise 4 and call it inside the main loop
# so that each time the user enters a password they see:
#   - the strength rating
#   - any improvement suggestions
#   - the estimated time to brute force it
#
# This is the finished tool — all five exercises combined into one program.
