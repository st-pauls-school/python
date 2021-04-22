import itertools 
import random 
import uuid 

# task 1 
# 5 years groups, y7-y11: 28-35 students per tutor group, 6 tutor groups, e.g. 7A
# each students may only vote for a rep from their tutor group 


# generate all the possible tutor group names, return them in a list 
def tutor_groups():
    # uses lots of list comprehension to make for more concise code
    
    # this first one is equivalent to:
    #   yeargroups = []
    #   for y in range(7,12):
    #     yeargroups.append[str(y)]
    
    # n.b. range(7,12) means start at 7, go up to, but not include 12
    yeargroups = [str(y) for y in range(7,12)]
    # generate the first six numbers, take the ASCII for 'A' and adding
    # 0 to 5 to create 'A' to 'F' 
    tutors = [chr(t + ord('A')) for t in range(6)]
    # using the built-in itertools method to generate all
    # permutations of the two lists as new lists, e.g.
    # [1,2,3] and [10,11] would create
    # [[1,10],[1,11],[2,10],[2,11],[3,10],[3,11]] 
    tgs = list(itertools.product(yeargroups, tutors))
    # iterate through the list combing the first and second items in the lists into single strings 
    return [t[0]+t[1] for t in tgs]

# if user input is expected, loop until a valid (case sensitive) tutor group is received, otherwise return a randomly chosen group 
# uses a default variable, if left empty then user is false 
def input_tutorgroup(user = False):
    tgs = tutor_groups()
    if user: 
        while True:
            tg = input("Name of the tutor group: ")
            if tg in tgs:
                return tg
            print("That's not a valid tutor group. (I am case sensitive.)")
    else: 
        return random.choice(tgs)


# use the private function to return a number between 28 and 35 
def input_tutorgroup_size(tg, user = False):
    return input_random_range("Number in " + tg + ": ", 28, 35, user)

# grab a number between 1 and 4 and then gather names or generate suitable values 
def input_tutorgroup_candidates(tg, user = False):
    sz = input_random_range("Number of candidates in " + tg + ": ", 1, 4, user)
    if user: 
        rv = []
        for i in range(sz):
            rv.append("Name of candidate {0}: ".format(i+1))
        return rv
    else:
        # if not taking user input, generate 'reasonable' looking strings 
        return [tg+"-"+str(x+1) for x in range(sz)]

# take in a number in a given range, or return a random number in that range 
def input_random_range(msg, lb, ub, user = False):
    if user:
        while True:
            sz = input(msg)
            # is the input an integer? if not, error message and repeat 
            if sz.isnumeric():
                # it is at least an integer, so check if it is in the required range 
                sz = int(sz) 
                if lb <= sz <= ub: 
                    return sz
            print("Need a value in the range [{0},{1}].".format(lb,ub))
    else: 
        return random.randint(lb,ub)

# for the given number of voters (sz) and the avaiable candidates (cands), take in the user input (or random choice)
# with optional arguments, ids, for the voter codes in task 2 
def tutorgroup_vote(sz, cands, user = False, ids = []):
    # use a dictionary to hold the votes. Initialise with the given candidate names,
    # setting each to 0 
    votes = {key:0 for key in cands}
    votes["abstain"] = 0
    if user: 
        voted = []
        while len(voted) < sz:
            takethevote = False
            # if the list of ids is empty, we're not checking the codes 
            if ids == []:
                voted.append(True)
                takethevote = True
            else:
                code = input("voter code:")
                # if we're checking the code there are 3 options:
                #  they've already voted
                #  their code is invalid
                #  their code is valid and need to be recorded 
                if code in voted: 
                    print("You've already voted")
                elif code in ids:
                    voted.append(code)
                    takethevote = True
                else: 
                    print("Invalid voter code")

                if takethevote:
                    print("choices:", cands, " or 'abstain'")
                    while True: 
                        vote = input("vote of student", s)
                        if vote in cands or vote != 'abstain':
                            votes[vote] += 1
                            break
                        print("invalid choice (I am case sensitive)")

    else:
        # note that we don't need the loop variable, so Python lets us replace this with an underscore
        for _ in range(sz):
            v = random.randint(0, len(cands))
            if v == len(cands):
                key = "abstain"
            else: 
                key = cands[v]
            votes[key] += 1

    return votes

# track the highest non-abstention total and the list of candidates with that total
def winning_candidates(votes):
    highest = -1
    candidates = []
    # loop through the dictionary to find the highest score and all those with that score 
    for k,v in votes.items():
        if k == "abstain":
            continue
        if v == highest:
            candidates.append(k)
        if v > highest:
            highest = v 
            candidates = [k]
    return candidates 

# task 2 - generate random codes for each of the students 
def voter_numbers(tgsz,sz = 12):
    # the uuid.uuid4() function returns a long string of hex digits,
    # chop off the first 12 (by default) 
    # generate according to RFC4122 - https://tools.ietf.org/html/rfc4122 
    return [uuid.uuid4().hex[:sz] for _ in range(tgsz)]

# print a summary and return a boolean as to whether there was a clear winner 
def summarise(tgsz, votes, winners):
    cast = tgsz - votes["abstain"] 
    for k in votes:
        # don't summarise abstentions
        # %age is of non-absentations, is this correct? 
        if k != "abstain":
            print("{0} received {1} vote{2} ({3}%)".format(k, votes[k], "" if votes[k] == 0 else "s", round(100.0*votes[k]/cast, 1)))
    print("{0} votes were cast, of which {1} were abstentions".format(tgsz, votes["abstain"]))
    if len(winners) > 1:
        print("TIE!")
    else: 
        print("{0} is the winner".format(winners[0]))
    return len(winners) == 1


# AS IT STANDS HERE, ALL DATA CREATED IS RANDOM, USE THE 'True' IN
# THE FUNCTIONS TO TAKE USER INPUT 

# generate the task 1 values
tg = input_tutorgroup()
tgsz = input_tutorgroup_size(tg)
# generate the task 2 codes 
votercodes = voter_numbers(tgsz)
cands = input_tutorgroup_candidates(tg)

print(tg, tgsz, cands)
print(votercodes)

# generate the task 3 output 
while True: 
    votes = tutorgroup_vote(tgsz, cands)
    print(votes)
    winners = winning_candidates(votes)
    print("winning candidate(s) for "+ tg+": "+str(winners))
    if summarise(tgsz, votes, winners):
        break 
    print("run-off!")
    cands = winners
