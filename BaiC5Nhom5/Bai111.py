#tách từng từ trong câu có sẵn
punctuation = ['.',',','?','!','-',':',';']
s = input("Nhap chuoi: ")
s += " "
for i in range(len(punctuation)) :
    s = s.replace(punctuation[i],"")
#tách từ
b = s.split()
print(b)