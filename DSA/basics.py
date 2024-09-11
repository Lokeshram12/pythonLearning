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