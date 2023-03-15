'''a=['A','B','C','D','E','F','G','H','K','L']
n=int(input())
s=""
if n==0: s='A'
while n>0:
    mod=n%10 
    n=n//10
    s=a[mod]+s
print(s)
'''
n=int(input())
s=""
if n==0: s="A"
while n>0:
    mod=n%10
    n=n//10
    if mod==0: s='A'+s
    elif mod==1: s='B'+s
    elif mod==2: s='C'+s
    elif mod==3: s='D'+s
    elif mod==4: s='E'+s
    elif mod==5: s='F'+s
    elif mod==6: s='G'+s
    elif mod==7: s='H'+s
    elif mod==8: s='K'+s
    else: s='L'+s
print(s)