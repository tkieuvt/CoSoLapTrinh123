s = input()
s = s.lower()
punc = [',',';',':','.']
# thêm khoảng trắng vào trước sau dấu câu
i = 0
while i < len(s):
    if s[i] in punc : 
        s = s[:i]+" "+s[i]+" "+s[i+1:]
        i += 2
    else : 
        i += 1
a = s.split()
# ghép chữ và dấu câu
i = 0
while i < len(a):
    if a[i] in punc : 
        a[i-1] += a[i]
        del(a[i])
    else : 
        i += 1
print(a)
s = " ".join(a)
print(s.capitalize())
