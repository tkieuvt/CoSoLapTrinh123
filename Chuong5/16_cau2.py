def nhap():
    # a = [1,2,3,4,5,6]
    x = int(input())
    # k = int(input("k="))
    n = int(input())
    a = []
    for i in range(n):
        a += [int(input())]
    return a,x

def search(a,x):
    for i in range(len(a)):
        if x == a[i] : 
            return i
    return None
a,x = nhap()    
print(search(a,x))