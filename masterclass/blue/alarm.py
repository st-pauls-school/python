current_hour = 14 # int(input("hours in 24 hour form: "))
hours_to_add = 51 

hour_to_go_off = (current_hour + hours_to_add) %24

print("Alarm will go off at " + str(hour_to_go_off) + ":00")

