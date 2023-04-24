n=input('nhap chuoi:')
nguyenam=['a','e','o','i','u']
if n[0] in nguyenam:
    n=n+'way'
else:
    for i in range(1,len(n)):
        if n[i] in nguyenam:
            n=n[i:]+n[:i]+'ay'
            break
print(n)