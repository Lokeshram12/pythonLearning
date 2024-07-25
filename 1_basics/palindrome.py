def is_palindrome(inp):
    for i in range(len(inp) // 2):
        if inp[i] != inp[len(inp) - i - 1]:
            return False
    return True
