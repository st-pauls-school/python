people = [4244, 4004, 3091, 4275, 4104, 3211, 3400, 3800, 4014, 3025, 3490, 3256]
rounds = [[67, 72, 51, 69, 42, 87, 62, 81, 84, 51, 85, 62] , [25, 40, 29, 56, 83, 77, 82, 31, 52, 90, 66, 93], [100, 48, 35, 68, 53, 48, 96, 63, 38, 77, 33, 71]]
means = [sum(rounds[r])/len(rounds[r]) for r in range(len(rounds))]
print('\n'.join(["mean for round {0} is {1:.1f}".format(r+1,means[r]) for r in range(len(rounds))]))
personmaps = [[rounds[m][p] for m in range(3)] for p in range(len(rounds[0]))]
personaltotals = [sum(i) for i in personmaps]
sortedtotals = personaltotals[:]
sortedtotals.sort(reverse=True)
print(', '.join(["{0}: person {1} with {2}".format(['Gold', 'Silver','Bronze'][m], people[personaltotals.index(sortedtotals[m])],personaltotals[personaltotals.index(sortedtotals[m])]) for m in range(3)]))
filtered = [len([i for i in range(len(pm)) if pm[i] >= means[i]]) == len(pm) for pm in personmaps]
print("Special prize winners: {0}".format('none' if len([f for f in filtered if f]) == 0 else ', '.join(str(people[i]) for i in range(len(people)) if filtered[i])))
