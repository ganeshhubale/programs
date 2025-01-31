# Longest Common Subsequence
# The Longest Common Subsequence (LCS) problem is to find the length of the longest subsequence common 
# to two strings. A subsequence is a sequence derived from another sequence by deleting some elements 
# without changing the order of the remaining elements.

# Steps to Create the Program:
# Understand the Problem

# We need to find the longest sequence of characters that appear in both strings in the same order (not necessarily contiguous).
# Approach: Dynamic Programming (Bottom-Up Table)

# Define dp[i][j] as the length of LCS of the first i characters of text1 and first j characters of text2.
# If text1[i-1] == text2[j-1], then dp[i][j] = dp[i-1][j-1] + 1
# Else, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# Base case: dp[0][j] = 0 and dp[i][0] = 0 (empty string case).
# Implement the DP Table

# Create a 2D table dp[m+1][n+1] where m and n are lengths of text1 and text2.
# Iterate through both strings and fill the table.
# Retrieve the Result

# The bottom-right cell dp[m][n] contains the length of the LCS.

def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    
    # Create a 2D DP array initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:  # If characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # If characters do not match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]  # The length of LCS is in the last cell

# Time complexity: O(m × n)	
# Space complexity: O(m × n)
