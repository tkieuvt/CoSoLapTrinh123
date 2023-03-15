#slide_31
def nhap():
    global n
    n=int(input("n="))
    return n
def nhapvadem(n):
    print("Nhap",n,"so nguyen:")
    d=0
    for i in range(1,n+1):
        a=int(input())
        if a%2==0 and a!=0: d+=1
    return d
def inkq(d):
    print("So chu so chan la:",d)
nhap()
d=nhapvadem(n)
inkq(d)