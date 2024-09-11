#  Write a Python function to check if a string is a palindrome.
#  Write a Python function to remove duplicates from a list while maintaining the original order.

#  Write a Python function to generate the Fibonacci sequence up to `n` terms.

def fib(n):
    if n==0 or n==1:
        return n
    else:
         return fib(n-1)+fib(n-2)

ans = fib(3)
print(ans)

#  Write a Python function to find common elements between two lists.

# List: Ordered, mutable, allows duplicates. Use it when you need a collection where elements can be modified and order matters.
# Set: Unordered, mutable, no duplicates. Use it when you need a collection of unique elements and don’t care about the order.
# Tuple: Ordered, immutable, allows duplicates. Use it when you need a fixed collection of elements that should not be changed and need to maintain their order.


def common(list1,list2):
    set1=set(list1)
    set2=set(list2)
    return list(set1.intersection(set2))

list1 = [1,2,3,4]
list2 = [3,4,5]

ans = common(list1, list2)

print(ans)
