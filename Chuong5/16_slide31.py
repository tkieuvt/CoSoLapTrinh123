def Input():
    a = []
    for i in range(10):
        a += [int(input())]
    x = int(input("x="))
    return a,x
def inkq(a):
    for i in a:
        print(i,",",sep="",end="")
    print()
#cau_a
def thaythe(a,x):
    for i in range(len(a)):
        if a[i] == 5 : a[i] = x
    inkq(a)
# def Delete(a,x):
    # while x in a:
    #     a.remove(x)
    # # for i in a:
    # #     if x in a: a.remove(x)
#     return a
a,x = Input()
thaythe(a,x)

#cau_b
def Delete(a,x):
    i=0
    while i<(len(a)):
        if a[i] == x: del(a[i])
        else: i += 1
    inkq(a)
Delete(a,x)

# def delete(a,x):
#     for i in a:
#         if x in a: a.remove(x)
#     print(a)
#cau_b_c2
# a = [i for i in a if i != x]
# print(a)

# for i in range(len(a)):
#     if a[i] == x: del(a[i])