# While loop
candies = 10
while candies > 0:
    print("Candies Available")
    candies -=1

# for loop

candies = 10

for i in range(0,candies):
    print("Candies Available")

# for loop for sequence

name ="chaitanya"

for i in name:
    print(i)

name = "Pavana"
length = len(name)
for i in range(length):
    print(i)

# Nested loop

for i in range(1,6):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j} ")