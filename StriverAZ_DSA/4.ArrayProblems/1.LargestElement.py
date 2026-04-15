'''   
# 41 Different Problems on Array -

# Basics of array : - It is a Data Structure contains only same datatype i.e similar elements i.e either only integers or stings or boolean or char or pairs.
    
arr[] = [][][][][][] ----> of size n = 6
         x, x+1, x+2, x+3,...

Here, x is random memory in the computer to store the elememt and it is contigous in nature measn next element stores in x+1, x+2 ..

In Python, we define fixed array with -

arr = [None]*6

# Defining array of size of 6 -

arr = [None]*6 #  0 to 5 i.e 0 to n-1.

print(arr)
print(len(arr)) 

Maximum Size of Array we can define, 10^6 inside any function and we can define 10^7 size array outside of function i.e GLobally we can define.


# We access array first element with zero and last element with (size-1)


arr[0]
arr[n-1] 

for(i = 0; i<n ; i++){ # run from 0 to n-1.
    print(arr[i]) --> to access each element in loop.
}

-----------------------------------------------------------------------------------


Q. Largest Element in an Array : -

arr[]= [3, 2, 1, 3, 2]

Approch In Interviews: Start with Brute Force Sultion and ask Test Cases and You should you who drives the interview and If you known the Optimized Soltion still come up with Brute Force Solution then Optimized soliution.

Brute-Force Solution ----> Better Solution ----> Optimed Solution.


Way1 :  Brute_Force : First Sort then last element is Largets - O(nLogN)

Sort - O(nlogn) Tc and O(1) for Quick Sort.

Way2 : Lets Optimize T.C O(N Log N) -

largeest = arr[0]  

for (i = 0 or 1 ; i<n ; i++){

    if arr[i] > largest {
            largest = arr[i]
    }


}

print(largest)

Time Complexity : O (n) coz we loop once.
'''
# Brute Force with inbuilt sort() function -
def largestElement(arr):

    n = len(arr)
    arr.sort() # .sort() function takes O(nlogn) Complexity

    # now return the last element -
    return arr[n-1]

# Time Complexity: O(N log N), where N is the size of the array, as we are sorting the array.
# Space Complexity: O(1), as we are using a constant



# Optimized Solution  -
def largestElementOpt(arr):

    n = len(arr)
    largest = arr[0]
    # largest = float("-inf")

    for i in range(0, n):
        if arr[i] > largest :
            largest = arr[i]
    
    return largest

# Time Complexity: O(N), where N is the size of the array, as we are iterating through the array once.
# Space Complexity: O(1), as we are using a constant

print(largestElementOpt([1,2, 3, 1, 10, 0, 50, 50, 14, 3]))
print(largestElementOpt([1,2, 3, -1, 10, 0, 50, 50, 14, 3])) 