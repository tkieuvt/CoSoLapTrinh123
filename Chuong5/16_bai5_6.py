def nhap():
    a = []
    for i in range(10):
        a += [int(input())]
    return a
def swap(a):
    for i in range(0,len(a),2):
        c = a[i]
        a[i] = a[i+1]
        a[i+1] = c  
        print(a[i],a[i+1],end=" ") 
a = nhap()
swap(a)