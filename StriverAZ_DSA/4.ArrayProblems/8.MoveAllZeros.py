

'''

arr = [1,0,2,3,2,0,0,4,5,1]

result = [1,2,3,2,4,5,1,0,0,0]



'''
'''  
#Brute force :-  
Step1: Pick all non-zero element from main array and put it into a temp array.
step2 : Now, Fill the remaining items of original size with zero element.


'''

#I. Brute Force  -

def moveZerosBrute(arr):
    n = len(arr)
    temp = []

    for i in range(n):
        if arr[i] > 0 :
            temp.append(arr[i])


#  filling zeros to remaing items in temp -
    nonZerolen = len(temp)

    for i in range(nonZerolen, len(arr)):
        temp.append(0) 

    return temp
        
arr = [1,0,2,3,2,0,0,4,5,1]
print(moveZerosBrute(arr))

# [1,0,2,3,2,0,0,4,5,1] i = 0; j = 0 
# [1,2,0,3,2,0,0,4,5,1] i = 1; j = 1
# [1,2,3,0,2,0,0,4,5,1] i = 3
# [1,2,3,2,0,0,0,4,5,1] i = 4


   
#II. Brute Force  - with making temp array size as original array size with filling zero elements by default -
def moveZerosBrute2(arr):

    n = len(arr)
    temp = [0]*n

    j = 0 # To fill all places of temp array.

    for i in range(n):
         if arr[i] != 0 :
             temp[j] = arr[i]
             j+= 1

    
    # Fill it back in original Array //OPTIONAL or return 'temp' array.
    for i in range(n):
        arr[i] = temp[i]

    return arr

arr = [1,0,2,3,2,0,0,4,5,1]
print(moveZerosBrute2(arr))




#III. Optimal : Two Pointer approch : check non-zero value and if it it found swap with 'j' index and increment j index to keep track on zero elements.

def moveZeros(arr):
    n = len(arr)
    
    j = 0 # To check if it is zero or not.
    for i in range(n):

        if arr[i] != 0:

            arr[i], arr[j] = arr[j], arr[i]

            j += 1

    return arr

arr = [1,0,2,3,2,0,0,4,5,1]
print(moveZeros(arr))


# Time Complexity : - O(n) at worst we move all zeroes to end in linear time.
# Space Complexity: O(1), no extra space is used.