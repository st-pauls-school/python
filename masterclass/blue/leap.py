year = int(input("Your year? "))
if year % 4 != 0:
    print("not a leap year")
elif year % 100 == 0 and year % 400 != 0:
    print("not a leap year")
else:
    print("It is a leap year")
    

    