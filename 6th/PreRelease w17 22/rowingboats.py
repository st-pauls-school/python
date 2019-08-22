import sys 

# a boats hire details are stored as a list of tuples - (start time, duration)

# store the strings so that they can be compared more easily in the tests. 
successful_hire = "hire successful"
already_out = "boat is already hired at that time"
outside_of_hours = "outside of opening hours"
invalid_input = "invalid time/duration"
none_available = "no boats available"

# a check to see if a string is an integer
def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# validates that a string is in the correct time formet 
def validate_time(t):
	bits = t.split(":")
	if len(bits) == 2 and IsInt(bits[0]) and IsInt(bits[1]):
		return True, int(bits[0]), int(bits[1])
	else:
		return False, 0, 0

# returns the number of minutes represented by a given string, defaults to 0 
def validate_duration(d):
	if d == "half":
		return 30
	if d == "whole":
		return 60
	return 0

def input_time():
	return input("input current time (hh:mm): ")

def input_duration():
	return input("input duration (half, whole): ")

# converts a number of minutes into a time, considered in terms of minutes past midnight  
def time_as_string(mins):
	return '{0:02d}:{1:02d}'.format(mins//60, mins%60)


# take out a specific boat, if the time and duration are not given, prompt the user 
def take_out_boat(boat_information, t = None, d = None):
	if t == None: 
		t = input_time()
	vt = validate_time(t)
	if vt[0]: 
		t = (60*vt[1]) + vt[2]

	if d == None:
		d = input_duration()
	d = validate_duration(d)
	
	# if either the time or the duration are invalid, return an error message
	if not vt[0] or d == 0:
		return invalid_input
	
	# if the start time would be too early or the return time too late, return a suitable message  
	if t < 600 or t + d > 1020: 
		return outside_of_hours

	# if the boat has been hired out, make sure that the start time is not during the period when the last hire was active 
	if len(boat_information) > 0 and boat_information[-1][0] <= t < boat_information[-1][0]+boat_information[-1][1]:
		return already_out

	# append the time and duration to the list 
	boat_information.append((t,d))
	return successful_hire

# for a given boat, loop through the hires, returning the amount of time hired and the total cost 
def ledger(boat, hour = 20, half = 12):
	money = 0
	time = 0
	for i in boat: 		
		if i[1] == 60: 
			money += hour 
			time += 1
		if i[1] == 30:
			money += half
			time += 0.5 
	return money, time

# for a list of boats, iterate through the boats until we can successfully hire one of them, if the time and duration are not supplied, prompt the user. 
def take_a_boat(boats, t = None, d = None):
	if t == None: 
		t = input_time()
	if d == None:
		d = input_duration()
	for i in range(len(boats)):
		res = take_out_boat(boats[i], t, d)
		if res == successful_hire: 
			return "took boat " + str(i)
		if res == invalid_input: 
			return invalid_input
		if res == outside_of_hours:
			return outside_of_hours
	return none_available

# sum up the usage of a boat 
def usage(boat):
	mins = 0
	for h in boat:
		mins += h[1]
	return mins

# sum up the cost of a boat, adding the appropriate costs 
def take(boat):	
	l = 0
	for h in boat:
		l += 20 if h[1] == 60 else 12
	return l

# find the most used boat by time 
def most_used(boats):
	b = -1
	amount = 0
	for i in range(len(boats)):
		mins = usage(boats[i])
		if mins > amount: 
			b = i
			amount = mins 
	return b

# find the boat with the most costs 
def most_lucrative(boats):
	b = -1
	amount = 0
	for i in range(len(boats)):
		l = take(boats[i])
		if l > amount: 
			b = i
			amount = l 
	return b

# define a test function that takes a boolean 
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


# test all the functions 

test(IsInt("123"))
test(not IsInt("a123"))

test(validate_time("10:30") == (True, 10, 30))
test(validate_time("10-30") == (False, 0, 0))
test(validate_duration("whole") == 60)
test(validate_duration("half") == 30)
test(validate_duration("anything") == 0)

test(time_as_string(630) == "10:30")
test(time_as_string(900) == "15:00")

test(ledger([(600,60)]) == (20,1))
test(ledger([(600,30)]) == (12,0.5))
test(ledger([(600,30),(700,30)]) == (24,1))


# test a sample boat with expected results 
boat1 = []
test(take_out_boat(boat1, "9:15", "whole") == outside_of_hours)
test(take_out_boat(boat1, "10:15", "whole") == successful_hire)
test(take_out_boat(boat1, "11:00", "whole") == already_out)
test(take_out_boat(boat1, "11:30", "half") == successful_hire)
test(take_out_boat(boat1, "12:00", "two") == invalid_input)
test(take_out_boat(boat1, "12:00", "whole") == successful_hire)
test(take_out_boat(boat1, "16:00", "whole") == successful_hire)
test(take_out_boat(boat1, "17:01", "whole") == outside_of_hours)
test(boat1 == [(615, 60), (690, 30), (720, 60), (960, 60)])
test(ledger(boat1) == (72,3.5))

boat2 = []
test(take_out_boat(boat2, "10:30", "whole") == successful_hire) 
test(take_out_boat(boat2, "10:50", "half") == already_out) 

# create a list of 10 boats and try to book out a few of them 
boats = [[] for i in range(10)]
test(take_a_boat(boats, "9:15", "whole") == outside_of_hours) 
test(take_a_boat(boats, "10:15", "whole") == "took boat 0") 
test(take_a_boat(boats, "10:30", "whole") == "took boat 1") 
test(take_a_boat(boats, "10:50", "half") == "took boat 2") 
test(take_a_boat(boats, "11:20", "half") == "took boat 0") 
print(boats)

test(usage([(615, 60), (680, 30)]) == 90)
test(take([(615, 60), (680, 30)]) == 32)

# based on the samples used, the boat most used and most income is boat 0 
test(most_used(boats) == 0)
test(most_lucrative(boats) == 0)

