
# Using For-loop : -

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

    # temp = arr[i]
    # arr[i] = arr[j]
    # arr[j] = temp 


def quick_sort(arr, lowIndex, highIndex):

    if lowIndex < highIndex:

       # Sorted Pivot indexing we get at correct position afterr each iteration of Partition Function -
        sorted_pivot_index = partition(arr, lowIndex, highIndex)

        quick_sort(arr, lowIndex, sorted_pivot_index - 1 ) # For LHS Partiton to get sort, mention LHS lowIndex and LHS highIndex.
        quick_sort(arr, sorted_pivot_index + 1 , highIndex) # For RHS Partiton to get sort, mention RHS lowIndex and RHS highIndex.


def partition(arr, lowIndex, highIndex):

    pivot = arr[highIndex]
    i = lowIndex - 1 # Bydefault i start from -1 and It will increatement after each iteration. // i  here is iteration steping.

    for j in range(lowIndex, highIndex): # j start from 0 index

        # First we check j index value is less than pivot, perform operarion make swap - 
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)


    swap(arr, i + 1, highIndex)
    
    return i + 1 



# Let's Test Example Run : -
unsortedArr = [5, 6, 2, 3, 1, 8, 4]
quick_sort(unsortedArr, 0, len(unsortedArr) - 1)  

print("Sorted Array : ", unsortedArr) 


# Quicksort Time Complexity and Space Complexity : - 

'''

#a) For Average Case and Best Case Only : -

n ---> For Single for-loop in Partition function it runs to n-times

logn ---> For the Recursive part array gets divided qually half each time.

Hence, O (n * log n) = O (nlogn ) is the time complexity of the Quick Sort. 

TC : O(nlogn)
SC : O(1)   ---> We are not using any extra space in Quick Sort to sort the array, so It has Constant Space Complexity.


#b) For Worst Case Scenario : - Time Complexity Becomes O(n^2) coz if the array is already sorted Or, Array all Items are same like -

arr = [1, 3, 5, 7, 8, 10]
arr2 = [5, 5, 5, 5, 5, 5]

In This, Senario, Quick SOrt Takes O(n * n) times coz first n for for-loop in partition function and Other loop for n times again in Recursion Part as Array LHS and RHS data will be already sorted but Recursive function will run to verify it. Hence,

TC : O (n^2)
SC : O (1) same Constant SPace Complexity for Worst Case As well.

Henceeee : There is significant improvement in time complexity for Quicksort in an average scenario is O (nlogn) , compared to the previous sorting algorithms Bubble, Selection and Insertion Sort with time complexity of O (n^2) .










'''


















# ---------------------------------------------------------------------
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             swap(arr, i, j)
#     swap(arr, i + 1, high)
#     return i + 1

# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]

# # Example run
# arr = [10, 7, 8, 9, 1, 5]
# quickSort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)


        
