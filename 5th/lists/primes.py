def primes(ubound):
    rv = [2]
    candidates = [x for x in range(3,ubound+1,2)]
    candidate = 2
    while candidate < ubound**0.5:
        candidate = candidates[0]        
        rv.append(candidate)
        candidates = list(filter(lambda x: x % candidate != 0, candidates)) 
    return rv + candidates


def number_of_primes(li):
    return len(set(li).intersection(set(primes(max(li)))))

print(number_of_primes([1,2,3,4,5,6,7])) 
