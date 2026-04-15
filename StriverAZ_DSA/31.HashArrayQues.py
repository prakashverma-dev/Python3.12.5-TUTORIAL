# 1. Counting Frequencies of Array Elements : -
'''   

Given an array nums of size n which may contain duplicate elements.

Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.

You may return the result in any order, but each element must appear exactly once in the output.


Example 1

Input: nums = [1, 2, 2, 1, 3]

Output: [[1, 2], [2, 2], [3, 1]]

Explanation:

- 1 appears 2 times

- 2 appears 2 times

- 3 appears 1 time

Order of output can vary.

''' 

# Here, quetion doesnot ask that given a item we need to look for, just asked the frequency count of each item.



# I. using HashArray :  Fixed size hasharry (ineffiecnt for large input element)
'''  
✅ Approach (Using Hash Array)

Find the maximum element in array.

Create a frequency array of size max + 1

Count occurrences.

Traverse frequency array and collect pairs.

Time Complexity: O(n + k)
(k = max element value)

'''
def countFrequencies(arr):

    n = len(arr)
    # Create hash array
    max_val = max(arr)
    hasharr = [0] * (max_val + 1)

    for i in range(n):
         hasharr[arr[i]] +=  1

    # Prepare result
    result = []
    for i in range(len(hasharr)):
         if hasharr[i] != 0:
              result.append([i, hasharr[i]]) 
         
    return result
print(countFrequencies([1, 2, 2, 1, 3]))  
print(countFrequencies( [5, 5, 5, 5]))



# II. using HashMap : Python Dictionary -
'''  
✅ Approach (Using Hash Map / Dictionary)

Create an empty dictionary (hash map).

Traverse the array.

For each number:

If it exists in dictionary → increment count.

If not found previous item set to zero as bydefault.

Finally, 
Convert dictionary into required pair format to array.

Time Complexity: O(n)
Space Complexity: O(n)


'''
def countFrequencies2(arr):

    n = len(arr)

    hashmap = {}
    for i in range(n):
         hashmap[arr[i]] = hashmap.get(arr[i], 0) +  1

    # Converting to list of pairs -
    result = [] 
    # for k, v in hashmap.items() :
    #     result.append([k, v]) 

    for k in hashmap :
        result.append([k, hashmap[k]]) 
         
    return result

print(countFrequencies2([1, 2, 2, 1, 3]))  
print(countFrequencies2( [5, 5, 5, 5]))   


'''
Complexity Analysis

Time Complexity: O(N), where N is the number of elements in the array. Each element is processed once.

Space Complexity: O(N), for storing frequencies of unique elements in the unordered_map.

'''