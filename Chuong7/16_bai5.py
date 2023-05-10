s = input()
x = int(input())
a = s.split()
d = 0
for i in range(len(a)):
    if int(a[i]) == x : 
        print(i+1)
        d = 1
if d == 0 : print(0)