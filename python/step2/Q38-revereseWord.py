# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The input string may contain leading or trailing spaces, 
# and multiple spaces between words. Ensure that the result 
# string has only a single space separating words, with no leading or trailing spaces.

# Input:
# s = " hello world "

# Output:
# "world hello"

def reverseWord(str):

    words = str.split()

    reverseList = words[::-1]

    return ' '.join(reverseList)

print(reverseWord("   Hello   World  "))

# Time Complexity: O(n)
# Space Complexity: O(n)


def reverseWords(s):
    result, word = [], []
    for char in s:
        if char != " ":  # Collect characters for the current word
            word.append(char)
        elif word:  # Add the word to the result when a space is encountered
            result.append("".join(word))
            word = []
    if word:  # Add the last word if it exists
        result.append("".join(word))
    return " ".join(result[::-1])  # Reverse the list and join with a single space

# Example
s = "  hello world  "
print(reverseWords(s))  # Output: "world hello"

# Time Complexity: O(n)
# Space Complexity: O(n)