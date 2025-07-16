# Example 1
l = [2,5,6,"Pavana","Chaitu","kusu"]

print(l[::-1])
print(l[1:4:])

# Example 2

list_name = [2,5,6,"Pavana","Chaitu","kusu"]
list_name[3] = 30


list_name.append(11)   #Adds an element to the end of the list
list_name.insert(0,1)  #inserts an element at a specific of a specified element.
list_name.remove(2) # Removes and return the element at a specified index
print(list_name.index("Chaitu")) # returns the index of the first occurrence of a specified element

print(list_name)

# Example 3 List concatentation 

list1 = [4,5,7]
list2 = [8,10,3]

listcon = list1+list2
print(listcon)

# Example 4 List comprehensions,provides a concise way to create lists using single line of code
squares = [x**2 for x in range(1,6)]
print(squares)
