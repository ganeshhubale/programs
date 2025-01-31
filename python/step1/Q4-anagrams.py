# Q4: Write a python function to check if two strings are anagrams of each other.

string1 = "listen"
string2 = "silent"

def checkAnagrams(string1, string2):

    if len(string1) !=  len(string2):
        return "Given strings are not anagrams."
    
    charDict = {}

    for char in string1:
        charDict[char] = charDict.get(char, 0) + 1
    for char in string2:
        if char in charDict:
            charDict[char] = charDict[char] - 1
            if charDict[char] == 0:
                del charDict[char]

        else: return "Given strings are not anagrams."
    if not charDict:
        return "Given strings are anagrams."
    return "Given strings are not anagrams."

print(checkAnagrams(string1, string2))

# Time complexity - O(n)
# Space complexity - O(k), where k is the number of unique characters in the string.