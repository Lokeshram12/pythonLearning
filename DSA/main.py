# Write a Python function to identify unique values in a list and return them as a new list.

def unique_values(listA):
    
    unique = list(set(listA))
    
    return unique

listA = [ 1,2,3,4,5,4,3,7,2]
unique_list = unique_values(listA)
print(unique_list)   #output : [1, 2, 3, 4, 5, 7]


#  Write a Python function to reverse a string.
#  Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#  Write a Python function to count the frequency of each character in a string using a dictionary.
#  Write a Python function to find the first non-repeating character in a string and return its index.
#  Write a Python function to reverse the digits of an integer.
def reverse_integer(n):
   
    is_negative = n < 0
    str_num = str(abs(n))

    reversed_str_num = str_num[::-1]
  
    reversed_num = int(reversed_str_num)
    
    if is_negative:
        reversed_num = -reversed_num
    
    return reversed_num


num1 = 12345
num2 = -67890

print(reverse_integer(num1))  # Output: 54321
print(reverse_integer(num2))  # Output: -09876 (which will be printed as -9876)
#  Write a Python function to check if a string is a palindrome.
#  Write a Python function to remove duplicates from a list while maintaining the original order.
#  Write a Python function to generate the Fibonacci sequence up to `n` terms.
#  Write a Python function to find common elements between two lists.