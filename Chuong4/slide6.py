def nhap():
    print("Nhap mot so nguyen:")
    n=int(input("n="))
    return n
def tinh(n):
    s=0
    for x in range(1,n+1):
        s=s+x
    return s
def inkq(n,s):
    print("Tong cua ",n," so nguyen duong dau tien=",s,sep="")
n=nhap()
s=tinh(n)
inkq(n,s)