def nhap():
    x=int(input("x="))
    global y 
    y=5
    return x+y

kq=nhap()
print("y=",y,sep="")
print("kq=",kq,sep="")