n=int(input("n="))
a = []
d = 0
aver = 0
c = 0
for i in range(0,n):
    a += [int(input())]
    if a[i] > 0 : d += 1
    if a[i] % 2 == 0 : 
        c += 1
        aver += a[i]
print("SND=",d,sep="")
if c == 0 : aver = 0
else : aver/=c
print("TBC=",aver,sep="")
    