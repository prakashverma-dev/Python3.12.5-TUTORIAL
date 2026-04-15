'''  

# Second Largest Element without Sorting -

arr [] = [1 2 4 7  7 5]


# Brute-Force --

Apply Sorting to sort - O(nlogn)

arr.sort() -->  1 2 4 5 7 7

largest = arr[n-1]
secondlarget = arr[n-2] we canot say if it has duplicate largest element.
secondlargest = -1 

for (i = 0; i <= n-2; i++){

    if arr[i] != largest{
        secondlargest = arr[i]
        break;
    }
}

Time Complexity : O(NlogN) + O(n) = O(NLogN)




# Optimized -

# Firstly we will find the first largest - O(n)

largeest = arr[0]  
for (i = 0 or 1 ; i<n ; i++){

    if arr[i] > largest {
            largest = arr[i]
    }

}

# Now for secondlargest - O(n)

secondlargest = -1
for (i = 0; i < n : i++){

    if arr[i] != firstlargest && arr[i] > secondlargest :

        secondlargest = arr[i]

}

print(secondlargest)


O(n) + O(n) = O(2n) Time Complexity i.e O(N)

'''''

#1. Brute Force - O(N logn)  ##* AVOID THIS SOLUTION AT INTERVIEW -
# The idea is to sort the array in non-decreasing order. Now, we know that the largest element will be at index n - 1. So, starting from index (n - 2), traverse the remaining array in reverse order. As soon as we encounter an element which is not equal to the largest element, return it as the second largest element in the array. If all the elements are equal to the largest element, return -1.


def findSecondLargest1(arr):

    n = len(arr)
    arr.sort()  # log(N Log N)

    # We get the largest element now -
    largestElem = arr[n-1]

    # Traversing to find second largest except the found number (which is first largest) -
    secondlargest = float("-inf")
    for i in range((n-2), -1):

        if arr[i] != largestElem :
            secondlargest = arr[i]
            break 
        
    

# 7 8 8 1 4 3  


#2. Better Solution : two Pass - O(n)
# The approach is to traverse the array twice. In the first traversal, find the maximum element. In the second traversal, find the maximum element ignoring the one we found in the first traversal.

def findSecondLargest(arr):
    # Write your code here.
    n = len(arr)
    firstLargest = float('-inf')
    secondLargest = float('-inf')
    
    for i in range(n):

        if arr[i] > firstLargest:
            firstLargest = arr[i] 
            # print(firstLargest)
    
    for i in range(n):
            
        if arr[i] != firstLargest and arr[i] > secondLargest :
            secondLargest = arr[i]
            

    if secondLargest == float("-inf"):
        return -1
    
    return secondLargest

print(findSecondLargest([7, 8, 8, 1, 4, 3])) # 7

# 3. Better Solution : One Pass - O(n)
# Here in one pass looping as soon as we find the largest while looping that means the second largest would be previous largest. thats the logic we will update -

def findSecondLargestOpt(arr):
    # Write your code here.
    n = len(arr)
    firstLargest = float('-inf')
    secondLargest = float('-inf')
    
    for i in range(n):

        if arr[i] > firstLargest:
            secondLargest = firstLargest # Remember to put in first line
            firstLargest = arr[i] 
            
            
        if arr[i] != firstLargest and arr[i] > secondLargest :
            secondLargest = arr[i]
            

    if secondLargest == float("-inf"):
        return -1
    
    return secondLargest

print(findSecondLargestOpt([7, 8, 8, 1, 4, 3])) # 7








# Code Ninja to FInd Second Largest and Second Smallest with O(n) Complexity -


# def getSecondOrderElements(n: int,  a: [int]) -> [int]:
#     # Write your code here.

#     slargest = secondLargest(a, n)
#     ssmallest = secondSmallest(a, n)

    
#     return slargest, ssmallest


def secondLargest(arr, n):

    fLargest = float("-inf")
    sLargest = float("-inf")

    # using one Looping -

    for i in range(n):

        if arr[i] > fLargest:
            sLargest = fLargest
            fLargest = arr[i]

        if arr[i] != fLargest and arr[i] > sLargest:
            slargest = arr[i]
    
    return sLargest


def secondSmallest(arr, n):

    firstSmall = float("inf")
    secondSmall = float("inf")

    # using one Looping -

    for i in range(n):

        if arr[i] < firstSmall :
            secondSmall = firstSmall
            firstSmall = arr[i]

        if arr[i] != firstSmall and arr[i] < secondSmall:
            secondSmall = arr[i]
    
    return secondSmall



    