negatives = []
zeros = []
positives = []
while True:
    num = input()
    if num == "" : break
    num = int(num)
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)
for n in negatives:
    print(n)
for n in zeros:
    print(n)
for n in positives:
    print(n)