# #thuc hien phep toan den khi 
# def pheptoan(x,y,c):
#         # if (c!='+' and c!='-' and c!='*' and c!='/'): break
#         if (c=='+'): print(x,"+",y,"=",x+y,sep="")
#         elif (c=='-'): print(x,"-",y,"=",x-y,sep="")
#         elif (c=='*'): print(x,"*",y,"=",x*y,sep="")
#         elif y!=0: print(x,"/",y,"=",x/y,sep="")
# def nhap():
#     x=float(input("a="))
#     y=float(input("b="))
#     c=(input("Phep toan:"))
#     pheptoan(x,y,c)
#     t=input("tiep tuc:")
#     if t!="T" and t!="t" : nhap()
# nhap()
#in n so nguyen to dau tien
import math
def prime(x):
    d = 0
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0 : return 1
    return 0
n = int(input("n="))
d = 0
for i in range(2,10000000):
    if prime(i) == 0: 
        print(i,end=" ")
        d += 1
    if d == n: break
        
    