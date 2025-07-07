#a,b,c
a = int(input("Enter a:-"))
b = int(input("Enter b:-"))
c = int(input("Enter c:-"))

Root1=0
Root2=0

d = (b**2) - 4*a*c
Root1 =(-b + (d**(0.5)))/2*a
Root2 =(-b - (d**(0.5)))/2*a
print(f"Roots:",Root1,Root2,sep=",")



