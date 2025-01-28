# Length of Last Word
#     - To find the length of the last word in a string

# Trim any extra spaces at the end of the string to avoid counting spaces.
# Split the string into words (separated by spaces).
# The last word in the list of words is the one we are interested in.
# Return the length of that word.


def lastWordLength(s):

    words = s.strip().split()

    return len(words[-1]) if words else 0

s = " my   name os ramehgs sfgfsgg slow   "
print(lastWordLength(s))
s = "    "
print(lastWordLength(s))

# Time complexity: O(n)
# Space complexity: O(n) for words