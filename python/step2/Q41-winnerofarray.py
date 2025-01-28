# Find the Winner of an Array Game
#     - The "Find the Winner of an Array Game" problem involves finding the winner in a game based on comparisons within an array.

# Problem Description:
# Given an integer array arr of distinct integers, a game is played as follows:

# The first element of the array is the current champion (winner).
# The champion competes with the next element in the array:
# If the champion is greater, it retains its title.
# Otherwise, the next element becomes the new champion.
# The process continues until:
# Either the champion wins k consecutive rounds, or
# The end of the array is reached.
# Goal: Return the champion when one of these two conditions is met.


# Approach:
# Use two variables:

# current_champion: Tracks the current champion.
# win_count: Tracks how many consecutive rounds the current champion has won.
# Traverse through the array:

# Compare current_champion with the next element.
# Update current_champion and reset/increment win_count accordingly.
# Stop early if win_count == k.

def getWinner(nums, k_rounds):

    win_count = 0
    champ = nums[0]

    for i in range(1, len(nums)):
        if champ > nums[i]:
            win_count += 1
        else:
            champ = nums[i]
            win_count = 1

        if win_count == k:
            return champ
        
    # If no one wins k rounds, return the maximum element
    return champ

# Test case
nums = [2, 1, 3, 5, 4, 6, 7]
k = 2
print(getWinner(nums, k))  # Output: 5

# Time Complexity: O(n), where 𝑛 is the length of the array. We traverse the array once.
# Space Complexity: O(1), as no additional data structures are used.
