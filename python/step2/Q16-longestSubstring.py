#  Longest Substring Without Repeating Characters
# - Given a string s, find the length of the longest substring without repeating characters.
# Sliding Window

def longest_substring_without_repeating_char(s):

    # Get a dict to store last index of each char
    char_index_map = {}
    # start the sliding window
    start = 0
    max_length = 0 # max lenth of substring

    for end in range(len(s)):
        char = s[end]
        print("infor end -> ", end)
        # if the char is already in map and within the current window
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
            print("start ->", start)
        
        # update the char's last seen index
        char_index_map[char] = end
        print(char_index_map)
        # update the max length
        max_length = max(max_length, end-start+1)
        print("max length: ", max_length)

    return max_length

s = "abffcdh"
print(longest_substring_without_repeating_char(s))

# Time complexity: O(n)
# Space complexity: O(min(n, a)) -> 
# n length of string and a is size of char set (e.g. 26 for lower case english letters)