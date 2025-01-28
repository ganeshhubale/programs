# H-Index
#     - The H-Index is a metric that quantifies the productivity and citation impact of a 
# researcher based on their publications.
#     - Given an array citations where each element represents the number of citations for 
# a specific paper, determine the H-Index for the researcher.
#     - The H-Index is defined as the maximum value of h such that the researcher has at least
#  h papers with h or more citations, and the rest have no more than h citations.


# Example:
# Input 1:
# citations = [3, 0, 6, 1, 5]

# Output 1:
# 3

# Explanation:
# The researcher has 5 papers with citation counts: [3, 0, 6, 1, 5].
# If we sort the citations in descending order: [6, 5, 3, 1, 0].
# The H-Index is the highest number h such that there are at least h papers with h or more citations:
# 1 paper has ≥ 1 citation.
# 2 papers have ≥ 2 citations.
# 3 papers have ≥ 3 citations. (This is the H-Index.)
# 4 papers do not have ≥ 4 citations.


# Sorting-Based Approach:

def HIndex(citations):
    citations.sort(reverse=True)  # Sort citations in descending order
    
    h_index = 0

    for i in range(len(citations)):
        if citations[i] >= i+1:
            h_index += 1
        else:
            break
    return h_index

citations = [3, 0, 6, 1, 5]
print(HIndex(citations))


# Time Complexity: O(n log n) (for sorting)
# Space Complexity: O(1) (no extra space needed)