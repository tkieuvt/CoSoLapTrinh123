def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def max3(a,b,c):
    kq=a
    # kq=max(kq,b)
    # kq=max(kq,c)
    kq=max(b,max(kq,c))
    return kq
def inkq(kq):
    print("So lon nhat la:",kq)
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)