'''def ngaykydieu():
    d=int(input('ngay='))
    m=int(input('thang='))
    y=int(input('nam='))
    if d*m==y%100:
        print('ngay',d,'thang',m,'nam',y,'la ngay dieu ki')
    else:
        print('ngay',d,'thang',m,'nam',y,'la ngay khong  dieu ki')
ngaykydieu()'''

def ngaykydieu(d,m,y):
    if d*m==y%100:
        return True
    return False
def inkq():
    for y in range(1900,2000):
        for m in range (1,13):
            for d in range(1,32):
                if ngaykydieu(d,m,y):
                    print('%04d/%02d/%02d'%(y,m,d))
inkq()