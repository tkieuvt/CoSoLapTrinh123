def lasonguyento(x):
    for i in range(2,int((x/2)+1)):
        if x%i==0: return False
    return True
def sohople(x):
    if x<=1: return False
    return True
def nhapvadem():
    x=int(input())
    kq=0
    while sohople(x): 
        if lasonguyento(x): kq+=1
        x=int(input())
    return kq
def inkq(kq):
    print("Co",kq,"so nguyen to")
print("Nhap day so:")
kq=nhapvadem()
inkq(kq)