'''n=1
while n<=9 :
    j=1
    while j<=9: 
        if j!=1 and (j*n)//10==0: print(" ",end="")
        print(j*n,end=" ") 
        j+=1
    print()
    n=n+1
'''
for i in range(1,10,1):
    for j in range(1,10,1): 
        if j!=1 and (j*i)//10==0: print(" ",end="")
        print(j*i,end=" ") 
    print()
