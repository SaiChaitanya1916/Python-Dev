m =int(input("Enter the Maths marks:- "))
s =int(input("Enter the Maths Science:- "))
p =int(input("Enter the Maths Physics:- "))

total = m+s+p
average = total/3

percentage = (total/300)*100
grade = ""

if percentage > 90:
    grade ="A"
elif percentage > 80 and percentage <= 90:
    grade ="B"
elif percentage > 70 and percentage <= 80:
    grade ="C"
else:
    grade = "D"

print(f"Your Grade is:{grade} \n Average Marks:{average} \n Total Marks:{total}")