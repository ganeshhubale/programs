# Find First and Last Position of Element in Sorted Array
#     - The "Find First and Last Position of Element in Sorted Array" problem requires locating the first and last indices of a given target value in a sorted array. 
#     If the target is not found, return [-1, -1].


# Input:

# A sorted array nums.
# An integer target.
# Output:

# An array [first_position, last_position], where:
# first_position is the index of the first occurrence of target.
# last_position is the index of the last occurrence of target.

# Steps:
# Use binary search twice:
# First binary search to find the first occurrence of the target.
# Second binary search to find the last occurrence of the target.
# If the target is not found, return [-1, -1].


def searchRange(nums, target):
    def findOccurence(isFirst):
        bound = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                # update bound
                bound = mid
                if isFirst:
                    right = mid -1  # Narrow to the left for the first position
                else:
                    left = mid + 1 # Narrow to the right for the last position
            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return bound
    
    frist_occurence = findOccurence(isFirst=True)
    if frist_occurence == -1:
        return [-1, -1]
    last_occurence = findOccurence(isFirst=False)

    return [frist_occurence, last_occurence]

# Example Usage
print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1, -1]
print(searchRange([], 0))                   # Output: [-1, -1]

# Time complexity: O(log n)
# Space complexity: O(1)