#  Product of Array Except Self
# - You are given an integer array nums of length n, where 𝑛 ≥ 2. Return an array answer such that answer[i] is 
# equal to the product of all the elements of nums except nums[i].

def product_array_except_self(nums):
    result = []
    n = len(nums)
    if n < 2:
        return result
    
    for i in range(n):
        j = 0
        product = 1
        while j < n:
            if j != i:
                product = product * nums[j]
            j += 1
        result.append(product)
    return result

nums = [0, 0, 0]
print(product_array_except_self(nums))

# Time complexity: O(n^2)
# Space complexity: O(n)


# Optimized solution

def product_array_except_self(nums):
    result = []
    n = len(nums)
    if n < 2:
        return result
    
    for i in range(n):
        j = 0
        product = 1
        while j < n:
            if j != i:
                product = product * nums[j]
            j += 1
        result.append(product)
    return result

nums = [0, 0, 0]
print(product_array_except_self(nums))

# Time complexity: O(n)
# Space complexity: O(n)

def product_array_except_self(nums):
    n = len(nums)
    if n < 2:
        return []
    
    result = [1] * n

    # Calculate prefix product in the result array
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Calculate suffix product and multiply it with the result array
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Example Usage
nums = [1,2,3]
print(product_array_except_self(nums))

# one more solution.
def product_array_except_self(nums):
    n = len(nums)
    if n < 2:
        return []
    
    # Initialize arrays to store prefix and suffix products
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    # Compute prefix product
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Compute suffix product
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Compute the result by multiplying prefix and suffix
    for i in range(n):
        result[i] = prefix[i] * suffix[i]
    
    return result

# Example Usage
nums = [0, 0, 0]
print(product_array_except_self(nums))

