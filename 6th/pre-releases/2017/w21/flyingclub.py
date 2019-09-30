fees = {"2" : {30 : 100, 60 : 150}, "4" : {30: 120, 60:200}, "H" : {30: 300, 60: 500}}
refuelling = 30 
starttime = 8
finishtime = 18 

def task1(plane, duration):
	if plane not in fees.keys() or duration not in fees[plane].keys():
		return None
	availableminutes = (finishtime-starttime)*60 
	availableminutesincludingrefuelling = availableminutes + refuelling
	trips = availableminutesincludingrefuelling // (duration + refuelling)
	return (trips, trips * fees[plane][duration])


print(task1("F", 60))
print(task1("2", 45))
for p in "24H":
	for d in [30,60]:
		print("{} x {} = {}".format(p, d, task1(p,d)))

