a=int(input())
b=int(input())
n=int(input())
if a+b==n: print("+")
elif a-b==n: print("-")
elif a*b==n: print("*")
elif (b!=0): 
    if a/b==n: print("/")
else: print("NO")