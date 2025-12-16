
'''

# Insertion SOrt : It is something inserting right elemet at right position by shifiting the other elements position one space so that right element get a postion to place and it will look like sorted.

nums = [3,5,6,4,8,9,10,7,1]






'''

def insertionSort(arr):

    size = len(arr)
    for i in range(1,size):
        # print("i : ",i)

        key = arr[i]
        insert_index = i

        for j in range(i-1, -1, -1):
            # print("j : ",j)

            if arr[j] > key :
                arr[j+1] = arr[j]
                insert_index = j
            
        arr[insert_index] = key
        print(arr)
                            

    print("Sorted list : ", arr)

insertionSort([3,2,6,1,5])


# Time Complexity of Insertion Sort : O(n^2)

# Coz : Insertion Sort must run the loop to insert a value in its correct place approximately n times which is outer loop and inner loop runs n/2 times to find the correct place to insert it.

# Thus, We get time complexity for Insertion Sort : O(n * n/2) = O(n^2).


# Next up is Quicksort. Finally we will see a faster sorting algorithm!