'''
# Sorting uses to fpr efficeint find the target which one we want and makes time -effieceint. We going to learn some sorting algotithms :

i) Bubble Sort
ii) Selection Sort
iii) Inserstion Sort
iv) Merge Sort
v) Quick Sort

These above five are famous.

vi) Counting Sort
vii) Radix Sort
viii) Heap Sort
ix) Bucket Sort


'''
'''
#1. Bubble SOrt : It is not that much Effieceint but simple to undertand. Time Complexity of Bubble sort is O(n^2)

# Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

# How it works: We start with an unsorted array.

[7, 12, 9, 11, 3]

Then, We start comparing two value at a time from left to right, if the left value is greater than right value, we swap the left value to right and if the left value less than right value, we keep it as it is and move to next pair and repeat same.

By doing in first iteration of array, we get most highest value at the end and in second iteration we second highest just before main highest.

Repeat until no more swaps are needed and you will get a sorted array using Bubble SOrt algo.

Comparision of Indexes at a time : [7, 12, 9, 11, 3, 2]
0 1  
1 2
2 3 
3 4
4 5
........


'''

def bubbleSort(arr):

    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i): # -i used for not checking last all shorted values again.

            # print(f'j : {j} ; j+1 : {j+1}')

            if arr[j+1] < arr[j] : # checking if next item is less than previous item, then only swap else no swap.
                  
                temp = arr[j] 
                arr[j] = arr[j+1]
                arr[j+1] = temp

                # arr[j], arr[j+1] = arr[j+1], arr[j]

        # print("Next Iteration...")
    
    print("Sorted array is : ", arr)
                

bubbleSort([7, 12, 9, 11, 3, 2])

# Time Complexity of Bubble Sort is : O(n^2) as First loop for making iteration again and again ; inner loop is for comparing two value at a time, so n * n  = n^2.

# Hence, the run time increases quadratic when the size of the array is increased in bubble sorting. There are other sorting algorithms that are faster than this, like Quicksort algo, that we will look at later.

'''

# Swapping in Python : -
i) using Tuple unpacking -

a = 5
b = 10
a,b = b, a
print(a,b) # 10 5

ii) using temp variable-

a = 5
b = 10

temp = a
a = b
b = temp
print(a,b) # 10 5


'''