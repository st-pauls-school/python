listA = [1, 3, 5, 7, 11]
listB = [2,4,6,8,10]

def add_vectors(a, b):
    rv = []
    if len(a) != len(b):
        return rv 

    for i in range(len(a)):
        rv.append(a[i] + b[i])
    
    return rv

print(add_vectors(listA,listB))



print('Specials') 

def add_vectors2(a,b):
    return [a[i] + b[i] for i in range(len(a))] if len(a)==len(b) else []

print(add_vectors2(listA,listB))
