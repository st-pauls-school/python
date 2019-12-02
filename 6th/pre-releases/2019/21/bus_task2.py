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
