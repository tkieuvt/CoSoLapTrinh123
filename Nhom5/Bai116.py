vowel = ['a','e','o','i','u']
# consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','k','r','s','t','v','w','x','y','z']
punctuation = ['.',',','?','!']
s = input("Nhap chuoi: ")
d = 0
if s[0].isupper() : 
    d = 1
    s = s.lower()
if s[0] in vowel : s += 'way'
else :
    for i in range(1,len(s)):
        if s[i] in vowel : 
            # s = s[i:] + s[:i] +'ay'
            Index = i
            break
    if s[-1] in punctuation : s = s[i:-1] + s[:i] +'ay'+s[-1]
    else : s = s[i:] + s[:i] +'ay'   
    if d == 1 : s = s.capitalize()
print(s)
