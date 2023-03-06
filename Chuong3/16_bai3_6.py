a=int(input())
b=int(input())
c=int(input())
if (a+b>c and a+c>b and b+c>a):
    if (a*a==b*b+c*c or a*a+b*b==c*c or b*b==a*a+c*c):
        print("Tam giac vuong")
    elif (a==b and b==c and c==a):
        print("Tam giac deu")
    else: print("Tam giac loai khac")
else: print("Khong hop le")