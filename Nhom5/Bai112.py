so=[]
while True:
    a=(input(''))
    if a=='':
        break
    so.append(float(a))
Trungbinh=sum(so)/len(so)
DuoiTrungbinh=[]
GiatriTrungbinh=[]
TrenTrungbinh=[]
for a in so:
    if a<Trungbinh:
        DuoiTrungbinh.append(a)
    elif a==Trungbinh:
        GiatriTrungbinh.append(a)
    else:
        TrenTrungbinh.append(a)
print('Trungbinh:',Trungbinh)
for a in DuoiTrungbinh:
    print('Dưới Trung Bình:',a)
for a in GiatriTrungbinh:
    print('Giá trị Trung bình:',a)
for a in TrenTrungbinh:
    print('Tren Trung Bình:',a)