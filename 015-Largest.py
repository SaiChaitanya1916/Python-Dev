s = input("Enter three numbers separated by commas: ")

x, y, z = s.split(",")

num1 = int(x)
num2 = int(y)
num3 = int(z)

great = 0

if num1 > num2:
    if num1 > num3:
        great = num1
    else:
        great = num3
else:
    if num2 > num3:
        great = num2
    else:
        great = num3

print("The greatest number is:", great)

