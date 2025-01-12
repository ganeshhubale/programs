# Q3: Implement a function that finds all pairs in an array that sum up to a given target.

arr = [1,2,3,4,5,62,4,5,4,56,5]
def targetSum(arr, target):
    seen = set()
    pairs = set()
    for num in arr:
        difference = target - num
        if difference in seen:
            pairs.add((num, difference))
        seen.add(num)

    return pairs


print(targetSum(arr, 5))

# Time complexity  - O(n)
# O(n) - For iterating through the array
# O(1) - For adding to seen and pairs set

# Space complexity - O(n)
# O(n) for seen set
# O(n/2) for pairs set in worst case