# While
n =int(input("Enter the n:- "))
i = 1
while i<=n:
    print(i)
    i +=1

# For
n =int(input("Enter the n:- "))
for i in range(1,n+1):
    print(i)

# Sum of N natural numbers

n =int(input("Enter the n:- "))
i = 1
sum = 0
while i<=n:
    sum +=i
    i +=1
print(f"Sum of N natural numbers:-{sum}")

print N even numbers

# n =int(input("Enter the n:- "))

i =1
while i<=n:
    if i%2==0:
        print(i)
    i+=1

# print N odd numbers

n =int(input("Enter the n:- "))
i =1
while i<=n:
    if not i%2==0:
        print(i)
    i+=1

# Table of give number with while loop

n =int(input("Enter the n:- "))
i=1
while i<=10:
    print(f"{n} X {i} = {n*i }")
    i +=1

# Table of give number with for loop

n =int(input("Enter the n:- "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i }")

# Factorial of Given number
n =int(input("Enter the n:- "))
factorial = 1
while n>0:
    factorial = factorial * n
    n -=1
print(f"Factorial is:-{factorial}")