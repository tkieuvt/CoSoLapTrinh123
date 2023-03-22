import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def giaipt(a,b,c):
    denta=b*b-4*a*c
    x1=0;x2=0
    if denta>0: 
        x1=(-b+math.sqrt(denta))/(2*a)
        x2=(-b-math.sqrt(denta))/(2*a)
    elif denta==0:
        x1=-b/(2*a)
        x2=x1
    return x1,x2
def inkq(x1,x2):
    if x1==x2 and x1!=0: 
        print("Phuong trinh co nghiem kep\nx1=x2=",x1,sep="")
    elif x1!=x2:
        print("Phuong trinh co hai nghiem\nx1=",x1,"\nx2=",x2,sep="")
    else: print("Phuong trinh vo nghiem")
a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)       

    