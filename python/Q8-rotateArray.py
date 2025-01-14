# Implement an algorithm to rotate an array.

def rotateArray(arr, k):
    i,j=0,len(arr)-1
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
    i, j = 0, k-1 
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i+= 1
        j -=1
    
    i, j = k, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -=1

    return arr

print(rotateArray([1,2,3,4,5,6], 2))