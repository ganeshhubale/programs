# Print characters and their frequencies in order of occurrence
#     - Given a string, print each character and its frequency in the order of their first occurrence.

# Input: "aabbc"
# Output:
# a 2
# b 2
# c 1

def freqOfChars(s):
    s = s.lower()

    freq_dict = {}
    for char in s:
        if char != ' ':
            freq_dict[char] = freq_dict.get(char, 0) + 1

    for char, count in freq_dict.items():
        if char:
            print(char, count)

freqOfChars("I am Software Testing")

# Time complexity: O(n)
# Space: O(k)