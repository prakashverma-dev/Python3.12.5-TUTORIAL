# To Swap Array's any two position value with each others -
'''  
arr = [10, 20, 30, 40]
        0,  1,  2,  3

You want to exchange values at two positions (indexes) in an array.

Example:
Before → [10, 20, 30, 40]
Swap elements at index 1 and 3
After → [10, 40, 30, 20]

'''

# Approach 1 : Pythonic Way (Best & Most Used) -
arr = [10, 20, 30, 40]

i = 1 # assign the indexes for which two position we wanna swap.
j = 3

arr[i], arr[j] = arr[j], arr[i]
print(arr)

# same using function - 
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [1, 2, 3, 4]
swap(arr, 0, 2)
print(arr)



# Approach 2 : Using a Temporary Variable -
arr = [10, 20, 30, 40]

i = 1 # assign the indexes for which two position we wanna swap.
j = 3

temp = arr[i]
arr[i] = arr[j] # now use arr[i] to hold j indexed value coz stored arr[i] original value into a temp variable.
arr[j] = temp

print(arr)


# Task Based on Swapping : For swapping first index and last index in array and one step increment and one step decrement..and continues..

arr = [4, 2, 1, 6, 3]
#      0  1  2  3  4
print(arr) 

# For swapping first index and last index and, one step increment and one step decrement... continues.. we could use "last index" (i.e j) in terms of length and 'i' i.e (n-1-i) 

# 'J' In terms of 'i'  # n -1 - i 
n = len(arr) # 5
# i = 0  #  5 - 1 - 0 = 4  ---> 0 and 4 indexed get swapped.
# i = 1  #  5 - 1 - 1 = 3  ---> 1 and 3 indexed get swapped.
# i = 2  #  5 - 1 - 2 = 2 ---> 2 and 2 indexed will get swapped if conditon is true for equal case, else not.

for i in range(0, n//2):

    print(i) # will go to 0,1 index only as will reach one less than n//2.
    arr[i], arr[n-1-i] = arr[n-1-i],  arr[i] 

print(arr) 







