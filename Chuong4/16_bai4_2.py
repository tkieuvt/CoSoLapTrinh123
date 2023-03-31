def inkq(n):
    for i in range(2,n+1,2): 
        print(i,end=" ")
    print()
def nhap():
    n=int(input("n="))
    inkq(n)
t=""
while (t!="k" and t!="K"):
    n=nhap()
    t=input("Tiep tuc khong?")


# # dieu kien nhap long def 
# def inkq(n):
#     for i in range(2,n+2,2): 
#         print(i,end=" ")
# def nhap():
#     n=int(input("n="))
#     inkq(n)
#     # t=""
#     t=input("Tiep tuc khong?")
#     if (t!="k" and t!="K"): nhap()
# nhap()