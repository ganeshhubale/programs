# Number of Substrings Containing All Three Characters
#     - You are given a string s consisting of the characters 'a', 'b', and 'c'. Your task is to 
# find the number of substrings 
# that contain at least one occurrence of each of the characters 'a', 'b', and 'c'.

# Sliding Window

def count_substrings(s):

    countMap = {"a": 0, "b": 0, "c": 0}
    count = 0
    left = 0

    for right in range(len(s)):

        if s[right] in countMap:
            countMap[s[right]] = countMap[s[right]] + 1

        while countMap["a"] > 0 and countMap["b"] > 0 and countMap["c"] > 0:
            count = count + (len(s) - right)
            if s[left] in countMap:
                countMap[s[left]] -= 1
            left += 1
    return count

print(count_substrings("abcabc"))

# Time complexity: O(n)
# Space complexity: O(1) dictionary since it only stores counts of 'a', 'b', and 'c'.