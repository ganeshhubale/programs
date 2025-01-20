# Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic 
# if the characters in one string can be replaced to get the other string, preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

def is_isomorphic(s, t):

    if len(s) != len(t):
        return False
    
    s_t_dict = {}
    t_s_dict = {}

    for i in range(len(s)):
        if s[i] in s_t_dict:
            if s_t_dict[s[i]] != t[i]:
                return False
        else:
            s_t_dict[s[i]] = t[i]
        
        if t[i] in t_s_dict:
            if t_s_dict[t[i]] != s[i]:
                return False
        else:
            t_s_dict[t[i]] = s[i]
    return True

print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
print(is_isomorphic("paper", "title"))  # True
print(is_isomorphic("abcd", "aaaa"))  # False
print(is_isomorphic("ab", "aa"))  # False
print(is_isomorphic("", ""))  # True

# Time complexity: O(n)
# Space complexity: O(1) as the size of the hash maps depends on the number of 
# unique characters, which is limited to the size of the alphabet.