'''   
# Quick SOrt : To sort Array in acending order and with minor tweaks(change) we can sort in decending order. 
# Quick SOrt : It works on the principle of Divide and Conquer Method.

Time Complexity : O (N*log(N) )
Space Complexity : O(1)


4 6 2 5 7 9 1 3 

# Quick Sort : Pick a pivot and place it in the correct position which would be of sorted array.

Pivot could be any element by choice in the array but makesure to pick that pivot same each time -

a) pivot could be first element in the array
b) pivot could be last element in the array
c) pivot could be mid element in the array
d) pivot could be the random element in the array.

[4 6 2 5 7 9 1 3 ]

Step1 : Picked the first element as pivot and placed the smallest elements in the left and largest elements in the right in the same order as original array.

[2 1 3]   4   [6 5 7 9]

Hence, after one iteration we found that 4 is at the sorted position any how.

Step2 : [2 1 3] --> picked the first element as pivot and placed the smallest elements in the left and largest elements in the right in the same order as original array.

[1]  2   [3]

When we get one element after all iteration, then it is sorted.

Step3 : [6, 5, 7, 9] --> picked the first element as pivot and placed the smallest elements in the left and largest elements in the right in the same order as original array.

[5]   6   [7 9]

Here, 5 is sorted.

step4 : [7, 9] --> picked the first element as pivot and placed the smallest elements in the left and largest elements in the right in the same order as original array.

7   [9]

Now, 9 is the sorted.

# PseudoCode :-

Here, as Merge Sort, we are not creating any new array for storing left and right array e arrange it within it using recusive call with low and high index pointer.

# In Pseudo Code, The algo follows same but we swap the element if low index elements is greater than pivot we stop the ith pointer and then we start running j pointer once at j index we finds the  jth index is greater than pivot we swap and continue till i cross j or gets equal. and finally we put that pivot to just after i index which will be the partician element.

[4 6 2 5 7 9 1 3 ]

considered here low pointer and high pointer -

low = 0 
high = n-1

# Picked the pivot and we assigned low index as i and high index as j and placed the ith index as low index place and j as high index place -
pivot = arr[low] # picked the first element
i = low
j = high

# if arr[i] > pivot and arr[j] < pivot matches ---> swap

after i cross the j or gets equal, we get -

4 3 2    1    7 9 5 6  

then we finally put pivot to the center -

1 3 2       4      7 9 5 6
    partition index

    
qs(low, partition - 1)
qs(partition + 1, high)


qs(arr, low, high):

     if low < high:
        



'''

# Children Function to perform the partition each time with finding the partition index  and value -
# (this take O(N) )
def partition(arr, low, high):

    pivot = arr[low]
    i = low # OR, if choosen First element as Low then i = low + 1.
    j = high

    while True :

        # if it get false means we found a element greater than pivot then we proceed to next i.e jth looping -
        while i<= j and arr[i] <= pivot:
            i= i + 1

        while i<= j and arr[j] >= pivot:
            j = j - 1

        if i <= j :
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # finally when we done with all swap we swap last i.e pivot with low index -
    arr[low], arr[j] = arr[j], arr[low]

    # Finally We return the partition index - 
    return j
    
# main Function - (this take O(LogN))
def quickSort(arr, low, high):

    if low < high:
         partitionInd = partition(arr, low, high)
         quickSort(arr, low, partitionInd - 1 )
         quickSort(arr, partitionInd +1, high)


# Lets run this -
# arr  = [3, 1, 2, 4, 4, 5, 6, 7, 9]
# n = len(arr)
# quickSort(arr, 0, n-1) 
# print(arr)

# Driver Code -
t = int(input())
# print(type(t))

for _ in range(t):
    n = int(input())
    # print(type(n))
    arr = list( map(int, input().split(" ")) )
    quickSort(arr, 0, n-1)
    print(*arr) 

'''          
# Time Complexity : O (NlogN) 

logN for splitting array each time divided half
N for each iteration of low to high.

Space Complexity : O(1) we are not using any extra space for Quick Sort.









'''
# ------------------------------------------- 

# For Code 360 Platform : - 

def partition(arr, low, high):

    pivot = arr[low]
    i = low # OR, if choosen First element as Low then i = low + 1.
    j = high

    while True :

        # if it get false means we found a element greater than pivot then we proceed to next i.e jth looping -
        while i<= j and arr[i] <= pivot:
            i= i + 1

        while i<= j and arr[j] >= pivot:
            j = j - 1

        if i <= j :
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # finally when we done with all swap we swap last i.e pivot with low index -
    arr[low], arr[j] = arr[j], arr[low]

    # Finally We return the partition index - 
    return j
    

def quickSortUser(arr, low, high):

    if low < high:
         partitionInd = partition(arr, low, high)
         quickSortUser(arr, low, partitionInd - 1 )
         quickSortUser(arr, partitionInd +1, high)


# Important** -
def quickSort(arr):
    quickSortUser(arr, 0, len(arr) - 1)
    return arr



# For GeeksforGeeks Platform -
class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
             partitionInd = self.partition(arr, low, high)
             self.quickSort(arr, low, partitionInd - 1 )
             self.quickSort(arr, partitionInd +1, high)
        #code here 

    def partition(self, arr, low, high):
        #code here
        pivot = arr[low]
        i = low
        j = high

        while True :
    
            # if it get false means we found a element greater than pivot then we proceed to next i.e jth looping -
            while i<= j and arr[i] <= pivot:
                i= i + 1
    
            while i<= j and arr[j] >= pivot:
                j = j - 1
    
            if i <= j :
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break

        # finally when we done with all swap we swap last i.e pivot with low index -
        arr[low], arr[j] = arr[j], arr[low]
    
        # Finally We return the partition index - 
        return j