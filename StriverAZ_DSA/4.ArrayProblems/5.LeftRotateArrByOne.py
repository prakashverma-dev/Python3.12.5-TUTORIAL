'''    

# Left Rotate the array by one place -

arr [] = [1,2,3,4,5]
ans = [2,3,4,5,1]


# Algo -

temp = arr[0]
for(i = 1; i<n; i++){
        arr[i-1] = arr[i]
}

arr[n-1] = temp



'''
def rotateArray(arr):
    # Write your code from here.
    n = len(arr)
    temp = arr[0]

    for i in range(1, n):
        arr[i-1] = arr[i]

    arr[n-1] = temp

    return arr

# Time Complexity : O(N) 
# Space Complexity : O(1) as no extra space we are using, we inplace changing array valuues. 

