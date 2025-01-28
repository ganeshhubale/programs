# Find the Index of the First Occurrence of a substring in a String

# To find the index of the first occurrence of a substring in a string without using find(), you can use a loop to iterate through the string and compare substrings manually.

# Here’s how you can do it:

# Approach:
# Loop through the main string (haystack).
# For each position, check if the substring (needle) starts at that position.
# If found, return the index.
# If not found by the end of the string, return -1.

def firstOccurenceSub(mainString, substring):
    if not substring:
        return 0
    
    for i in range(len(mainString) - len(substring) + 1):
        if mainString[i: i + len(substring)] == substring:
            return i
    return -1

print(firstOccurenceSub("Hello", "ll"))

# Time complexity: O((n-m+1)*m) -> n is mainstring, m is substring
# Space complexity: O(1)