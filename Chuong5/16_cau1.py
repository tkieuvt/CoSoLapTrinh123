def nhap():
    # a = [1,2,3,4,5,6]
    x = int(input())
    k = int(input())
    n = int(input())
    a = []
    for i in range(n):
        a += [int(input())]
    return a,x,k
# def add(a,x,k):
#     a = a[:k] +[x]+a[k:]
#     return a
def add(a,x,k):  
    if k > len(a) : 
        # a.append(x)
        a += [x]
    else: 
        # a.insert(k,x)
        
        a =a[:k]+[x]+a[k:]
        
        # a += [" "]
        # for i in range(k,len(a)):
        #     c = a[i]
        #     a[i] = x
        #     x = c
    return a
a,x,k = nhap()
print(add(a,x,k))

    


    