s = input()
a = []
for i in s :
    if i not in a :
        a += [i]
print("".join(a))