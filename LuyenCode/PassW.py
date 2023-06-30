n = int(input())
a = []
for i in range(n):
    s = input()
    d1 = 0; d2 = 0; d3 = 0
    safe = min(5,max(0,len(s)-5))
    for j in range(len(s)):
        if s[j].isupper() : d1 = 1
        if s[j].isnumeric() : d2 = 1
        if s[j].islower() : d3 = 1
    d = d1+d2+d3
    if d == 1 : safe += 1
    if d == 2 : safe += 2
    if d == 3 : safe += 5
    a += [safe]
for i in a: print(i,end=" ")