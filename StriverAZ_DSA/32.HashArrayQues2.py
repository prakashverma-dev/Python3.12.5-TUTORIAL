'''

# Highest Occurring Element in an Array : -


Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.



Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!


Example 1

Input: nums = [1, 2, 2, 3, 3, 3]

Output: 3

Explanation: The number 3 appears the most (3 times). It is the most frequent element.

Example 2

Input: nums = [4, 4, 5, 5, 6]

Output: 4

Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.

'''



# I.using HashArray : -

def mostFrequentElement(arr):

    n = len(arr)
    # Create hash array
    max_val = max(arr)
    hasharr = [0] * (max_val + 1)

    for i in range(n):
         hasharr[arr[i]] +=  1

    # print(hasharr) # [0, 0, 0, 0, 2, 2, 1] for array = [4, 4, 5, 5, 6]
                 #    0  1  2  3  4  5  6 
    
    #Now, Let's Iterate through hasharr to find the max element in the stored hasharr, corresponding index will be highest ocurring element from the array - 
    maxElem = 0  # float("-inf")  Need a value less than any other number for comparisons
    maxElemIndex = 0 # which will lead to max Element.
    for i in range(len(hasharr)):
         if hasharr[i] > maxElem:
            maxElem = hasharr[i] # 2
            maxElemIndex = i # 4

    print(maxElemIndex)  # OR,  print(hasharr.index(maxElem)) 


    # Iterate through hasharr to find min element and corresponding min elmenet index will be the lowest occuring elment from the array -
    minElem = float("inf") # We have set the positive infinity as highest value by default.
    minElemIndex = -1 
    for i in range(len(hasharr)):

        if hasharr[i] > 0 : 
            if hasharr[i] < minElem: 
                minElem = hasharr[i] # 0 
                minElemIndex = i # 0

    print(minElemIndex)  # OR,  print(hasharr.index(minElem))


 
# mostFrequentElement([4, 4, 5, 5, 6]) # 4 and 0 (4 ouccured for twice and 6 occured for once) 
# mostFrequentElement([1, 2, 2, 3, 3, 3]) 





# II. using HashMap : - 

def highest_frequency(arr):

    hashmap = {}

    for i in range(len(arr)):

           hashmap[arr[i]] = hashmap.get(arr[i], 0)  + 1  # For first time arr[i] doesnot get value so assined 0 and from next updation arr[i] get the previous value which get updated with +1.

    print(hashmap)

# Let' find max frequency value correspondig to key -
    maxValue = 0
    maxValueKey = 0

    for k in hashmap:
        # print(k, hashmap[k])

        if hashmap[k] > maxValue:
            maxValue = hashmap[k]
            maxValueKey = k 
    
    print("highest frequency element : ", maxValueKey)


# To find the lowest key value, then we return the corresponding key -
    minValue = float("inf") 
    minValueKey = 0

    for key in hashmap:

        if hashmap[key] < minValue:
            minValue = hashmap[key]   
            minValueKey = key

    print("Lowest frequency element : ", minValueKey)




highest_frequency( [4, 4, 5, 5, 6] )
highest_frequency( [1, 2, 2, 3, 3, 3] ) 



















'''  
Complexity Analysis : -

Time Complexity: O(N), where N = size of the array. The insertion and retrieval operation in the map takes O(1) time.
Space Complexity: O(N), where N = size of the array. It is for the map we are using.



'''