# def nhap():
#     x=int(input("x="))
#     global y 
#     y=5
#     return x+y

# kq=nhap()
# print("y=",y,sep="")
# print("kq=",kq,sep="")
def inkq(n):
    for i in range(2,n+1,2):
        print(i)
n=int(input())
inkq(n)