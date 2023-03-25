import random
def taobiensoxe():
    if random.random()<0.5:
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=random.randint(0,9)
        d=random.randint(0,9)
        a1=random.choice("qwertyuiopasdfghjklzxcvbnm")
        a2=random.choice("qwertyuiopasdfghjklzxcvbnm")
        a3=random.choice("qwertyuiopasdfghjklzxcvbnm")
        print(a,b,c,d,a1,a2,a3,sep="")
    else:
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=random.randint(0,9)
        a1=random.choice("qwertyuiopasdfghjklzxcvbnm")
        a2=random.choice("qwertyuiopasdfghjklzxcvbnm")
        a3=random.choice("qwertyuiopasdfghjklzxcvbnm")
        print(a1,a2,a3,a,b,c,sep="")
taobiensoxe()