x = int(input("multiple: "))
r = int(input("range: "))
for i in range(r):
    space = ''
    if (i+1) <10:
        space= ' '
    print(space,(i+1),'*',x,'=',(i+1)*x)

