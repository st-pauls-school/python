# Password Exercise 3: Counting Character Types  (extension)
# In exercise 2 we detected whether each character type was present.
# Here we count how many of each type there are, which allows more precise feedback.

# Counting all four types in one pass using accumulators:
password = "Pass1w2ord3!"
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

for char in password:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print(f"{upper_count=}  {lower_count=}  {digit_count=}  {special_count=}")


# --- Exercises ---

# 1. Write code that counts all four character types in a password and prints
#    a warning for any type that appears only once (easy to guess or drop by accident).
#    Test with: "MyP@ssw0rd!" and "Abc1!"

# 2. Write code that works out what fraction of the password each character type makes up
#    and prints each as a percentage (use integer division).  For example:
#       uppercase:  9%
#       lowercase: 54%
#       digits:    27%
#       special:    9%
#    Test with: "MyP@ssw0rd!" and "Abc1!"


# --- Challenge A: balanced passwords ---

# A password is considered "balanced" if no single character type makes up
# more than half the total characters.
# Write code that checks whether a password is balanced and prints the result.
# Test with: "aaaBBB", "aaaBBB1!", "aaaaaaB1!", "Aa1!"


# --- Challenge B: refined brute force estimate ---

# So far we have assumed an attacker can make 1_000_000_000 guesses per second.
# Is that realistic? It depends on how the password is stored:
#   - A fast hash like MD5 can be cracked at billions of guesses per second on a GPU
#   - A slow hash like bcrypt is deliberately designed to be expensive: perhaps 10_000 per second
#   - An online attack (typing into a login page) might be throttled to 10 per second
#
# Investigate: search for "password cracking speed bcrypt MD5 GPU" and choose a rate
# that you think is realistic. Store it in a variable so it is easy to change:
#
#   guesses_per_second = 1_000_000_000   # fast hash, modern GPU
#
# Then write code that:
#   - Counts each character type
#   - Only adds a type to the charset size if it contributes at least 2 characters
#   - Calculates combinations as charset_size ** len(password)
#   - Divides by guesses_per_second to get seconds, then converts to minutes, hours, days
#   - Prints each value with :_ formatting
#
# Try your code with three different values of guesses_per_second (e.g. 10, 10_000, 1_000_000_000).
# How much difference does the attacker's speed make compared to the password's length?
