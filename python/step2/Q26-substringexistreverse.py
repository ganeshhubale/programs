# Existence of a Substring in a String and Its Reverse

# To check whether a substring exists in a string and also in its reverse, here is the explanation and implementation:

# Given a string s and a substring sub, determine if:
# sub exists in s.
# sub exists in the reverse of s.

def check_substring_in_reverse(s, sub):

    sub_in_original_string = sub in s

    reverse_str =  s[::-1]
    sub_in_reverse_string = sub in reverse_str

    return sub_in_original_string and sub_in_reverse_string

print(check_substring_in_reverse("abcde", "bcd"))  # Output: fasle
print(check_substring_in_reverse("hello", "oll"))  # Output: False
print(check_substring_in_reverse("abcba", "abc"))  # Output: True

# Time complexity: O(n+m)
# n is the length of s.
# m is the length of sub.

# space complexity: O(n)  for reversing s.