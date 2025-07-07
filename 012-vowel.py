Name = input("Enter the name: ")

name2 = Name.lower()

a = name2.count('a')
e = name2.count('e')
i = name2.count('i')
o = name2.count('o')
u = name2.count('u')

# print(f"Number of vowels:-{a+e+i+o+u}")

# Method 2

Name = input("Enter the name: ")

vowels = "aeiouAEIOU"

for char in Name:
    if char in vowels:
        print(f"Number of Vowel:- {char}")