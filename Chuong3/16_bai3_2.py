m1=int(input("M1="))
m2=int(input("M2="))
m3=int(input("M3="))
s=int(input("S="))
if s<=100: t=s*m1
elif s<=150: t=(100*m1)+((s-100)*m2)
else: t=(100*m1)+(50*m2)+((s-150)*m3)
print("Phai tra=",t,sep="")