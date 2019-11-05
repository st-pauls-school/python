listA = [4,3,6,8,11,2]

def third(incoming):
    item = incoming[2]
    return item

x = third(listA) 
print(x)

def sumlasttwo(incoming):
    length = len(incoming)
    if length == 0:
        return 0
    elif length == 1:
        return incoming[-1]
    return incoming[-1] + incoming[-2]

print(sumlasttwo(listA))
