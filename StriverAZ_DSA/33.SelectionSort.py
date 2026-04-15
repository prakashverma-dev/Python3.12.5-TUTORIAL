
'''
# Selection Sort : -

13, 46, 24, 52, 20 , 9     ---> we select minimums.

Step1 : Look who is minimum, and take that minimum and place it over first element of array with swap with each other i.e 13 to that min position.

9, 46, 24, 52, 20, 13 ( HEre 9 is sorted.)

Step2 : Now, Except sorted element; 13 is the now minumum --> put 13 to first place by putting 46 to 13 position.

9, 13, 24, 52, 20, 46 (Here, 9, 13 are sorted.)

Step3 : Now, Except sorted elements i,e 9 and 13; 20 is now new minumum --> put 20 to first place by putting 24 to 20 position.

9, 13, 20, 52, 24, 46 (9, 13, 20 are sorted.)

Step4 : Now, Except sorted elements i,e 9, 13, 20;  24 is now new minumum --> put 24 to first place by putting 52 to 24 position.

9, 13, 20, 24, 52, 46 (9, 13, 20, 24 are sorted)

Step5 : Now, Except sorted elements i,e 9, 13, 20, 24 ;  46 is now new minumum --> put 46 to first place by putting 52 to 46 position.

9, 13, 20, 24, 46, 52 (9, 13, 20, 24, 46 are sorted)

Step5 : Now, 9, 13, 20, 24, 46 are sorted, only one element left at right side so always one element is sorted, hence Emtire array's elements are sorted.


Note : In Selection Sort, We get the minimum at each step and swap it. Hence, it takes n-tim


# Psesedo Code : -
Swap at index i = 0 and minimum index range 0  to n - 1
Swap at index i = 1 and minimum index range 1  to n - 1
Swap at index i = 2 and minimum index range 2  to n - 1


Swap at index i = n - 2 and minimum index range (n-2) to n - 1


Outer loop run from i = 0 to n-2 coz we want to do swaping till one index less than last index coz last index item is already sorted.

for ( i = 0 ; i <= n-2 ; i++){

    minIndex = i # Suppose i index is min element.

    Inner Loop to find the minimum index value after each iteration from j = i to n-1 range.

    for (j = i ; j <= n -1; j++){
    
        if(arr[j] < arr[minIndex]){
            minIndex = j 
        }
    }

    # Finally when we found the minindex - swap with current ith index with minIndex -

    arr[i], arr[minIndex] = arr[minIndex], arr[i]


}



'''

def selectionSort(arr):

    n = len(arr)

    for i in range(0, (n-2) +1): # i = 0 to i = n-2 till run.
        
        minIndex = i # Assummed min index intially is 'i' index. Note : We are finding smallest index with cooresponding index wise.
        for k in range(i, (n-1) +1 ): # k = i to k = n-1 till run.

            if arr[k] < arr[minIndex]:
                minIndex = k
            
        
        # Now we got minIndex after first iteration, lets swap now with current i and minIndex -
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    
    return arr # Finally array will be sorted.



print(selectionSort([13, 46, 24, 52, 20, 9])) 

'''
# Analysis Time Complexity : -

For each outer loop inner loop runs n-times, so it will take  N * N time.

O(N^2) Time complexity for worst TC, Best TC, Averge TC.




'''