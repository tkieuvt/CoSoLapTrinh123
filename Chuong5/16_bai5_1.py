def nhap():
    n=int(input("n="))
    a=[]
    for i in range(0,n):
        a += [int(input())]
    x=int(input("x="))
    return n,a,x
def FirstAndLast(a):
    L=[]
    L.append(a[0])
    L.append(a[-1])
    return L
def Search(a,x):
    d=a.count(x)
    if d != 0 : return True
    return False
n,a,x=nhap()
print(FirstAndLast(a))
print(Search(a,x))