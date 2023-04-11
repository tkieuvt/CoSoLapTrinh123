a = []
for i in range(10):
    a += [int(input())]
for i in range(0,10,2):
    c = a[i]
    a[i] = a[i+1]
    a[i+1] = c  
    print(a[i],a[i+1],end=" ") 
# print(a)