'''i=1
while i<=6:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print('\n')
    i+=1'''
i=1
while i<=6:
    j=1
    while j<=6-i: 
        print(" ",end="")
        j=j+1
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print('\n')
    i+=1