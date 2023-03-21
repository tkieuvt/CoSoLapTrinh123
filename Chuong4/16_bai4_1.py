def nhap():
    n=int(input("n="))
    return n
def giaithua(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x
def inkq(n,x):
    print(n,"!=",x,sep="")
n=nhap()
x=giaithua(n)
inkq(n,x)