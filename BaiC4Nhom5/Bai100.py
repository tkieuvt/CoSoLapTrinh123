from calendar import monthrange
def thangvanam():
    a=int(input('Thang:'))
    b=int(input('Nam:'))
    a,c=monthrange(b,a)
    return c
def ketqua(c):
    print(c)
c=thangvanam()
ketqua(c)