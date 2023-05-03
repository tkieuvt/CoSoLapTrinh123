import re
s = input()
if (6 <= len(s) <= 17) and re.search("[a-z]",s) and re.search("[0-9]",s) \
    and re.search("[A-Z]",s) and re.search("[#$@]",s) : print(True)
else : print(False)

    
