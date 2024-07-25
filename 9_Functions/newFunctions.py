def square(number):
    return  number**2

ans=square(4)
print(ans)

def mul(p1,p2):
    return p1*p2
ans=mul('d',5)
print(ans)

import math
def circle_stats(r):
    area=math.pi * r**2
    circumference=2*math.pi*r
    return area,circumference

a,c=circle_stats(4)
print("Area: ",a,"Circumference: ",c)

#default parameter
def greet(name="User"): 
    return "Hello, " + name 

print(greet())

# lambda function

cube= lambda x:x**3
print(cube(4))

#  *args and *kwargs

def sum_all(*args):
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,5,4,))
print(sum_all(1,2,6,3,7,8,3))

# generator function that yields even numbers from a specified limit

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
for num in even_generator(10):
    print(num)

