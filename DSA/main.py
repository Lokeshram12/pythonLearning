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
#  Write a Python function to check if a string is a palindrome.
#  Write a Python function to remove duplicates from a list while maintaining the original order.
#  Write a Python function to generate the Fibonacci sequence up to `n` terms.
#  Write a Python function to find common elements between two lists.