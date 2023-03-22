def lasonguyento(x):
    for i in range(2,x):
        if x%i==0: return True
    return False
def sohople(x):
    if x<=1: return True
    return False
def nhapvadem():
    x=int(input())
    kq=0
    while sohople(x)==False: 
        if lasonguyento(x)==True: kq+=1
        x=int(input())
    return kq
def inkq(kq):
    print("Co",kq,"so nguyen to")
print("Nhap day so:")
kq=nhapvadem()
inkq(kq)