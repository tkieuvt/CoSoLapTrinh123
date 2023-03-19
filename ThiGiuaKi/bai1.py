a=int(input())
b=int(input())
s=0
for i in range(a+1,b+1,1):
    s+=i
print(s)

# a=int(input())
# b=int(input())
s1=b*(b+1)/2
s2=a*(a+1)/2
print(int(s1-s2))