
# Selection Sort : It is also takes O(n^2) time complexity like Bubble Sort But In Selection sort, we use only once swap of two items for each iteration and again we repeat the iteration and do once swaping such that max value stack to the right side of array or, min value get stack to the left side of array.

# In Selection Sort there is alwys two section after each iteration that is sorted array and unsorted array, and then we always look into unsorted array by keepin sorted array fixed.

def selectionSort(arr):

    size = len(arr) # when ever there is size or length consider always it will go till last element in the array that is the mean of size or length actually.
    # maxIndex = 0 # considered array first value is the max value for now.

    for i in range(0, size):
        maxIndex = 0 
        # print(f'For i value : {i} ')
        for j in range(0, size-i):

            # print(j)
            # print(arr[j])
        
            # print(f'j : {j} ')

            if arr[j] > arr[maxIndex]:
                maxIndex = j # Max Index get updated.

        # print("Max value :", arr[maxIndex])      # After first iteration we get the max value.
        
        temp = arr[maxIndex]
        arr[maxIndex] = arr[j] # OR, arr[j] ---> arr[size - i - 1] 
        arr[j] = temp

        # print("Array Sorted after each iteration", arr)

        # OR, 
        # lastIndex = size - i - 1
        # arr[maxIndex], arr[lastIndex] = arr[lastIndex], arr[maxIndex]


        
    
    print("Complete Sorted Array using Selection Sort : ", arr)
        


selectionSort([0, 21, 5, 1, -5, 12, 9, 11, -2])


# Time Complexity of Selection Sort Is O(n^2) coz On average, about n/2 elements are compared to find the lowest value in each iteration of inner loop and in Outer loop it runs runs each time approximately n times.

# So, We get time complexity: O(n/2 * n ) = O(n^2)


# Hence, As you can see, the run time is the same as for Bubble Sort: The run time increases really fast when the size of the array is increased.


# ----------------------------------------------------------------------




# def selectionSort(arr):

#     size = len(arr) # when ever there is size or length consider always it will go till last element in the array that is the mean of size or length actually.
#     # maxIndex = 0 # considered array first value is the max value for now.

#     for i in range(0, size):
#         maxV = arr[0] 
#         # print(f'For i value : {i} ')
#         for j in range(0, size-i):

#             # print(j)
#             # print(arr[j])
        
#             # print(f'j : {j} ')

#             if arr[j] > maxV:
#                 maxV = arr[j] # Max Index get updated.

#         # print("Max value :", maxV )      # After first iteration we get the max value.
        
#         maxPotion = arr.index(maxV)
#         temp = arr[maxPotion]
#         arr[maxPotion] = arr[j] # OR, arr[j] ---> arr[size - i - 1] 
#         arr[j] = temp

    
#     print("Complete Sorted Array using Selection Sort : ", arr)
        

# selectionSort([0, 21, 5, 1, -5, 12, 9, 11, -2])