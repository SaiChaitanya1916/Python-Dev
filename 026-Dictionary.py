# Dictionary is an unordered collection of "key-value" pairs.
# are used to store data in the form of key-value pairs,where each key is unique

my_dict = {'name':'GT650','age':6,'location':'HYD'}


name = my_dict['name']
age = my_dict['age']
location =my_dict['location']
my_dict['CC'] = '648'   # to add elements 

print(name)
print(age)
print(location)
print(my_dict)

# Methods
# keys() #it will print keys only
# values() #it will print values only
# items() #it will print all items in dist
# get() #can you get specific value
# pop()
# update()

for i in my_dict.values():
    print(i)


for j in my_dict.keys():
    print(j)

for i,j in my_dict.items():
    print(i,j)

# Comprehensions

squares_dist = {x: x**2 for x in range(1,6)}
print(squares_dist)