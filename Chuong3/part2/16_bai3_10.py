#cau_a
n=int(input("n="))
for i in range(1,n+1,1): print(i)
#cau_b
n=int(input("n="))
for i in range(1,n+1,1):
    print(i,end=" ")
    if i%5==0: print()
#print()
#cau_c
n=int(input("n="))
for j in range(1,n+1,1):
    for i in range(1,n+1,1): print(i,end=" ")
    print()
    