# Shortest String That Contains Three Strings
# You are given three strings a, b, and c. Your task is to find the shortest 
# string that contains all three strings as substrings. 
# If there are multiple results of the same length, return any one of them.

# Not understood

from itertools import permutations

def shortest_superstring(a, b, c):
    # Helper function to calculate overlap between two strings
    def get_overlap(s1, s2):
        max_overlap = 0
        # Check suffix of s1 with prefix of s2
        for i in range(1, min(len(s1), len(s2)) + 1):
            if s1[-i:] == s2[:i]:
                max_overlap = i
        return max_overlap

    # Helper function to merge two strings based on overlap
    def merge_strings(s1, s2):
        overlap = get_overlap(s1, s2)
        return s1 + s2[overlap:]

    # Try all permutations of the strings
    strings = [a, b, c]
    shortest = None

    for perm in permutations(strings):
        # Combine the three strings in this order
        merged = merge_strings(merge_strings(perm[0], perm[1]), perm[2])
        if shortest is None or len(merged) < len(shortest):
            shortest = merged

    return shortest

# Example Usage
a = "abc"
b = "bca"
c = "cab"

print(shortest_superstring(a, b, c))  # Output: "abcabca" (or any equivalent)
