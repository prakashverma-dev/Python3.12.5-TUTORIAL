'''
#Quick Sort : As the name suggests, Quicksort is one of the fastest sorting algorithms which has O(nlogn) time complexity for Average Case and Best Case  but for worst case time it also goes to O(n^2) time complexity. 

Average Time Complexity : O(n logn)
Worst Case Time Complexity : O(n^2) For Sorted Array COz when array is soreted if we do Quick sort, it will as equal to complete search space coz no of left and right partition be n iteration as per input


Whereas, Bubble sort, Selection Sort, Insertion sort has Big O(n^2) time complexity.

In Quick sort we uses :-

i)  Divide and Conquer Method : Divide the main problem into multiple parts and solve each part indivisually and at the end combining all solved problem into one, known as Divide and Conquer MEthod in the term of programming language.

ii) Recursion : We going to use Recursion in Quick sort where we calls our funcion inside function untill recursion base case to stop recursion function.

iii) Pivot(peeveet) : Pivot In short it is a point where to take the reference for the sorting our problem. In other words, It is a central point of Problem.

iv) Tree : When we using divide and conquer method, we basically creating a tree structure where each branch has got subproblems untill it not get shorter.







'''
# Find Min and Max Number from an unsorted array : -


def findMinMaxNum(arr):

    size = len(arr)
    minN = arr[0]
    maxN = arr[0]

    for i in range(0, size):

        if arr[i] < minN:
            minN = arr[i]

        if arr[i] > maxN:
            maxN = arr[i]

    print("Min No : ", minN)
    print("Max No : ", maxN)


# findMinMaxNum([3,1,2,7, -1])

# ----------------------------------------------------------------

def swap(arr, i, j):
        
        # arr[i], arr[j] = arr[j], arr[i]
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


def partition(arr, lowIndex, highIndex):

    pivot = arr[lowIndex]
    i = lowIndex + 1
    j = highIndex

    while i< j :

        while arr[i] <= pivot and i <= j :
            i = i + 1 # Increment the while loop forwording for i-loop

        while arr[j] >= pivot and i <= j :
            j = j - 1 # Increment the while loop backwording for j-
            
        if i<=j:
            swap(arr, i, j)
      
    swap(arr, lowIndex, j)
    
    return j # Returing the sorted Single Element Index which is pivot placed at correct position of each iteration of running this partition function.


def quick_sort(arr, lowIndex, highIndex):

    if lowIndex < highIndex:

       # Sorted Pivot indexing we get at correct position afterr each iteration of Partition Function -
        sorted_pivot_index = partition(arr, lowIndex, highIndex)

        quick_sort(arr, lowIndex, sorted_pivot_index - 1 ) # For LHS Partiton to get sort, mention LHS lowIndex and LHS highIndex.
        quick_sort(arr, sorted_pivot_index + 1 , highIndex) # For RHS Partiton to get sort, mention RHS lowIndex and RHS highIndex.


# Let's Test : -
unsortedArr = [5, 6, 2, 3, 1, 8, 4]
quick_sort(unsortedArr, 0, len(unsortedArr) - 1)  

print(unsortedArr) 



