num1 = int(input("Give num1:- "))
num2 = int(input("Give num2:- "))
operator = input("Enter the operator:- ")

if operator =="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)
else:
    print("Invalid Statement")
