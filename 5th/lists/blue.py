listA = [4,3,6,8,11,2]
listB = ["hello", "to", "5CO.5", "!!"]
def PrintList(incoming):
    for i in incoming:
        print(i)
        
PrintList(listA)

def Contains(li, item):
    index = 0
    while index < len(li):
        if li[index] == item:
            return True
        index += 1
    return False

print('should be True:', Contains(listA, 4))
print('should be False:', Contains(listA, 5))

def partial(li, startingat, num):
    for i in range(startingat, startingat + num):
        print(li[i])      
    
partial([2,4,6,8, 10, 12], 3, 2)

def PrintListOnALine(li):
    index = 0
    while index < len(li):
        print(li[index], end=" ") 
        index += 1
    print()

PrintListOnALine(listA)

def Counter(li):
    index = 0
    #while index < len(li):
    for x in li: 
        index += 1
    return index

print('should be ',len(listA),":", Counter(listA))

def PrintNicely(li):
    if len(li) == 1:
        print (li[0])
        return
    if len(li) > 2:
        for i in range(len(li)-2):
            print(li[i], end=", ")
    print(li[-2], 'and', li[-1])

PrintNicely(listA)

def Filter(li, item):
    c = 0
    for i in li:
        if i > item:
            c += 1
    return c

print("should be 1: ", Filter(listA, 9))



###  And some alternative versions using len, in and so on - and some extra Python special sauce 
print("Specials")

def partial2(li, startingat, num):
    PrintList(li[startingat:startingat+num])

partial2([2,4,6,8, 10, 12], 3, 2)


def PrintListOnALine2(l):
    print(' '.join([str(x) for x in l]))
    
PrintListOnALine2(listA)


def Filter2(li, item):
    return len([x for x in li if x > item])

print("should be 1: ", Filter2(listA, 9))
