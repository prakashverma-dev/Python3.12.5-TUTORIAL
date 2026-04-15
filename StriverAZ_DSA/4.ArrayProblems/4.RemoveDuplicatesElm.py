'''  

# Remove Duplicates Elemensts with in-place from Sorted Array - 

[1,1,2,2,2,3,3]   ---> [1,2,3] we need to return the final no of unique element at the end.

Measn we dont have to create a new array i.e we no need to take extra sapce i.e O(1) Space Complexity -


# Brute Force Sultion : Creating a set and adding array all element one by one into set since set stores unique elements hence at the end we will get only uniqely stores element in the set Data Strcuture but here we get 
 O(n) Space complexity. 

 and return the unique elements from the array.


'''

# With new Space - O(N) Space Complexity

def removeDuplicates(arr):

    n = len(arr)
    myset = set()

    for i in range(n):
        myset.add(arr[i])
    
    # return myset
    return len(myset)
    # return list(myset)

print(removeDuplicates([1,1,2,2,2,3,3]))

# Time Complexity: O(N), We traverse the entire array and insert elements into set.
# Space Complexity: O(N), additional space used to store elements in set.


# With In-place : First keep first element index as currentIndex as unique element to compare to next elment you face as soon as unique element found i.e arr[current] != arr[i] --> increment the currentIndex and swap it. and at the end we will found at one place all unqiue elements till out current index reached and other side we have other remaining elements. Though we will return currentIndex +1 for length of unique element.

def removeDuplicatesInplc(arr):

    n = len(arr)

    currentIdx = 0
    for i in range(1, n):

        if arr[currentIdx] != arr[i] :
            currentIdx += 1
            swap(arr, currentIdx, i) #OR, # arr[currentIdx] = arr[i]

    return currentIdx +  1

def swap(arr, i, j):
    
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


print(removeDuplicatesInplc([1,1,2,2,2,3,3]))

# Time Complexity: O(N), We traverse the entire original array only once.
# Space Complexity: O(1), constant additional space is used to check unique elements.
