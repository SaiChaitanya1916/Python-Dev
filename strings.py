str = "PYTHON"
print(str[-1])
print(str[1])
print(str[4])


str = "CHAITANYA"
print(str[0:5:2])   #string slicing :- Division of string several parts ,variablename[start:stop:step]
print(str[::2])
print(str[0::1])
print(str[0:4:])
print(str[0:-2:])
print(str[::-1])


 # string concatenation :- using the "+" operator
 # #   str1+str2


first_name = "Sai"
last_name = "Chaitanya"
full_name = first_name + " " + last_name
print(full_name)



# length of the string

name = "chaitanya"
print(len(name))



# Examples of Manipulation  of strings

s = "Hello world"

print(s.upper())   # Converts the string to upper case

print(s.lower())  # converts the string to lower case

print(s.strip())  # remove the leading and trailing witespaces from the string

print(s.replace('o','x'))  #replace all occurence of 'o' with 'x' in string

print(s.count('o'))  # count the occurence of 'o'