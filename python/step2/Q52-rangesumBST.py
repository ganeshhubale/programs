# Range Sum of Binary search tree
#     - Given the root of a Binary Search Tree (BST) and two integers low and high, return 
# the sum of all values of nodes with values in the inclusive range [low, high].

# 1. input
#         10
#        /  \
#       5   15
#      / \    \
#     3   7    18
# low = 7, high = 15

# output - 32

# Explaination - The values within the range [7,15] are {7, 10, 15}. Their sum is 7 + 10 + 15 = 32.


# 2. Input
#         10
#        /  \
#       5   15
#      / \   / \
#     3   7 13 18
#    /   /
#   1   6
# low = 6, high = 10

# output - 23
# Explaination -  The values within the range [6,10] are {6, 7, 10}. Their sum is 6 + 7 + 10 = 23.

# recusrive depth first search

class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right
    
def recursiveDFS(root, low, high):

    if not root:
        return 0
    
    sum = 0

    if root.val < low:
        sum += recursiveDFS(root.right, low, high) # Go right side
    
    if low <= root.val <= high:
        sum +=  root.val 
        sum += recursiveDFS(root.left, low, high)
        sum += recursiveDFS(root.right, low, high)
        # keep suming recurisively with left and right node

    if root.val > high:
        sum += recursiveDFS(root.left, low, high) # go left

    return sum


# # Creating BST manually
node1 = TreeNode(10, 
                TreeNode(5, 
                        TreeNode(3), 
                        TreeNode(7)
                        ), 
                TreeNode(15)
                )

print(recursiveDFS(node1, 7, 15)) # Expected Output: 32 (7 + 10 + 15)

# Time complexity: O(n)
# Space complexity: O(n) to main recurive stack