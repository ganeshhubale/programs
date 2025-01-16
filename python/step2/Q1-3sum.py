# 3 sum

# Steps:
# - Sort the array
# - fix the first element
# - have 2 pointers left and right
# - with fix pointer travel with left and right pointers to find perfect triplet
# - avoid duplicates of triplets by updating left and right pointer if it matches with previous
# - avoid fix element duplication with its increament if it is same as previous

def threeSum(nums):
    # sort the array in ascending order

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
    
    pairs = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                pairs.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1

                # skips duplicates for 2nd and 3rd element
                while left < right and nums[left] == nums[left-1]:
                    left+=1
                while left < right and nums[right] == nums[right+1]:
                    right-=1
            
            elif current_sum < 0:
                left+=1
            elif current_sum > 0:
                right-=1
                        
    return pairs


# Example Usage:
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

# Time complexity: O(n3)
# Space complexity: O(k) where k are the triplets in array
