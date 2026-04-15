'''
Q. # Reverse an Array : - There are major two approaches - General Approch and Recursive Approach -


#1) General Approch : using for-loop and while loop : - 

i) Basic: Reverse an Array using temp storage variable space using for-loop without swaping : -

Time Complexity : O(n)
Space Complexity : O(n) # Extrac SPace needed to store the temp array after storing.

i) Basic: Reverse an Array using temp storage variable space using while-loop without swaping : -

Time Complexity : O(n)
Space Complexity : O(n) # Extrac SPace needed to store the temp array after storing.

ii) Reverse an array using Two Pointer with Swaping : swap first and last index and continue till both left and right align at same index we stop then, hence array has been reversed.

Time Complexity : O(n)
Space Complexity : O(1)


iii) Reverse an array using Single Pointer with Swaping : The reversal of array should be inplace -

Time Complexity : O(n/2) = O(n)
Space Complexity : O(1)



'''

#i Using for-loop with temp Storage  -
# Time Complexity : O(n)
# Space Complexity : O(n) due to extra array needed to store for n-items.
def reverseArr(arr):

    n = len(arr)
    # SC : O(n) # temp array used for storing the reversed array data.
    tempArr = []

    for i in range(n-1, -1, -1):

        # print(i, arr[i])
        tempArr.append(arr[i])

    return tempArr


myarr = [3, 9, 3, 5, 2, 1]
print(reverseArr(myarr))
# Time Complexity : O(n)
# Space Complexity : O(n)


#ii) using while loop with temporary Space i.e tempArray=[]  :-

# Approch : Here we use one pointer from backside of original array and keep moving and taking element from one after another to add to new temporay array till pointer crosses the original zero indexed then we stopped.

# Using while-loop with temp Storage  -

# array run from 0 to n-1; where n is size of the array.
myarrr = [9, 5, 7, 1, 8]
# we used j as pointer which start from last from original array
j = len(myarrr) - 1

# Just think loop runs from (n-1) to 0 index; where n is size of array, To reach decreasing order from end to zero index we can either use j >=0 or, j > -1 like in for-decreasing loop range(n-1, -1, -1)


def reverseArr2(arr, n):

    temp = []

    j = n-1 # While loop start from last indexed i.e (n-1)th indexed till 0th index.
    while j >= 0:  # 4> 0 3>0 2>0 1>0 0>=0  -1>0

        # print(j, myarrr[j])
        temp.append(arr[j])
        j = j - 1  # OR, j -= 1 # Update the loop.

    return temp

# Origial Array 
arr = [3,4,5,6,7]
n = len(arr)
print(reverseArr2(arr,n))  # The reversed array will get stored.

# Time Complexity : O(n)
# Space Complexity : O(n) due to extra array needed to store for n-items.



# iii) Better Sultion using two pointer with no extra space with swaping : Optimized the Space Complexity i.e rather using temp=[] array which is an extra space used for reversing array items. we can be ommited -

# Second Apprach : To avoid O(n) Space complexity - and get O(1) SPace Complexity.

# Reverse an Array using Two Pointer : - We fixed two pointer, one at starting index of araay and second at end element of array; and then we swap each two items, after then once swaped done, we pushed the left pointer to one step right and right pointer to one step left and repeat the same swaping and one pointer left and right pointer could align together then we dont need swaping -

ar = [4, 2, 1, 6, 9]  # array run from 0 to n-1 index; n is the size of array.
n = len(ar)
# left pointer 'startP' : which is start index of original array i.e 0.

# v) With Built-in Library Function Approach - reversed(arr) or .reverse


def reverseArrHelper(startP, endP, ar):

    while (startP < endP ) :

        ar[startP], ar[endP] = ar[endP], ar[startP]

        # Swap operation First -
        # temp = ar[startP]
        # ar[startP] = ar[endP]
        # ar[endP] = temp

    # After successfully swaped move left pointer to one step right and right pointer to one step left -
        startP += 1 # Increment the start pointer
        endP -= 1 # Decrement the end pointer


# Origial Array 
arr = [3,4,5,6,7]
n= len(arr)
# Using two pointer concept : one at start index and another at end index -
startP = 0 # Note: It should not be ar[0] else it value will assign as starting index.
endP = n-1 
reverseArrHelper(startP, endP, arr) # The reversed array will get stored.
# reverseArrHelper(0, n-1, arr) # OR

# Let's Print Reversed Array - as original array get modified due to helper function -
print(arr)

# Time Complexity : O(n)
# Space Complexity : O(1) due to no extra array needed to store for n-items.






# iv) Better Sultion using single pointer with no extra space with swaping in terms of 'i' : 

# using one pointer concept -
ar = [4, 2, 1, 6, 9]  # array run from 0 to n//2 index; n is the size of array.

def reverseArrHelper2(i, ar, n):

    # Here, 'i' is left Pointer and will move to right till n//2 -

    i = 0 # While loop start from 0 till one step before n//2 -
    while (i < n//2 ):

        ar[i], ar[n-1-i] = ar[n-1-i], ar[i] # swap(arr[i], ar[n-1-i])

        i = i + 1 # update the increment go till one step before n//2


# Origial Array 
arr = [3,4,5,6,7]
n= len(arr)
# Using One pointer concept : We took 'i' as start pointer -
i = 0 # Note: It should not be ar[0] else it value will assign as starting index.
reverseArrHelper2(i, arr, n) # The reversed array will get stored.
# reverseArrHelper2(0, arr, n) # OR

# Let's Print Reversed Array - as original array get modified due to helper function -
print(arr)

# Time Complexity : O(n)
# Space Complexity : O(1) due to no extra array needed to store for n-items.


# Same using for-loop -

def reverseArrHelper3(l, arr, n):
    # We took 'l' as left pinter -

    for i in range(l, n//2):
            
        # print(i) # will go to 0 , 1 index only as will reach one less than n//2.
        arr[i], arr[n-1-i] = arr[n-1-i],  arr[i]  # Note we replacing ith indexes while looping.


# Origial Array -
arr = [3,4,5,6,7, 8] 
n= len(arr)
# Using One pointer concept : We took 'l' as start pointer -
l = 0 # Note: It should not be ar[0] else it value will assign as starting index.
reverseArrHelper3(l, arr, n) # The reversed array will get stored.
# reverseArrHelper3(0, arr, n) # OR

# Let's Print Reversed Array - as original array get modified due to helper function -
print(arr)



# Time Complexity : O(n/2) = O(n)
# Space Complexity : O(1); No extra space used.



