# Candy
#     - The Candy problem is a classic greedy algorithm problem. Let me explain the problem, the approach, and an example in detail.
#     - There are n children standing in a line, and each child is assigned a rating value (an integer). You need to distribute candies to the children such that:

#     - Each child gets at least 1 candy.
#     - A child with a higher rating than their neighbors must get more candies than their neighbors.
#     - You need to determine the minimum number of candies required.


# Approach
# The problem can be solved using a two-pass greedy algorithm:

# Left-to-right pass:
# Compare each child with their left neighbor. 
# If the current child's rating is greater than their left neighbor, give them one more candy than 
# their left neighbor.

# Right-to-left pass:
# Compare each child with their right neighbor. 
# If the current child's rating is greater than their right neighbor, ensure they have more candies than 
# the right neighbor (but also keep the result from the first pass).

# Steps
# Create a candies array where each child starts with 1 candy (since every child gets at least 1 candy).
# Perform the left-to-right pass to ensure the increasing ratings condition is met.
# Perform the right-to-left pass to ensure the decreasing ratings condition is met.
# Sum up the candies array to get the minimum candies required.

# greedy algorithm

def candy(ratings):

    # Give atleast 1 candy to each 
    n = len(ratings)
    candies = [1] * n

    # left to righ pas
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # right to left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)

ratings = [1, 0, 2]
print("total candy needed: ", candy(ratings))
ratings = [1, 2, 3]
print("total candy needed: ", candy(ratings))

# Time complexity: O(1)
# Space complexity: O(n) for candies