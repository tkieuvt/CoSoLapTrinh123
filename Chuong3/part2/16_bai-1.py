n=int(input("n="))
if n==0: s=1
else:
    s=1
    for i in range(1,n+1,1):
        s=s*i;
print(s)