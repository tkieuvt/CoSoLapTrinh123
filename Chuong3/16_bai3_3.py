x=float(input("x="))
y=float(input("y="))
c=(input("Phep toan:"))
if ((c!='+' and c!='-' and c!='*' and c!='/') or (y==0 and c=='/')):
    print("Khong hop le") 
elif (c=='+'): print(x,"+",y,"=",x+y,sep="")
elif (c=='-'): print(x,"-",y,"=",x-y,sep="")
elif (c=='*'): print(x,"*",y,"=",x*y,sep="")
else: print(x,"/",y,"=",x/y,sep="")
 