# finding an element that appears more than 25% of the time in a sorted array
# Key Idea
# Since the array is sorted:

# If an element appears more than 25% of the time, it must span across at least one contiguous subarray of length n/4.
# Thus, we can focus on checking indices spaced by n/4 to see if the same element occurs at those positions.

# Sliding window
# Check the element at every index i and compare it with the element at i + n/4.
# If they are the same, it's the answer.

def findElement(nums):

    n = len(nums)
    visiblity = n // 4

    for i in range(n - visiblity):
        if nums[i] == nums[i+visiblity]:
            return nums[i]
        
    return "Not found"


print(findElement([1,2,2,2,2,2,3,4,5,6,6,7,8]))
# Time complexity: O(n)
# Space complexity: O(1)


# hashmap

def findElement(nums):

    visibility = len(nums) // 4 # 25%
    hashMap = {}
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1

    for num, count in hashMap.items():
        if count >  visibility:
            return num
    return "Not found"

print(findElement([1,2,3,3,3,3,3,3,4,5,6,6,7,8]))

# Time complexity: O(n)
# Space complexity: O(n) for elements to store in hashmap
