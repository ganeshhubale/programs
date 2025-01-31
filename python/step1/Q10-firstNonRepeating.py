# Find the first non-repeating character in a string.

s = "aabbxyssdffghkldghklxy"

def firstNonRepeatingChar(s):
    charDict = {}

    for char in s:
        charDict[char] = charDict.get(char, 0) + 1

    for char in s:
        if charDict[char] == 1:
            return char
    return "No non-repeating character in a string"

print(firstNonRepeatingChar(s))

# Time complexity - O(n)
# Space complexity - O(n)