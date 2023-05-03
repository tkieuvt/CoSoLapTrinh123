def tokenize(s):
    tokens = []
    token_2 = ""
    for i in range(len(s)):
        if s[i].isspace(): 
 #  kiểm tra xem ký tự hiện tại trong biểu thức toán học có phải là khoảng trắng (space), tab (\t), newline (\n)  hay không.
            continue
        elif s[i] in "+-*/^()":
            if len(token_2) > 0:
                tokens.append(token_2)
                token_2 = ""
            tokens.append(s[i])
        else:
            token_2 += s[i]
    if len(token_2) > 0:
        tokens.append(token_2)
    return tokens

def main():
    a = input("Nhập 1 chuỗi: ")
    tokens = tokenize(a)
    print(tokens)
main()