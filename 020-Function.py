# Example 1
def sum(a,b):
    return a+b
result = sum(5,10)
print(result)

# Example 2

def personal_details(name,age):
    print("Name:",name)
    print("Age:",age)
personal_details(age=22,name="chaitanya")

Example 3 default arguments

def greet_user(name,greetings="Hello"):
    return greetings + " ," + name + "!"
greetings1 = greet_user("chaitanya")
greetings2 = greet_user("bob","hi")
print(greetings1)
print(greetings2)