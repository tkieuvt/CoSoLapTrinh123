#slide_17
'''
def show_number(n=10):
    for i in range(1,n+1):
        print(i)
show_number(5)
show_number()'''
#slide_20
'''
def phepcong(x , y = None):
    if y == None:
        return x
    else: return x + y
kq1 = phepcong(2)
kq2 = phepcong(5,2)
print(kq1,kq2)'''
#slide_7
'''def hello():
    print("Howdy!")
    print("Hello there!")
for i in range(1,4): hello()'''
#slide_11
'''
def hello(name):
    print("hello"+name)
hello("alice")'''
#slide_16
'''def show_number(m,n):
    for i in range(m,n+1):
        print(i)
show_number(2,6)'''
#slide_18
'''def show_number(m=1,n=10):
    for i in range(m,n+1):
        print(i)
show_number(3,7)
show_number(3)
show_number()'''
#slide_24
def nhap():
    x=int(input("x="))
    y=int(input("y="))
    return x,y
a=nhap() 
print("2 so vua nhap la",a[0]*2)
