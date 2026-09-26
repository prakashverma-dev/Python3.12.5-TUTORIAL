def twosum(arr, target):

    n = len(arr)

    for i in range(n):

        # found = False
        for j in range(i+1, n):

           if arr[i] + arr[j] == target :
                return True

        
        
    return False
    
        
arr = [1,2,5,6,7]
# target = 10
target = 7
print(twosum(arr, target))

# Time Complexity : O(n^2)