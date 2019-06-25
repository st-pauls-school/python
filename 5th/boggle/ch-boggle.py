from random import shuffle
dice = [['R','I','F','O','B','X'],['I','F','E','H','E','Y'],['D','E','N','O','W','S'],['U','T','O','K','N','D'],['H','M','S','R','A','O'],['L','U','P','E','T','S'],['A','C','I','T','O','A'],['Y','L','G','K','U','E'],['Qu','B','M','J','O','A'],['E','H','I','S','P','N'],['V','E','T','I','G','N'],['B','L','A','I','Y','T'],['E','Z','A','V','N','D'],['R','A','L','E','S','C'],['U','W','I','L','R','G'],['P','A','C','E','M','D']]

def words(filename="collins.txt"):
    with open(filename, "r") as handle:
        wordlist = handle.readlines()
    wordlist = [w.strip().lower() for w in wordlist]
    return wordlist 

def generate_board():
    for b in dice:
        shuffle(b)
    shuffle(dice)
    return [x[0] for x in dice]


# for each location, generate the valid neighbours
def generate_neighbours(): 
    neighbours = []
    for i in range(16):
        x = i % 4
        y = i // 4
        ineighbours = []
        for xdelta in [-1,0,1]:
            if x == 0 and xdelta == -1:
                continue
            if x == 3 and xdelta == 1:
                continue 
            for ydelta in [-1,0,1]:
                if y == 0 and ydelta == -1:
                    continue
                if y == 3 and ydelta == 1:
                    continue 
                if xdelta == 0 and ydelta == 0:
                    continue
                ineighbours.append(((y + ydelta)*4) + x + xdelta)
        neighbours.append(ineighbours)
    return neighbours


def indices_to_string(indices, board):
    s = ""
    for i in indices:
        s += board[i]
    return s.lower()


#def valid_pattern(pattern, w):
#    f = [x for x in w if x[:len(pattern)] == pattern]
#    return len(f) > 0, pattern in f

def valid_pattern(pattern, w):
    f = find_pattern(pattern, w, 0, len(list_of_words)-1)
    if f == -1:
        return False, False
    while True:
        if w[f] == pattern:
            return True, True
        if w[f][:len(pattern)] == pattern:
            f -= 1
        else:
            return True, False 
    

def find_pattern(pattern, w, f, t):
#    print(f,t)
    if f > t:
        return -1
    if f == t:
        return f if w[f][:len(pattern)] == pattern else -1
    mid = (f+t)//2 
    middle_pattern = w[mid][:len(pattern)]
    if middle_pattern == pattern:
        return mid
    if middle_pattern > pattern:
        return find_pattern(pattern, w, f, mid-1)
    else:
        return find_pattern(pattern, w, mid+1, t) 
    
    

list_of_words = words()
# print(valid_pattern("asp", list_of_words))


trails = [[x] for x in range(16)]

neighbours = generate_neighbours()
board = generate_board()

print(board[0:4])
print(board[4:8])
print(board[8:12])
print(board[12:16])

candidates = [] 
while len(trails) > 0:
    head = trails.pop()
    for n in neighbours[head[-1]]:
        if n in head:
            continue 
        cp = head[:] + [n]
        pattern = indices_to_string(cp, board)
        vp = valid_pattern(pattern, list_of_words)
        if vp[0]:
            trails.append(cp)
        if vp[1]:
            candidates.append(pattern) 
#            print(pattern, len(trails))

candidates = list(set(candidates))
candidates.sort()
candidates.sort(key=len, reverse=True)
print(candidates) 


# # starting with single letters
# add all valid neighbours (that aren't in the list)
# remove any which aren't valid stubs
# if a valid word, add to the list 
