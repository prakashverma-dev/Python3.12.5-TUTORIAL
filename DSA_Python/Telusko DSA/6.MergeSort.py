# Merge Sort : -

'''


It also has time complexity of O(nlogn). Both Quick Sort and Merge Follow the technique called Divide and Conquer Method.

Divide and Conquer Method : Here, we break the down the problem into sub-problem and Solve it, and once we get the soltion for each sub problem then we combine all the sub solitons into one to get teh final solution of main problm knwon as Divide and Conquer Method in programming.


In Merge Sort, We using Divide and Conquer method -

It is basically the 

Step1 : Deiv




'''

# Step1 : Let's First Divide the main array into two subarrays recursively - 

def mergeSort(mainArr):

    if len(mainArr) <= 1 :
        return mainArr  # Base case
 
    mid = len(mainArr) // 2

    leftPart =  mainArr[:mid]  #  Divide left half
    rightPart = mainArr[mid:]  # Divide right half
    
    # print("Dividing:", left, right)  # Visualize the divide step


    left_sorted = mergeSort(leftPart)   # Recursively sort left half
    right_sorted = mergeSort(rightPart) # Recursively sort right half


    return mergeTwoSortedArr(left_sorted, right_sorted) # Merge sorted halves of two arrays.


# Step2 : Now, Once We Divided Till We dont get single ELement in sub array, which means it is sorted now, now we will merge each two sorted array -

def mergeTwoSortedArr(arr1, arr2):

    resultArr = []
    i = 0
    j = 0

 # Merge two sorted lists
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j] :
            resultArr.append(arr1[i])
            i += 1

        else :
            resultArr.append(arr2[j])
            j += 1


 # Add remaining elements
    while i < len(arr1) :
          resultArr.append(arr1[i])
          i += 1

    while j < len(arr2) :

            resultArr.append(arr2[j])
            j += 1


    return resultArr


# Let' Run -
print(mergeSort([3,1,2,4, 1,5,2,6,4,8,10 ]))  


'''
# Time Complexity : For first Only Divide Part Time Complexity is O(log n) coz Array Gets divided each time with increase in size and For Merge Part, Time Complexity is O(n) coz It taverse trough each two sub arrays i.e O(m + n) = O(n) for both subarray two merge them into one having time Complexity BigO(n).

Hence, Resultant Time Complexity of Merge SOrt is O (logn * n) = O(n log n) .

Note : time complexity is pretty much same for different kinds of arrays like if the array is sorrted array already or same elements or completely shuffled, the time complexity takeb by Merge sort for Worst/Best/Averga Case is same i.e BigO(n logn ) .

# Space Complexity of Quick Sort : - / Auxiliary Space -

Sc : O(n), Additional space is required for the temporary array used during merging.

'''
     
