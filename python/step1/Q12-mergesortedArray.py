# Merge two sorted arrays.

arr1 = [1,3,5]
arr2 = [2,4,4,6]

def mergesortedArrays(arr1, arr2):

    i = 0
    j = 0
    merged_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            merged_list.append(arr2[j])
            j += 1
        else:
            merged_list.append(arr1[i])
            i += 1
    # remaining element of array 1
    while i < len(arr1):
        merged_list.append(arr1[i])
        i += 1

    # remaining element of array 2
    while j < len(arr2):
        merged_list.append(arr2[j])
        j += 1

    return merged_list


print(mergesortedArrays(arr1, arr2))

# Time complexity - O(n+m) for array1+array2
# Space complexity - O(n+m) for elements stored in merged list
