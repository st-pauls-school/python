def bin_insert_at(li, item, f, t):
    mid = (f+t)//2
    if li[mid] == item:
        return mid
    if f >= t:
        if item < li[f]:
            return f
        else:
            return f+1
    if item < li[mid]:
        t = mid-1 
    else:
        f = mid+1 
    return bin_insert_at(li, item, f, t)


def insert_at(li, item):
    if li == []:
        return 0
    return bin_insert_at(li, item, 0, len(li)-1)

li = [1,2,6,7]
val = 5

i = insert_at([1,2,6,7], 5)

li.insert(i, val)

print(li)

