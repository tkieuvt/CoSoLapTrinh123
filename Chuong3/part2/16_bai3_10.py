#cau_a
n=int(input())
for i in range(1,n+1,1): print(i)
#cau_b
n=int(input())
for i in range(1,n+1,1):
    print(i,end=" ")
    if i%5==0: print('\n')
#cau_c
n=int(input())
for j in range(1,n+1,1):
    for i in range(1,n+1,1): print(i,end=" ")
    print('\n')
    