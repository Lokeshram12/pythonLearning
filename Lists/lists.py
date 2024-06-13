l2= [1,2,3]
l2.append("hi")
l2.pop()
for i in l2:
    
    print(i,end="-")

if "3" in l2:
    print("true")
else:
    print("false")
# remove

# insert

# append

# list comprehension

square_num= [x**2 for x in range(10)]

print(square_num)

# =,copy()->shallow copy not good for nested lists,deepcopy()->works for all types of lists

list=[10,20,30,47]

print(list[0:2])

# .sort()  , sorted(array)