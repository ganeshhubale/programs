# Permutation in String
# The Permutation in String problem is a common question that involves 
# checking whether one string's permutation is a substring of another string.

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, one of s1's permutations is the substring of s2.

# Sliding Window with Frequency Count

def permutation_string(s1, s2):
    if len(s1) > len(s2):
        return False

    target_count = {}
    # Fequency count for s1
    for i in range(len(s1)):
        target_count[s1[i]] = target_count.get(s1[i], 0) + 1
    
    # Frequency count for initial window in s2
    windo_count = {}
    for i in range(0, len(s1)):
        windo_count[s2[i]] = windo_count.get(s2[i], 0) + 1
    
    if target_count == windo_count:
        return True
        
    # Slide the window over s2
    for i in range(len(s1), len(s2)):
        # add the new charactor to window
        windo_count[s2[i]] = windo_count.get(s2[i], 0) + 1

        # Remove the char thats no longer in window
        windo_count[s2[i-len(s1)]] -=1

        # Clean up zero counts
        if windo_count[s2[i-len(s1)]] == 0:
            del windo_count[s2[i-len(s1)]]

        # compare counts
        if target_count == windo_count:
            return True
    return False

s1 = "aabb"
s2 = "eidbaoooabbaa"
print(permutation_string(s1, s2))

# Time complexity: O(n)
# Space complexity: O(1) -> as the size of the frequency count dictionaries is bounded by 
# the number of unique characters (26 for lowercase English letters).