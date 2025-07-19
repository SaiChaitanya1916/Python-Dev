# input:-[10,20,30,40,50]
# output:-sum of the list:-150

l = [10,20,30,40,50]
sum = 0
for i in l:
    sum+=i
print(sum)

# input:-15,2,7,25,10
# output:- maximum = 25 ,minimum = 2


l =[15,2,7,25,10]
l.sort()

print(l[0])
print(l[-1])

# input :- 10,20,30,20,30,40,50
# output :- 10,20,30,40,50  remove all duplicate in list
# Method 1

inp = input().split(',')
l =[int(item) for item in inp]

newl =[]

for i in l:
    if i in newl:
        continue
    else:
        newl.append(i)
print(newl)

# Method 2

inp = input().split(',')
l ={int(item) for item in inp}
newl = list(l)
print(newl)

# input:-[2,3,4,5,6,2,3,2] repated num
# output:-[count of repated num ]
inp = (input()).split(',')
l =[int(a) for a in inp]
n = int(input("Enter n: "))
num =l.count(n)
print(f"count of {n} :- {num}")

# input: SetA:{1,2,3,4,5}
#        setB:{4,5,6,7,8}
# output: intersection:{4,5}
#        union{1,2,3,4,5,6,7,8}

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

unionset = set_a.union(set_b)
intersectionset = set_a.intersection(set_b)

print(f"union:-{unionset}")
print(f"intersection:-{intersectionset}")


# Dictionary
my_dict = {}
a = input("Enter name:- ")
b = int(input("Enter age:-"))
c = input("Enter location:-")

my_dict["name"] = a
my_dict["age"] = b
my_dict["location"] = c

print(my_dict)

# Through iterate
for i,j in my_dict.items():
    print(i,j)