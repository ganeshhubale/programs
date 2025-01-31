# Merge Strings Alternately
#     - You are given two strings, word1 and word2.
#     Merge the two strings by adding letters in alternating order, starting with word1.
#     If a string is longer than the other, append the additional letters at the end.

# word1 = "abc"
# word2 = "pqr"
# Output: "apbqcr"
# Merge alternately: "a" + "p" + "b" + "q" + "c" + "r" → "apbqcr"

# Two pointer
def mergealter(word1, word2):

    if not word2:
        return word1
    elif not word1:
        return word2

    i = 0
    j = 0
    output = []
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            output.append(word1[i])
            i += 1

        if j < len(word2):
            output.append(word2[j])
            j+=1

    return ''.join(output)

print(mergealter("abc", "pqrs")) # apbqrs

# Time complexity: O(n+m)
# Space complexity: O(n+m)