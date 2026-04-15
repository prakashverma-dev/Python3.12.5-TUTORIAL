'''  
# Intersection of Two Sorted Arrays : - Only elments which are common in both/Present in both(duplicates allowed if common again.)

arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,7]

result = [2,3,3,5,6]



# Direct we jump to Optimal Solution :

Step1 : Check one element from first to another array and compare. If they mateched proceed both and add the value to result and if current array element is less than other array then increment i index and if current element is greater then increment j index.



'''

def intersection(a, b):

    n, m = len(a), len(b)

    i, j = 0, 0
    result = []

    while i<n and j <m:

        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            result.append(a[i])
            i += 1
            j += 1
    
    return result 

arr1 = [1,2,2,3,3,4,5,6]
arr2 = [2,3,3,5,6,6,7]
print(intersection(arr1, arr2))

# Time Complexity : O(n+m) = O(N)
# Space Complexity : O(n+m) = O(N) and O(1) if do not consider rerurn reesultant.