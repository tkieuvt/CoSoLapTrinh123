import random
def tao_mat_khau_ngau_nhien():
    do_dai = random.randint(7, 10)
    mat_khau = ''
    for i in range(do_dai):
        mat_khau += chr(random.randint(33, 126))
    return mat_khau
print(tao_mat_khau_ngau_nhien())