def nhap():
    # a = [1,2,3,4,5,6]
    # x = int(input("x="))
    # k = int(input("k="))
    n = int(input())
    a = []
    for i in range(n):
        a += [int(input())]
    return a
def count(a):
    d = 0
    for i in a:
        d +=1
    return d
a = nhap() 
print(count(a))