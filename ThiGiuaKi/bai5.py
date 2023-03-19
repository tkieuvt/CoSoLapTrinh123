n=int(input())
if n%2==0: n+=1
s=0
for i in range(2,n,2):
    s+=i
print(s)

# n=int(input())
# if n%2!=0: n-=1
# s=(n*(n+1)/2)-(n/2)
# print(int(s/2+n/2))