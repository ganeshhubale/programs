# Longest Palindromic Substring
# - Given a string s, find the longest substring in s that is a palindrome.
# A palindrome is a string that reads the same forward and backward.

# Dynamic programming

def longest_palindromic_substring(s):

    if (len(s)) <= 1:
        return s
    
    LPS = ""

    for i in range(1, len(s)):

        # start at odd length i.e. 1
        low = i
        high = i
        while s[low] == s[high]:
            low -= 1
            high +=1
            if low == -1 or high == len(s):
                break
        
        current_pal_string = s[low+1:high]

        if len(current_pal_string) > len(LPS):
            LPS = current_pal_string
        
        # consider checking with even length i.e 0
        low = i - 1
        high = i

        while s[high] == s[low]:
            low -= 1
            high += 1

            if low == -1 or high == len(s):
                break
        
        current_pal_string = s[low+1:high]

        if len(current_pal_string) > len(LPS):
            LPS = current_pal_string

    return LPS

print(longest_palindromic_substring("EBBABAD"))
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))   # Output: "bb"
print(longest_palindromic_substring("a"))      # Output: "a"
print(longest_palindromic_substring("ac"))     # Output: "a" or "c"
print(longest_palindromic_substring("forgeeksskeegfor"))  # Output: "geeksskeeg"

# Time complexity: O(n^2)
# Space complexity: O(1)