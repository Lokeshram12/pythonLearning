def square(number):
    return  number**2

ans=square(4)
print(ans)

def sum(a,b):
    return a+b

ans=sum(4,5)
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