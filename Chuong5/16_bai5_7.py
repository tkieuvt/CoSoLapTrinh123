def nhap():
    n = int(input('n='))
    a = []
    for i in range(n):
        a += [int(input())]
    return a
def delete(a):
    i = 0
    m = []
    for i in a:
        if i not in m : 
            m += [i]
    return m
a = nhap()
a = delete(a)   
for i in range(len(a)):
    print(a[i],end=" ")