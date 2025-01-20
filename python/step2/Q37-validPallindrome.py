# Valid Palindrome


def valid_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())

    left = 0
    right = len(s) -1
    
    while left < right:

        if s[left] != s[right]:
            return f" {s} -> is not a pallindrome"
        left += 1
        right -= 1
    return f" {s} -> is a pallindrome"

print(valid_palindrome("Nayan2"))  # True
print(valid_palindrome("nayana"))  # False
print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))  # False

# Time complexity: O(n)
# Space compleixity: O(n) for processing string to remove spaces and convert to lowercase