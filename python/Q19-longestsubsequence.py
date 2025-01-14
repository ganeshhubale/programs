#. Find the longest common subsequence.
# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

def longest_common_subsequence(text1, text2):
    """
    Find the length of the longest common subsequence between two strings.
    :param text1: First string
    :param text2: Second string
    :return: Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    # Initialize a 2D DP table with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # Match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # No match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS string
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:  # Characters match
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
            i -= 1
        else:  # Move left
            j -= 1

    # Reverse the LCS because we collected it backwards
    lcs.reverse()

    return dp[m][n], "".join(lcs)  # The LCS length

# Test case 1
text1 = "abcde"
text2 = "ace"
print(f"LCS length: {longest_common_subsequence(text1, text2)}")  # Output: 3 ("ace")

# Test case 2
text1 = "abc"
text2 = "def"
print(f"LCS length: {longest_common_subsequence(text1, text2)}")  # Output: 0 (no common subsequence)

# Test case 3
text1 = "abcdef"
text2 = "abdf"
print(f"LCS length: {longest_common_subsequence(text1, text2)}")  # Output: 4 ("abdf")

# Time complexity - O(m*n)
# Space complexity - O(m*n)