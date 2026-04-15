'''

#2) Using Recursive Approch :  All are same above but Space Complexity gets increase here due to recursive call stack :-

#i) Reverse an array using Recursion with two pointers : This will be done using Parameterized Recusion Way Rather Function Recursion Way -

# Generally Reversion array without extra space with two ponters : In this apProch we keep pointer at zeroth index and (n-1)th index and swapped and move the left pointer to step right and left pointer to one step left and again swap and repeats till it reaches equal both pointers or crossed each other.

Time Complexity : O(n) 
Space Complexity : O(n/2) = O(n)

Note : This Recursive approach uses O(n) auxiliary space due to the recursion call stack. 

# Concept is we are increasing the left and right pointer so we take as argument in recursive call and runn till left >= right --> left the recursive call (as left <= right ---> is True Condition.)

# 
f(left, right){

    if (left >= right){
        return;
        }

    swap( arr[left], arr[right] )

    # call again recursive call -
    f(left+1, right-1);

}

# My Original Array -
arr = [4,5,3,1]
n = len(arr)
# left  = 0 # indexes
# right = n-1 

# call the main recursive function -
# f(left,right) OR, f(0, n-1)

# Let's Print the array ---> which got modified as array is mutable DS -
print(arr) # Swapped Array Output.




#ii)  Reverse an array using Recursion with single pointer with swaping concept in terms of 'i' and length 'n' :-

Time Complexity : O(n/2) = O(n)
Space Complexity : O(n/2) = O(n)

Note : Time Complexity: O(n)The function processes each element of the array exactly once. It makes a total of (n/2) swaps.

and, This Recursive approach uses O(n) auxiliary space due to the recursion call stack. coz For an array of size 'n', there will be approximately (n/2) function calls waiting on the stack at the deepest point of the recursion.



ar = [3, 4, 1, 0, 9]
# Ealier, Swap between '0' index and n-1 index' ; n is size of the array.

# Swapping Concept in terms of 'i' :   i  and  n-1-i
Now, Swap between 'i' index and 'n-i-1' index' ; n is size of array and i is starting index of swaping starts.
Ex: ar = [3, 4, 1, 0, 9]
0 -> 0
4 -> n -1

0, 5-1-0  --> 1, 5-1-1 ---> 2, 5-1-2
0, 4  --> 1, 3 ---> 2, 2

Here, n = 5 
if n/2 = 2.5 = 2 i.e n//2 so run loop till from 'i' to 'n//2'

Time Complexity : O(n/2) = O(n)
Space Complexity : O(n) due to recursive call stack.

# Takig 'i' as only pointer which will move from left to right and run till half of the array size. 
# In Recursive function call we repeate the recusionn funtion till half of the array size by stopping with 
i < n//2  --> True Condition ; so false condtion would be i >= n//2; stop even get equal.

f(i){
    if i >= n//2{
        return;
        }
    
    swap( arr[i], arr[n-1-i] )

    # Update the Recursive call for next step and get stopped when reaches n//2 -
    f(i+1);

}

# My Original Array -
arr = [3, 1, 7,2]
startPointer = 0
# call the main recursive function -
f(startPointer) or f(0)


# Let's Print the array ---> which got modified as array is mutable DS -
print(arr) # Swapped Array Output.

'''

# Recusive Approch1 : Two Pointer Concept with swapping  - 
# Time Complexity : O(n/2) = O(n)
# Space Complexity : O(n) due to recusive call stack.

# Original Array -
def helper(leftP, rightP, arr):

    if leftP >= rightP :
        return

    arr[leftP], arr[rightP] = arr[rightP] , arr[leftP]

    # Repeate recursive call -
    helper(leftP+1, rightP-1, arr)


#Original Array 
arr = [20,30,40,50,60, 70] 
n = len(arr)
helper(0, n-1, arr ) # Start Pointer is 0 and end Pointer is n-1.

# Let's Print the Original Array - which got reversed now -
print(arr) 


# Note : This approach improves on the previous one by reversing the array in-place, avoiding the need for extra space. It uses two pointers to simultaneously traverse the array from both ends, swapping the elements until the center is reached. This way, we avoid creating a new array and perform the reverse operation efficiently using constant space.


# Recusive Approch2 : Single Pointer Concept with swapping - 
# Time Complexity : O(n/2) = O(n)
# Space Complexity : O(n) due to recusive call stack.

# We take 'i' as left Pointer -
def helper2(i , arr, n):

    if i >= n//2 :
        return

    arr[i], arr[n-1-i] = arr[n-1-i] , arr[i]

    # Repeat recursive call -
    helper2(i+1, arr, n)


#Original Array 
arr = [20,30,40,50,60, 70] 
n = len(arr)
helper2(0, arr, n ) # Start Pointer start from 0th indexed.

# Let's Print the Original Array - which got reversed now -
print(arr) 