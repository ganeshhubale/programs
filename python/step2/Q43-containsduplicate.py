# Contains Duplicate
#     - The "Contains Duplicate" problem asks if there are any duplicate elements in an array.
#     - Given an integer array nums, return True if any value appears at least twice in the array, 
# and False if every element is distinct.


# Hash

def containsDuplicate(nums):

    map = {}
    for num in nums:
        map[num] = map.get(num, 0) + 1
        if map[num] > 1:
            return True
    return False



nums = [1, 2, 3, 4, 5]
print(containsDuplicate(nums))

# Time complexity: O(n)
# Space complexity: O(n)


# with Set
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test case
nums = [1, 2, 3, 4, 5]
print(containsDuplicate(nums))  # Output: True


# Time complexity: O(n)
# Space complexity: O(n)