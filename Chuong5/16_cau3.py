def nhap():
    # a = [1,2,3,4,5,6]
    x = int(input())
    # k = int(input("k="))
    n = int(input())
    a = []
    for i in range(n):
        a += [int(input())]
    return a,x
def delete(a,x):
    b = [] 
    for i in range(len(a)):
        if a[i] != x : b += [a[i]] 
    return b
a,x =  nhap()
a = delete(a,x)
print(a)