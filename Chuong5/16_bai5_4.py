n = int(input("n="))
a = []
for i in range(n):
    a += [int(input())]
print(a[::-1])
a.sort()
print(a)
    