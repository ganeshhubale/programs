# Check if a string is a palindrome.

def pallindrome(s):

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


print(pallindrome("nayana"))

# Time complexity - O(n)
# Space complexity - O(1)