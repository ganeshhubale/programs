# Jump Game
#     - The Jump Game is a popular algorithmic problem that can be solved using greedy algorithms.
#     - You are given an array of non-negative integers nums, where each element represents your 
# maximum jump length at that position. 
# Your task is to determine if you can reach the last index starting from the first index.

# Example:
# Input:
# nums = [2, 3, 1, 1, 4]

# Output:
# true

# Explanation:
# Start at index 0, with value 2. You can jump to index 1 or 2.
# From index 1 (value 3), you can jump to index 2, 3, or 4.
# Finally, you can reach the last index.

# Greedy Algorithm

def canJump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, nums[i] + i)
    return True

nums = [2, 3, 1, 1, 4, 8, 9]
print(canJump(nums))

# Time complexity: O(n)
# Space Complexity: O(1)