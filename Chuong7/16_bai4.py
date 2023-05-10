s = input()
a = s.split(",")
a.sort()
i = 1
while i < len(a):
    if a[i] != a[i-1] : i += 1
    else : a.remove(a[i])
s = ",".join(a)
print(s)