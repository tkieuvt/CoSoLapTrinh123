def nhap():
    a = []
    while True:
        x = input()
        if x == '' : break
        a += [x]
    return a
def Print(a):
    for i in range(len(a)):
        print(a[i],end ="")
        if i < len(a)-2 : print(",",end = " ")
        elif i == len(a)-2 : print(" and",end = " ")
a = nhap()
Print(a)