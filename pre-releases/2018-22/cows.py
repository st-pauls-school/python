from random import uniform

###
print("\rTASK 1")

def generate_random_yields(cows, milking):
	rv = []
	for cow in cows:
		rv.append((cow, milking, uniform(4,10)))
	return rv 

def generate_a_week(cows):
	rv = []
	for day in ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']:
		for m in range(1,3):
			rv += generate_random_yields(cows, "{0}{1}".format(day, m))
	return rv 

number_of_cows = 3
cow_ids = [123, 234, 345]

yields = generate_a_week(cow_ids)

print("{0} cows. {1} yields generated.".format(len(cow_ids), len(yields)))

###
print("\rTASK 2")

def total_volume(milking_data, cow = None):
	return sum([y[2] for y in milking_data if cow == None or y[0] == cow]) 

print("The total volume of milk for the week from the {1} cows is {0:.0f} litres:".format(total_volume(yields), len(cow_ids)))

for cow in cow_ids:
	print("\tcow_{0}: {1:.0f}".format(cow, total_volume(yields, cow)))

###
print("\rTASK 3")
def getKey(item):
	return item[1]
breakout_yields = [(c, total_volume(yields, c)) for c in cow_ids]
sorted(breakout_yields, key=getKey)

print("cow_{0} is top cow with {1:.0f} litres".format(breakout_yields[0][0], breakout_yields[0][1]))

days = [y[1][:-1] for y in yields]
poor_day_counts = []
for cow in cow_ids:
	for d in days:
		for y in filter(lambda x: x[0] == cow, yields):
			print(y)

