# Q5: Implement a function to determine the longest substring without repeating characters.

s = "abcdabc"

def longestSubstringwithoutrepeatingChars(s):

    i, j = 0, 0
    maxLength = 0
    longString = ""
    x = set()
    while j < len(s):
        if s[j] not in x:
            x.add(s[j])
            if maxLength < len(x):
                maxLength = len(x)
                longString = s[i:j+1]
            j += 1
        else:
            x.remove(s[i])
            i+=1

    return maxLength, longString


print(longestSubstringwithoutrepeatingChars(s))

# Time Complexity - O(n)
# Space complexity - O(n)