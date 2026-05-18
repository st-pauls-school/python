# this library contains functions about manipulating objects that represent dates 
import datetime 

today = datetime.datetime.today()

# create a datetime object from a given year, month date
aday = datetime.datetime(2026, 5, 8)



# use the weekday function 
today_day = today.weekday()
weekday = aday.weekday()

# print the number - Monday is 0 
print(today_day, weekday)

# the timedelta object allows us to add an amount on to a date, months, years, weeks are all valid too 
tomorrow = aday + datetime.timedelta(days=1)

tomorrowday = tomorrow.weekday()
print(tomorrowday)

# writing the date out using a format string, different codes can grab the different aspects of the date - more here: https://www.w3schools.com/python/python_datetime.asp
format = '%A %Y-%m-%d'

# output it nicely 
print(f"if today is {aday:%A %Y-%m-%d}")
print(f"tomorrow will be {tomorrow:%A %Y-%m-%d}")
