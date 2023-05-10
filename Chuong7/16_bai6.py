s = input()
a = s.split(",")
b = []
for i in range(len(a)):
    if int(a[i],2) % 3 == 0 : 
        b += [a[i]]
print(",".join(b))