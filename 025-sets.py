# Sets : are an unordered collection of unique elements
# defined using curly braces {} or the set()
# Mutable
# Duplicate elements are automatically removed


fruits = {'Apple','Bananna','Orange'}

fruits.add('Grean Apple')
fruits.remove('Apple')

print(fruits)

# Set Operations 

set1 = {1,2,3}
set2 = {3,5,6}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

# Set membership and length

my_set = {1,2,3}
print(2 in my_set) 
print(4 in my_set)

print(len(my_set))

# Frozen set :- which can be accessible but can't be change or update

my_set = {4,5,6}
frozen_set = frozenset(my_set)
print(frozen_set)

# set comprehensions

squares = {x**2 for x in range(1,6)}
print(squares)

# Set Methods
# copy() copy all elements in set and can be stored in another set
# clear() it will remove all elements
# pop() it remove last element
# update() it will update or to change 