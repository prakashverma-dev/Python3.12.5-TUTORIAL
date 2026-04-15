'''   
# Rotate the array by d place right -


arr = [ 1,2,3,4,5,6,7] ; n = 7 and d = 2(rotate 2 step left)

resulantArr = [6,7,1,2,3,4,5]

Brute-Force -

Step1 : Store last elements in temp arr 
Step2 : Shift array to right 
Step3 : Place the temp array in front.

Optimum Approch -(Algorithm is same for both left Rotate and Right Rotate )

arr = [ 1,2,3,4,5,6,7] ; n = 7 and d = 3(rotate 3 step left)
resulantArr = [5,6,7,1,2,3,4]

Step1 : Reverse First half 
reverse(arr, 0, (n-d) - 1)  --> [4,3,2,1]
reverse(arr, n-d, n-1)  ---> [7,6,5]
[4,3,2,1] [7,6,5]
reverse(arr, 0, n-1)  ---> [5,6,7,1,2,3,4]

'''

def rightRotate(arr, k):

    n = len(arr)

    # # Handle k when k > n
    k = k%n
    # print(k) 


    # Step1 : Slicing last elements -
    temp = arr[(n-k):] 

    # Step2 : Reversing the loop and placing before d item into current last item and decreaing so far -
    for i in range(n-1, -1, -1):

        arr[i] = arr[i-k]  
    
    # Step3:Putting in the front -
    for i in range(0, len(temp)):

        arr[i] = temp[i]

    return arr


arr = [1,2,3,4,5,6,7]
d = 10
print(rightRotate(arr, d)) 



# Optimal Solution -

def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        reverse(nums, 0, (n-k) -1)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)

        
def reverse(arr, s, e):

        while s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1

arrr = [1,2,3,4,5,6,7]
k = 3
rotate(arrr, d)
print(arrr)  