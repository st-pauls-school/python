# Password Topic 1: Length Checking
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

