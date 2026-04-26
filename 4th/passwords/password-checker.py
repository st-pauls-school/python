
def hasUpper(word):
    for ch in word:
        if ch.isupper():
            return True
    return False


def hasLower(word):
    ok = False
    for ch in word:
        if ch.islower() == True:
            ok = True
    return True 
        
def hasSpaces(word):
    changespaces = word.replace(" ", "")
    if word == changespaces:
        return False
    else:
        return True 
    
def hasDigit(word):
    count = 0
    for ch in word:
        if ch.isdigit() == True:
            count = count + 1
    if count > 0:
        return True
    return False
        


    

def check(pw):
    if not hasUpper(pw):
        return "no upper case"
    elif hasLower(pw) == False:
        return "no lower case"
    if hasSpaces(pw):
        return "there are spaces"
    if not hasDigit(pw):
        return "there are no digits"

    return "ok"
            

pw = "p12345"
print(check(pw))
pw = "Pas!word123"
print(check(pw))

