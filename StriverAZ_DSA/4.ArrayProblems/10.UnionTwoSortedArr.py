
''' Union of two sorted Array : - Doesnot carray any duplicates after combining two arrays 

arr1 = [1,1,2,3,4,5] might have duplicates
arr2 = [2,3,4,4,5,6] might have duplicates

Result = [1,2,3,4,5,6] Adding two Arrays with all elements with no duplicates.


'''

# I. Brute-Force Approch : using a 'set' DataStructure -


def union(arr1, arr2):

    n1 = len(arr1)
    n2 = len(arr2)

    myset = {}  # Order is neccessay.

    for i in range(n1):
        myset.keys(arr1[i])

    for i in range(n2):
        myset.keys(arr2[i])

    # return list(myset) 
    # return sorted(myset) # For returing sorted array.


arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]
# print(union(arr1, arr2))


# Time Complexity : O(n1logn1) + O(n2logn2) = O(n * logn) ; here n1 is for Trasversing in one loop and logn1 is for Inserting an element in a set takes logN time.
# Space Complexity : O(n1+n2) = O(n) for using n-space extra.





# II. Optimal Approch : Two Pointer Approch with O(n+m) Time and O(n+m) Space /O(1) if mention not to include extra array for resutant -
# Basically we are using "Merge Step of Merge Sort" -

'''  
arr1 = 1 1 1 3 4 5 ;  i pointer at arr1[0]
arr2 = 2 2 2 2 3 4 ;  j pointer at arr2[0]

n1 = len(arr1)
n2 = len(arr2)

i = 0
j = 0 # Remember to assign at index not its value we compare value inside the while loop.


Step1 : Firstly check indivisual array if duplicates adjacent element then shift the respective i or j index ahead.

while i<= n1-1 and j <= n2-1 { #Run till last index of arr1 and arr2.

    if i>0 and arr[i] = arr[i-1]{ # We are comparing current value with one previus value; the reason for first compare we avoid the negative indexing with i>0
            i++
            continue; ---> Dont break the while loop just skip ahead of the code after this and move to next looping round.
        }

    # sAME FOR J LOOP -
    if j>0 and arr[j] = arr[j+1]{
            j++
            continue; ---> Dont break the while loop just skip ahead of the code after this and move to next looping round.
        }

}

Step2 : Now, we use merge sort algo, now check if arr1[i] < arr[j] then add current i index element into result array and shift i index once and same if arr1[i] > arr[j] then add j current index value and shift j index and in last case if both array found equal then add either one and move i and j both to next.

while i<= n1-1 and j <= n2-1 { #Run till last index of arr1 and arr2.

    if arr1[i] < arr2[j]{

            result.append[arr[i]]
            i++
       
        }

    # Otherwise j element is smaller -
    elseif if arr1[i] > arr2[j]{

            result.append[arr[j]]
            j++
       
        }

    # if both i and j element equal add either one and shift i and j both -
    else :
            result.append[arr[i]]
            i++
            j++

}


Step2 : IF either one of the i and j gets completed the loop, then if any array has some remaining elements then add left over either array data into result array -


    # Step3 : Add remaing element from either one the array -
    while i <= n-1:

        if i > 0 and arr1[i] == arr1[i-1]:
            i += 1
            continue

        result.append(arr1[i])
        i += 1

    while j <= m-1:

        if j > 0 and arr2[j] != arr2[j-1]:
            j += 1
            continue
        
        result.append(arr2[j])
        j += 1



'''


def union2(arr1, arr2):

    a,b = arr1, arr2
    n = len(arr1)
    m = len(arr2)

    result = []
    # Remember to keep it as zero index not its value, we compare value inside the while loop.
    i = 0
    j = 0

    while i < n and j < m:  # Run till 0 to n-1 of array size.

        # Step1 - Working with indivisual current array -
        # First Edge Case : When Similar element in the current array we move to next index -
        # We are comparing current value with one previus value
        if i > 0 and arr1[i-1] == arr1[i]:
            i += 1
            continue

        if j > 0 and arr2[j-1] == arr2[j]:
            j += 1
            continue

        # Step2 : Working with both array with comparioson -
        # select and add the smaller element and move
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1

        # If equal, then add to result and move both
        else:
            result.append(arr1[i])
            i += 1
            j += 1

    # print(i) # check current i index and j index -
    # print(j)

    # Step3 : Working with indivisual array to add remaining elements -
    # Add remaing element from either one the array -
    while i <= n-1:

        if i > 0 and arr1[i] == arr1[i-1]:
            i += 1
            continue

        result.append(arr1[i])
        i += 1

    while j <= m-1:

        if j > 0 and arr2[j] != arr2[j-1]:
            j += 1
            continue

        result.append(arr2[j])
        j += 1

    return result


# arr1 = [1,1, 1, 3, 4, 5]
# arr2 = [2,2, 2, 2, 3, 4, 5, 6, 8, 9]

# arr1 = [4, 6, 6, 9, 10, 11, 11, 11]
# arr2 = [1, 1, 1, 3, 3]

arr1 = [2]
arr2 = [2]
print(union2(arr1, arr2))


'''
Time Complexity : O(n+m) = O(N) 
Space Complexity : O(n+m) = O(N) for returing the result; O(1) {If Space of union ArrayList is not considered}


'''

# HashTable : It is Data struture under which a) hash Sets and b) hash Maps comes.   

# In python : set --> hashset and dict --> hashmap

# Hash Sets in Python are typically done by using Python's own set data type.
# Hash Maps in Python are typically done by using Python's own dictionary data type.
