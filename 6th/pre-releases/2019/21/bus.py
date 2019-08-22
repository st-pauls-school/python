# a function to return just the days of the week in a list 
def days(): return ["Mon", "Tue", "Wed", "Thu", "Fri"]

### USER INPUT SECTION for Task 1

# Validate the user's input 
def validate(value):
    if not value.isnumeric() and value[1:].isnumeric() and value[0] != '-':
        return False
    i = int(value)
    return -20 <= i <= 20

# take in an input (using the given prompt) and loop until it validates
def input_and_validate(prompt):    
    while True:
        candidate = input(prompt)
        if validate(candidate):            
            return int(candidate)
        print("Invalid value - please try again.") 

# Given a bus label (e.g. "Bus A") take in a number of weeks' worth of data 
def input_bus(busLabel, weeks):
    returnValues = []    
    for i in range(weeks*5):
        # the {} are replaced in the string by the arguments in the format brackets, in the order used 
        p = "Bus {}, {}{} ".format(busLabel, days()[i%5], (i//5)+1)
        val = input_and_validate(p)
        returnValues.append(val)
    return returnValues

# Given a list of bus names, call the individual bus function 
def input_busses(busLabels, numWeeks):    
    busLists = []
    for bl in busLabels:
        busLists.append(input_bus(bl, numWeeks))
    return busLists

# take in a number of bus labels - the inputs are not validated - until just enter is clicked 
def input_bus_labels():
    labels = []
    while True:
        label = input("What is the next bus name? (Leave blank to exit) ")
        if label == "":
            return labels
        labels.append(label)

# select to use manual input 
def user_input(numWeeks):
    labels = input_bus_labels()
    lists = input_busses(labels, numWeeks)
    return labels, lists

### the test data supplied in the pre-release. 

def supplied():
    labels = ["Bus A", "Bus B", "Bus C", "Bus D", "Bus E", "Bus F"]
    lists = [
        [ 0, 0, 0, 2, 2,  4, 0, 3,4,-2,-5, 0, 0, 3,4,-1, 8, 1, 1,-2],
        [ 0, 1, 0, 0, 1,  2, 0, 0,0, 0, 1, 0, 0, 0,2, 0, 0, 1, 0, 0],
        [ 2, 0,-1,-1,-2, -2,-3,-1,0, 0,-2, 0, 1, 1,1, 1,-1,-1, 2,-2],
        [ 1, 0, 0, 0, 0,  0, 0, 0,0, 0, 2, 0, 0, 0,0, 0, 0, 0, 0, 0],
        [-1,-1,-1,-2,-4,-10,-2, 0,0, 0, 0, 1, 2,-3,1, 1, 3,-1, 0, 0],
        [ 0,-5,-5,-5,-4, -3,-5, 0,0, 0, 0,-2,-3, 1,1, 1, 0, 0,-2,-5]
        ]
    return labels, lists

## Choose between the user inputed data or the supplied test data
def task1(prompted, numWeeks=4):
    if prompted:
        return user_input(numWeeks)
    else:
        return supplied()

# for a given bus list, return a tuple with the number of lates, the total amount of lateness
# and the total of just the lates 
def late_arrivals(data):
    count = 0
    tot = 0
    tot_exclusive = 0 
    for i in data:
        if i < 0:
            count+=1
            tot_exclusive += i 
        tot += i
        
    return count, tot, tot_exclusive

# format the output nicely. 
def header(msg):
    print('\n{}\n{}'.format(msg, '-'*len(msg)))

# take the bus list and the lateness data and output the answers to task 2
def task2(busses, data):
    header("Task 2")
    latest = ""
    mostLates = 0
    # loop over the list of bus 
    for i in range(len(busses)):
        # get the late arrival summaries 
        cLate, totalLate, totalOnlyLate = late_arrivals(data[i])

        # calculate the average lateness per bus (using the number of data items for the bus) 
        avgLate = round(totalLate/len(data[i]), 2)

        # print out the summary, the {n} bracket prints the nth item in the format brackets         
        print('{0}:\n\tlate {1} times,\n\tavg. {2} {3} minutes, \n\tavg. when late {4} minutes'
              .format(busses[i],
                      cLate, 
                      "late" if avgLate < 0 else "early",
                      avgLate * (-1 if avgLate < 0 else 1),
                      -round((totalOnlyLate/cLate) if cLate > 0 else cLate, 2)))

        # does the current bus equal the most lates 
        if cLate == mostLates:
            latest += ", " + busses[i]

        # does the current bus have the most lates 
        if cLate > mostLates:
            mostLates = cLate
            latest = busses[i]
    print('Worst performing route(s): {}'.format(latest))

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

#### RUN THE CODE


# False for the supplied data, True to ask the user to input their own 
busses, data = task1(False)
task2(busses, data)
task3(busses, data)
          
    
