#tách từng từ trong câu có sẵn
punc = ['.',',','?','!','-',':',';']
s = input("Nhap chuoi: ")
s += " "
for i in range(len(punc)) :
    s = s.replace(punc[i],"")
#tách từ
b = s.split()
print(b)