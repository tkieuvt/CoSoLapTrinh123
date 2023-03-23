def nhap():
    n=int(input("So luong hang da mua: "))
    return n
def tienvanchuyen(n):
    n-=1
    print("Phi van chuyen cho don hang:",round(10.95+n*2.95,2))
n=nhap()
tienvanchuyen(n)