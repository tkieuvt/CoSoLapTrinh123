def inKQ(Upper,Lower,Num,Remaining):
    print("In hoa:",Upper)
    print("In thuong:",Lower)
    print("Chu so:",Num)
    print("Khac:",Remaining)
    
def main():
    s = input()
    Upper = 0
    Lower = 0
    Num = 0
    Remaining = 0
    for i in range(len(s)):
        if s[i].isupper() : Upper += 1
        elif s[i].isnumeric() : Num += 1
        elif s[i].lower() and s[i].isalpha() : Lower += 1
        else : Remaining += 1
    inKQ(Upper,Lower,Num,Remaining)

main()
