s = input()
a = s.split()
punctuation = ['.',',',':',';']
# punctuation = ['.',',',':',';','?','!','-']
for i in range(len(a)):
    a[i] = a[i].lower()
    for j in range(len(a[i])):
        
print(a)
s = " ".join(a)
print(s)