from bus_task1 import days 
from bus_task2 import header 

# take in a given day in the correct for,  
def specific_day(inp=''):
    while True:
        if inp[:3] in days() and inp[-1].isnumeric():
            return inp[:3], int(inp[-1])
        inp = input("Which day to analyse, in the form DayX? e.g. Fri3 (Blank to exit) ")

# translate a day of the week and a week number into the index for the bus data array
# e.g. Mon1 => 0, Mon2 => 5, Tues2 => 6
def encode(day, week):
    return (week-1) * 5 + days().index(day)

# given an index (calculated from the day code), look in the data for lateness and then use that
# value to return the bus name 
def lates(idx, busses, data):
    lateBusses = []
    for i in range(len(data)):
        if data[i][idx] < 0:
            lateBusses.append((busses[i], data[i][idx]))
    return lateBusses

# Task 3 - take the bus names and lateness data, if the day code has been given use it, otherwise
# ask the user 
def task3(busses, data, day_code=""):
    header("Task 3")
    day, week = specific_day(day_code)
    idx = encode(day, week)
    l = lates(idx, busses, data)
    print("On {}{} there were {} lates".format(day, week, len(l)))
    if len(l) > 0:
        for p in l:
            print('{}: {} mins late'.format(p[0], -p[1]))
        print()
