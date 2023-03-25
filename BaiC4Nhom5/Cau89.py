def Viethoa_str(s):
    s = s.capitalize()
    s = s.replace(" i ", " I ")
    index = 0
    while index < len(s) and s[index] not in ".!?":
        index += 1
    while index < len(s):
        if s[index].isalpha():
            s = s[:index] + s[index:].capitalize()
            break
        index += 1
    return s
a= input("Nhap 1 chuoi: ")
VIETHOA_str = Viethoa_str(a)
print(VIETHOA_str)