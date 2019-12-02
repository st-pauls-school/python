# a function to return just the days of the week in a list 
def days(): 
    return ["Mon", "Tue", "Wed", "Thu", "Fri"]

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
