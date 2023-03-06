x=float(input("a="))
y=float(input("b="))
c=(input("Phep toan:"))
while (c!="T" or c!="t"):
    if (c!='+' and c!='-' and c!='*' and c!='/'): break
    elif (c=='+'): print(x,"+",y,"=",x+y,sep="")
    elif (c=='-'): print(x,"-",y,"=",x-y,sep="")
    elif (c=='*'): print(x,"*",y,"=",x*y,sep="")
    elif y!=0: print(x,"/",y,"=",x/y,sep="")
    x=float(input("a="))
    y=float(input("b="))
    c=(input("Phep toan:"))
