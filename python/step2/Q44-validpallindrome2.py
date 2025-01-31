# Valid Palindrome II
# Given a string s, return True if it can be a palindrome after deleting at most one character.

# s = "abca"
# By removing "b" or "c", the string becomes "aca" or "aba", which are palindromes.

# Approach: Two Pointers (Greedy)
# Steps
# Use two pointers (left, right) to check for a palindrome.
# If a mismatch is found:
# Try removing either character (s[left] or s[right]).
# Check if the remaining substring is a palindrome.
# If the loop completes without mismatches, return True.

def isPalindrome(s, left, right):
    """ Helper function to check if a substring is a palindrome. """
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:  # Found a mismatch
            # Try removing one character (either left or right)
            return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1)
        left += 1
        right -= 1

    return True  # If no mismatch found, it's already a palindrome

print(validPalindrome("abca"))       # Expected Output: True
print(validPalindrome("racecar"))    # Expected Output: True
print(validPalindrome("abc"))        # Expected Output: False
print(validPalindrome("deeee"))      # Expected Output: True
print(validPalindrome("a"))          # Expected Output: True
print(validPalindrome("ab"))         # Expected Output: True
print(validPalindrome("abcdba"))     # Expected Output: True
print(validPalindrome("abcdef"))     # Expected Output: False


# Time: O(N): We scan the string at most twice.
# Space: O(1): No extra space is used.
