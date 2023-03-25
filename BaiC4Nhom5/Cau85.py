def enter():
    num=int(input('n='))
    return num
def ordinal(num):
    ans=''
    if num==1:
        ans='1st'
    elif num==2:
        ans='2nd'
    elif num==3:
        ans='3rd'
    elif 4 <= num <= 12 :
        ans=str(num)+'th'
    return ans

def inkq(kq):
    print(kq)

num=enter()
kq=ordinal(num)
inkq(kq)