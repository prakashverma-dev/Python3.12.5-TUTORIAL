'''
# Selection sort
# Bubble sort
# Insertion sort all takes O(N^2) Time Complexity.


# Merge Sort : Much More Optimized Sorting Algorithm to sort Numbers, Character, Strings.

MErge Sort ----> Algorithm means Divide and Merge.

Lets consider array of size 5 -

[3, 2, 4, 1, 3] ---> Divide [3, 2 ,4] and [1, 3]

low = 0
high = n-1

mid = (low + high)//2 = 0 + 4 = 4 //2 = 2

Hence First Half Arr from 0 to 2 index = [3,2,4] and,
Second half arr from mid+1 to n-1 index = [1, 3]


Here we are generally going to follow the recursion and backtracking -

After, complete Divide we get single element each  array with consecutive indexing -
[3]  [2]  [4]   [1]  [3]
0     1     2    3     4
So here each array is sorted we will merge them.

Here for [3], low = 0 and high = 0 , then we dont further divide.
Here for [2], low = 1 and high = 1 , then we dont further divide.
 
# Algo for Merging two sorted Divide Array into one array -
Suppose the sorted array: [2, 3 ,4] and [1, 3]
                           i     mid    mid+1  high

For First Arr : low = 0 and high = 2
For Second Arr : low = 2+1 and high = 4

def mergeTwoSortedArr(arr, low, mid, high):
        # Here, arr = [3, 2, 4, 1, 3]
        #            [2, 3, 4] [1, 3]
            #   low = 0
             #  mid = 2
             #  high = 4

        # On the basis of index we merging the two arrau -
        i = low # for first array starting index to compare
        j = mid + 1  # for second array starting index to compare

        temp = [] # to store new array i.e merge array each time.

        while ( i <= mid and j <= high ):
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i++  
            else :
                temp.append(arr[j])
                j++

            # if either left or righ array exceeds mid value, we just add the remaining element to temparr -
        while (i <= mid):
            temp.append(arr[i])
            i++

        while (j <= high):
            temp.append(arr[j])
            j++ 

            
        # Now we get temp array single one with sorted elements, now we need to put into arr -
        # Copy sorted temp into original array arr - 
        # temp = [1, 2, 3, 3, 4]

        for (i = low to high ):
            arr[i] = temp[i-low]
             # 0 - 0 = 0 - 0 = 0 
             # 1 - 0 = 1 - 0 = 1  
            

'''


# Children Function to merge two sorted Divide Array into one array -
def mergeTwoSortedArr(arr, low, mid, high):

    temp = []
    i = low  # considered first array starts at i index which is low index value.
    j = mid+1 # # considered second array starts at j which is mid+1 index value.

    while i <= mid and j <= high :
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i = i + 1
        else:
            temp.append(arr[j])
            j = j + 1

    # In case some left if any left or right array left with items -
    while i <= mid:
        temp.append(arr[i])
        i = i + 1

    while j <= high:
        temp.append(arr[j])
        j = j + 1

    # now, copy the temp sorted array into sorted array -
    # Copy back to original array
    for i in range(low, high+1 ):
        arr[i] = temp[i-low] 


# Main Function to execute the MErge sort i.e Parent Function, here we following recursive for dividing into two half by midNo each time after each iteration of recursion function and once it get devidied till single element,then lastly we doing merging two sorted into one by backtrack recursive approach -

def mergeSort(arr, low, high):

    # to stop Recursive call/base call -
    if low == high :
        return 
    
    mid = (low + high)//2

    mergeSort(arr, low, mid) # For the first half array dividing each time after iteration i.e 0 to 2 index.
    mergeSort(arr, mid+1, high) # For the second half array dividing each time after iteration i.e 3 to 4 index.

    # Now, we done with divide i.e our least sorted into size of 1 array after iterative recusursive call, now we merge it back with backtracking recusive at same here i.e merging two sorted array back ; simply we call the function for merging two array -


    mergeTwoSortedArr( arr, low, mid, high)




# Lets Run code -
arr = [5, 2, 8, 4, 1] 
n = len(arr)
mergeSort(arr, 0, n-1) # here low we passed AS zero and high as left size i.e n-1.
print(arr)

'''   

# Time Complexity : At every step getting divided by 2 so Time Complexity is  log(base2)(N) and for each time merging two array, the time complexity is O(N). Hence, Resultant Timer Complexity = N * log(base2)(N) = O( Nlog(N) ) for the worst case.

Space Complexity : We are using an extra sapce for N-size array during merging two array, hence O(N) is the space Complexity for worst case.






'''

