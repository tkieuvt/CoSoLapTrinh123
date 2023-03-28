def int2any(n,Outp):
    s='0123456789ABCDEF'
    num=""
    while n>0:
        num=s[n%Outp]+num
        n//=Outp
    return num
def any2int(x,Outp):
    num=0
    power=0  #mũ
    s='0123456789ABCDEF'
    while len(x)>0:
        num+=s.find(x[len(x)-1]) *(Outp**power)
        #print(x[len(x)-1],num)
        x=x[:len(x)-1]
        power+=1
    return num
def nhap():
    Inp=int(input("Nhap co so dau vao:"))
    Outp=int(input("Nhap co so dau ra:"))
    if Inp<2 or Inp>16 or Outp<2 or Outp<16 :  #kiểm tra cơ số có thuộc 2-16
        print("Khong hop le")
        return 0
    else :
        n=input("so can chuyen: ")
        coso10=any2int(n,Inp)  #chuyển cơ số ban đầu về cơ số 10
        chuyendoi=int2any(coso10,Outp)   #chuyển cơ số ban đầu về cơ số yêu cầu Output
        print("số ở hệ cơ số",Outp,"là:",chuyendoi)
nhap()