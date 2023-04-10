def nhap():
    n=int(input("n="))
    a=[]
    for i in range(0,n):
        a += [int(input())]
    return n,a
def Search(a):
    maxx=a[0]
    minn=a[0]
    for i in range(1,n):
        if a[i] > maxx : maxx = a[i]
        if a[i] < minn : minn = a[i]
    return maxx,minn
def Output(maxx,minn):
    print(maxx,minn)
n,a = nhap()
maxx,minn = Search(a)
Output(maxx,minn)