'''   
# Check if Array is Sorted if yes return True and if not return false -

arr = [1, 2, 2, 3, 3, 4]  --> True
arr = [1, 2, 1, 3, 4]  --> False

# algo : Run loop from 0 to n-2 till and check current element with next elment till n-2 elememt and if at any point next element is smaller than current element return false thus array is not sorted.

Time Complexity : O(n)
'''

def isArraySorted(arr):
    n = len(arr)
    for i in range(0, (n-2) +1 ):

        if arr[i] > arr[i+1]:
            return False
    
    return True

print(isArraySorted([1, 2, 2, 3, 3, 4]))
print(isArraySorted([1, 2, 1, 3, 4])) 

# Time Complexity : O(n)
