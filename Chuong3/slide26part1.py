bonus=0
y=int(input("yrsOfServer="))
salary=int(input("salary="))
if (y<5): 
    if(salary<500): bonus=100
    else: bonus=200
else: bonus=700
print("Bonus moult: ",bonus)
