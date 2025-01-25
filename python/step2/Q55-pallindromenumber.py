#  Palindrome Number
#     - The Palindrome Number problem checks whether a given integer is a palindrome. 
# A palindrome is a number that reads the same backward as forward.
    

# Problem Statement
# Given an integer x, return true if x is a palindrome and false otherwise.

# Constraints:

# An integer is considered a palindrome when it reads the same backward as forward.
# Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes.

def pallindromeNumber(number):
    if number < 0 or not number:
        return False
    number = str(number)
    left , right  = 0, len(number) - 1

    while left <= right:
        if number[left] != number[right]:
            return False
        left +=1 
        right -=1
    return f"Given number {int(number)} is pallindrome."

print(pallindromeNumber(121))
print(pallindromeNumber(-131)) #false
print(pallindromeNumber(1221))
print(pallindromeNumber(89)) # false
print(pallindromeNumber(99))

# Time complexity: O(n)
# Space complexity: O(1)


def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):  # Negative numbers and non-zero multiples of 10
        return False
    
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # Compare the first half (x) and the reversed second half
    return x == reversed_half or x == reversed_half // 10

# Example
print(isPalindrome(121))  # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))  # Output: False

# Time Complexity: O(log 10 ^ x) as we process half the digits of x.
# Space Complexity: O(1).