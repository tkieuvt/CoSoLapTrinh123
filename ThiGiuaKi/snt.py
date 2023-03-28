def prime(n):
    for i in range(n-1,0,-1):
        d=0
        for j in range(2,i,1):
            if i%j==0: 
                d+=1
                break
        if d==0 : return i
        
def nhap():
    n=int(input("n="))
    print(prime(n))
    
nhap()
    