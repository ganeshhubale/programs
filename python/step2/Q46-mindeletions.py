# Minimum Deletions to Make Character Frequencies Unique

# The "Minimum Deletions to Make Character Frequencies Unique" problem is a greedy algorithm problem on LeetCode.

# s = "aabb"
# 'a' appears twice, 'b' appears twice.
# Deleting one 'b' (or 'a') makes the frequencies unique: "aab" or "abb".


# Greedy with Sorting
# Steps
# Count character frequencies using collections.Counter.
# Sort the frequencies in descending order.
# Iterate over the list, ensuring no two frequencies are the same:
# If a frequency already exists, decrease it (by deleting characters).
# Track deletions needed.


from collections import Counter

def minDeletions(s: str) -> int:
    freq = Counter(s)  # Count character frequencies
    freq_values = sorted(freq.values(), reverse=True)  # Sort in descending order
    
    deletions = 0
    seen_frequencies = set()

    for f in freq_values:
        while f > 0 and f in seen_frequencies:  # Adjust duplicate frequencies
            f -= 1
            deletions += 1
        seen_frequencies.add(f)  # Store unique frequency

    return deletions


print(minDeletions("aabb"))       # Expected Output: 1
print(minDeletions("aaabbbcc"))   # Expected Output: 2
print(minDeletions("ceabaacb"))   # Expected Output: 2
print(minDeletions("abc"))        # Expected Output: 0
print(minDeletions("aaabbbbcc"))  # Expected Output: 2
# Time: O(N log N) for frequency count.
#  Space: O(N) for sorting.
# O(N) for frequency count.
# O(N log N) for sorting.
# O(N) for tracking unique frequencies.

