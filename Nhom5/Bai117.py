diem = []
while True:
    a = input('Nhập toạ độ x:')
    if a == '':
        break
    x = float(a)
    y = float(input('Nhập toạ độ y:'))
    diem.append((x, y))
n = len(diem)
Tongx = sum([c[0] for c in diem])
Tongy = sum([c[1] for c in diem])
Tongxy = sum([c[0] * c[1] for c in diem])
Tongxbinhphuong = sum([c[0] ** 2 for c in diem])
m = (Tongxy - Tongx * Tongy / n) / (Tongxbinhphuong - Tongx ** 2 / n)
b = (Tongy / n) - (m * (Tongx) / n)
print('y =',round(m,2),'x +', round(b,1))