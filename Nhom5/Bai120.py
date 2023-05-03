n=int(input())
l=[]
for i in range(1,n+1):
    l=l+[input()]
k=[]
j=[]
k=l.copy()
k.sort(reverse=True)
j=l.copy()
j.sort()
if l==k or l==j:
    print('True')
else:
    print('False')