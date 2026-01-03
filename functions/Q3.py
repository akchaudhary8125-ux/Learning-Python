"""Write a recursive function is_palindrome(s) that:
Returns True if a string is a palindrome
Returns False otherwise
Does not use loops
Is case-insensitive"""


def is_palindrome(s):
    s = s.strip().lower()


    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

print(is_palindrome("hello"))
print(is_palindrome("madam"))