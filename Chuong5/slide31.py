a = []
for i in range(10):
    # x = int(input())
    # a += [x]
    a += [int(input())]
x = int(input("x="))
#cau_a
for i in a:
    if a[i] == 5 : a[i] = x
print(a)
#cau_b
d=0
for i in a:
    if a[i] == x : 
        
        d+=1
        del(i)
        #i=i-1
        print(len(a))
print(a)

