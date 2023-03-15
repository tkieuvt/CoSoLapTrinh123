'''n=int(input())
while (n>=0):
    s=1 
    i=2
    while (i<=n): 
        s=s*i
        i=i+1
    print(s)
    n=int(input())
'''
n=int(input())
while (n>=0):
    s=1 
    for i in range(2,n+1,1):
        s=s*i
    print(s)
    n=int(input())