n=int(input())
d=0
s=0
if n<10: print(0)
else:
    while d<2:
        s+=(n%10)
        n=n//10
        d+=1
        #print(d," ",s)
    print(s)