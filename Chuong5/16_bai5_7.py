def nhap():
    n = int(input('n='))
    a = []
    for i in range(n):
        a += [int(input())]
    return a
def delete(a):
    i = 0
    m = []
    while i < len(a):
        m += [a[i]]
        x = a[i]
        while x in a:
            a.remove(x)
    return m
a = nhap()
a = delete(a)    
print(a)