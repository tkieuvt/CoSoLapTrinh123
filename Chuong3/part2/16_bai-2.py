n=int(input("n="))
d=0
for i in range(2,n,1):
    if n%i==0: d=d+1
if d==0: print(n,"la SNT")
else: print(n,"khong la SNT")