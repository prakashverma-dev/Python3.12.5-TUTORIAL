'''   

# Left Rotate the array by D-place -

D-places --> means 1 place or, 2 place or 3 place from left side.

arr [] = [1,2,3,4,5,6,7] ; 

For d = 2 --> [3,4,5,6,7,1,2]
For d = 3 --> [4,5,6,7,1,2,3]
For d = 7 --> [1,2,3,4,5,6,7] again come back to same place.(7 is the size of array.)

For d = 8 --> 7 + 1 means only after 7 rotation my array gets same and one rotation I have to do.
[2,3,4,5,6,7, 1] 

For d = 9 --> 7 + 2 means only two rotation I have to do.
[3,4,5,6,7, 1,2] 

For d = 15 --> 14 + 2 means only 1 rotation I have to do.
[2,3,4,5,6,7, 1] 

Hence, It is goes with multiple of 7 rotation will alwsy bring us to original array and remaining number only we have to do rotation.





# Brute Force Approch - [1,2,3,4,5,6,7]


size_of_arr = len(arr)    
d = d % (size_of_arr) # We updated the shiting number based on no of size of array.
Suppose d = 3

Step1 : Firstly will slice out firt d-element into a temp varibale -
for i in range(0, d):
    temp.append(arr[i])

OR, temp = arr[:d]

Step2 : Let' shift except first item to the left means 4th element on its first position -
for i in range(d, (n-1)+1):

    arr[i - d] = arr[i]

After step, our original array will look like : [4,5,6,7,5,6,7]


Step3 : Final step, to put back temp array in the end of original array -

j = 0
for i in range(n-d, n):

    arr[i] = temp[j]
    j += 1












'''

def leftRotateArrByD(arr, d):

    size_of_arr = len(arr)    
    d = d % (size_of_arr)

    # storing the initial shifting array element into temp array -
    temp = [] # [1, 2, 3]
    for i in range(0, d):
        temp.append(arr[i])

    # Now, Shifting to left -
    n = len(arr)
    for i in range(d, (n-1) + 1):

        arr[i-d] = arr[i]

    # Now, putting back to array right -
    j = 0
    for i in range(n-d, n):
        arr[i] = temp[j]
        j += 1

    return arr




d = 10
print(leftRotateArrByD([1,2,3,4,5,6,7], d))

# Time Complexity : -
# Time Complexity: O(n), We are performing a constant number of linear operations copying `k` elements and shifting up to `n-k` elements.

# Space Complexity: O(k) ,A temporary array of size `k` is used to store either the first `k` or last `k` elements depending on the direction of rotation.


# Optimal Solution(MOST EASY**): To optimized Space Complexity -
'''  
arr = [ 1,2,3,4,5,6,7] ; n = 7 and d = 3(rotate 3 step left)

resulantArr = [4,5,6,7,1,2,3]

Firstly try to consider Divide the array by d, then -
[1,2,3] [4,5,6,7]

Step1 : Reverse First half from (0 Index till d-1 index)  --> [3,2,1]  --> O(d)
Step2 : Reverse Second half from (d index till n-1 index) --> [7,6,5,4]  --> O(n-d)
[3,2,1] [7,6,5,4]

Step3(Final) : Reverse Complete Arry from (0 index till n-1 index) -->  O(n)
[4,5,6,7,1,2,3]  --> We get the resulant array.

Time Complexity = d  + (n-d)  + n = 2n --> O(2n) = O(n)
Space Complexity = O(1) we arnot using any extra space.


'''

def leftRotateByK(arr, k):

    n = len(arr)
    k = k % n # making k value smaller if in case it exceeds the size of the array to rotate.
    

    reverseArr(arr, 0, k-1)
    reverseArr(arr, k, n-1)
    reverseArr(arr, 0, n-1)

    return arr 

def reverseArr(arr, start, end):

    while start < end:

        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1

arr = [1,2,3,4,5,6,7]
k = 10
print(leftRotateByK(arr, k))




