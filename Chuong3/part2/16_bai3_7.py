n=int(input())
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
for j in range(1,10000000000000000000000000000000000000000,1):
    s=1 
    for i in range(2,n+1,1):
        s=s*i
    print(s)
    n=int(input())
    if n<0: break'''