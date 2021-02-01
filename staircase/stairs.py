
# the iterative solution says create all possible combinations,
# counting them when they're correct, dropping them when they overshoot 
def stairsI(target, steps):

    counter = 0

    # these are the possible combinations that haven't been completed yet
    # crucially it's a list containing just an empty list 
    candidates = [[]]
    while True:
        newcandidates = []
        # for each possible step, try to add it to each of the outstanding
        # combinations - hence needing an empty list to start 
        for s in steps:
            # go through each of the candidates in turn, adding the current choice
            for c in candidates:
                # important - copy the candidate, c, don't just add to it 
                nc = c[:] + [s]
                # if it is the target length increment the counter 
                if sum(nc) == target:
                    counter += 1
                # otherwise if there's still space, add it to our list 
                elif sum(nc) < target:
                    newcandidates.append(nc)
                # if we overshoot, do nothing, i.e. drop it
        # if we've not added any new incomplete options, break 
        if newcandidates == []:
            break
        # take the list of new candidates and promote them 
        candidates = newcandidates
    # we're done, return the number 
    return counter

# the recursive version, we make the problem smaller each time
# e.g. the answer is based on asking how many start with each of the steps, noting that
# each option is then the answer to how many ways are there with a reduced target, having
# taken that particular step 
def stairsR(target, steps):
    # if we overshoot, i.e. a negative target, there are no solutions 
    if target < 0:
        return 0
    # if the target is 0, we've found a solution 
    if target == 0:
        return 1
    # initialise a counter 
    counter = 0
    # for each step
    for s in steps:
        # how many options are there, with a target that has reduced by the step we've
        # taken, add it to the total 
        counter += stairsR(target-s, steps)
    return counter

print(stairsI(4, [1,2]))
print(stairsR(4, [1,2]))
print(stairsI(5, [1,3,5]))
print(stairsR(5, [1,3,5]))
            