def sohoanhao(n):
    s=1
    for i in range(2,n):
        if n%i==0:
            s=s+i
    return n==s
def inkq():
    print('So hoan hao tu 1 den 10000 la:')
    l=[]
    for k in range(1,10000+1):
        if sohoanhao(k):
            l.append(k)
    print (l)
inkq()