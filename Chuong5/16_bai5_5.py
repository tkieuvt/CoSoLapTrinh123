n = int(input("n="))
a = []
s = 0
for i in range(n):
    a += [int(input())]
    if i % 2 == 1 : s += a[i]
print("Tong=",s,sep="")