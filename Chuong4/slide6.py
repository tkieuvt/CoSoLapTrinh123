import random
# 1=bua 2=keo 3=bao
def game(nguoi,may):
    if (nguoi==1):
        if (may==1): s="Hòa"
        elif (may==2): s="Người thắng"
        elif (may==3): s="Máy thắng"
    elif (nguoi==2):
        if (may==2): s="Hòa"
        elif (may==3): s="Người thắng"
        else: s="Máy thắng"
    elif (nguoi==3):
        if (may==3): s="Hòa"
        elif (may==1): s="Người thắng"
        elif (may==2): s="Máy thắng"   
    return s
def nhap():
    nguoi=int(input("Người: "))
    may=random.randint(1,3)
    if nguoi==0: return 0
    print("Máy: ",may)
    print("Kết quả: ",game(nguoi,may))
    return nguoi
nguoi=nhap()
while 


# while (nguoi!=0):
#     print("Kết quả: ",game(nguoi,may))
#     nguoi=int(input("Người: "))
#     if (nguoi==0): break
#     may=random.randint(1,3)
#     print("Máy: ",may)
