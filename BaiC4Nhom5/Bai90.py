def Integer(s):
    for j in range(1,len(s)):
        if s[j].isdigit() == False : #kiếm tra kí tự nào không phải là số
            return 0
    if s[0] == "+" or s[0] == "-" or s[0].isdigit() : #kiểm tra kí tự đầu là sô hay dấu +/-
        return 1
    
def inkq(kq):
    if kq == 1 : print('Chuoi nay dai dien cho so nguyen')
    else : print('Chuoi nay khong dai dien cho so nguyen')
    
def nhap():
    s=input("Nhap chuoi can kiem tra: ")
    s=s.strip(" ")  #xóa kí tự trống ở đầu và cuối
    return s

s=nhap()
kq=Integer(s)
inkq(kq)