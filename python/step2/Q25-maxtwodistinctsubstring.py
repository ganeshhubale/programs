# Maximum Length Substring With Two Occurrences
#     - To find the maximum length substring with exactly two distinct characters (also known as the "Longest Substring with Two Occurrences"), we can use a sliding window approach.
#     - Input: A string s.
#     - Output: The length of the longest substring that contains exactly two distinct characters.

# Did not get this
def longest_substring_two_distinct(s):
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Add the current character to the map
        char_map[s[right]] = char_map.get(s[right], 0) + 1
        print(char_map)
        # If we have more than 2 distinct characters, shrink the window
        while len(char_map) > 2:
            print(left, char_map[s[left]])
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                print(s[left])
                del char_map[s[left]]  # Remove the character completely if its count is 0
            left += 1
            print(left)

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length

# Test cases
print(longest_substring_two_distinct("abcabcbb"))  # Output: 4
# print(longest_substring_two_distinct("eceba"))     # Output: 3
# print(longest_substring_two_distinct("aabbcc"))    # Output: 4

# Time Complexity: O(n)
# Space Complexity: O(1)
