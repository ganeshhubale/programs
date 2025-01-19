# Contains Duplicate
# - Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def contains_duplicate(nums):

    elementCount = {}
    dupValues = []
    for i in nums:
        elementCount[i] = elementCount.get(i, 0) + 1
        if elementCount[i] > 1:
            dupValues.append(i)
    return f"Found duplicate elements {dupValues}"



nums = [1,2,3,4,1,4,5]
print(contains_duplicate(nums))

# Time complexity: O(n)
# Space complexity: O(n) for dictionary