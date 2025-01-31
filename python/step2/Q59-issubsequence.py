# Is Subsequence
#     - Given two strings s and t, return True if s is a subsequence of t, or False otherwise.

#     A subsequence of a string is a sequence that appears in the same relative order, but not 
# necessarily consecutively. 
# s consists only of lowercase English letters.
# t consists only of lowercase English letters.


# input
s = "abc"
t = "ahbgdc"
# output: True
# The characters "abc" appear in "ahbgdc" in the same order.

# Two pointer

def isSubsequence(s, t):

    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i +=1
        j+=1

    return i == len(s) # If j reaches the end of t but i is not finished, return False.

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
print(isSubsequence("abc", "ahbgdc"))  # Expected Output: True
print(isSubsequence("axc", "ahbgdc"))  # Expected Output: False
print(isSubsequence("", "ahbgdc"))     # Expected Output: True (Empty string is always a subsequence)
print(isSubsequence("abc", ""))        # Expected Output: False
print(isSubsequence("abc", "abc"))     # Expected Output: True
print(isSubsequence("b", "abc"))       # Expected Output: True



# Time Complexity: O(N + M) because we scan both strings once.
# Space Complexity: O(1) space because we use two integer variables.


# N = len(s), M = len(t)

