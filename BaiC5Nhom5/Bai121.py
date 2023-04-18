def nhap():
    n = int(input("n="))
    a = []
    for i in range(n):
        a += [int(input())]
    maxx = int(input("max="))
    minn = int(input("min="))
    return a,maxx,minn
def countRange(a,maxx,minn):
    b = []
    for i in range(len(a)):
        if minn <= a[i] < maxx :
            b += [a[i]]
    return b
a,maxx,minn = nhap()
b = countRange(a,maxx,minn)
print(len(b))
print(b)
        