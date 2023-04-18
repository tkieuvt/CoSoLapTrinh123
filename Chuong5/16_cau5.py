def nhap():
    # a = [1,2,3,4,5,6]
    x = int(input())
    y = int(input())
    n = int(input())
    a = []
    for i in range(n):
        a += [int(input())]
    return a,x,y
def update(a,x,y):
    for i in range(len(a)):
        if a[i] == x : a[i] = y
    return a
a,x,y = nhap()
a = update(a,x,y) 
print(a)