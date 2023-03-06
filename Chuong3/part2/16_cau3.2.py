n=int(input())
i=1
while (i<=n):
    print(i,end=" ")
    if(i%10==0): print('\n')
    i=i+1
'''n=int(input())
m=n/10
if (n%10>0): m=m+1
i=1
while (i<=m):
    j=1
    while (j<=10): 
        print((i-1)*10+j,end=" ")
        if((i-1)*10+j==n): break
        j=j+1
    print('\n')
    i=i+1'''
'''n=int(input())
for i in range(1,n+1,1):
    print(i,end=" ")
    if(i%10==0): print('\n')    '''  