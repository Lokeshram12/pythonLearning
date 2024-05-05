l1=[1,2,3]
l2=[1,2,3]
print(l1 ,l2)

l1[0]=44
print(l1 ,l2)

# below we sre using references as lists are immutable
l1=[1,2,3]
l2=l1
print(l1 ,l2)

l1[0]=44
print(l1 ,l2)


# [:] can be used to for copy of data
# copy module is also available



