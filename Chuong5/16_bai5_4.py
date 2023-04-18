n = int(input("n="))
a = []
for i in range(n):
    a += [int(input())]
# print(a[::-1])
a.reverse()
print(a)

a.sort()
print(a)
    