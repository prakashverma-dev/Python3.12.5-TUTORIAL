#  Bubble Sort : - Pushes the maximum to the end of the array by each iteration adjacent swapping. Oposite of Selection sort(pick lowest and put it to front)

'''  

13, 46, 24, 52, 20, 9

Step1 : 13 and 46 compare 13 is sorted 46 dont do anything
13, 46, 24, 52, 20, 9

Step2 : Move to next, 46 and 24 ajaacent compare 46 is not sorted move 24 to 46  i.e swap ajacent elements. 
13, 24, 46, 52, 20 , 9

Step3 : 52 and 20 Adjacent

13, 24, 46, 20, 52 , 9

Step3 : 52 and 9 Adjacent

13, 24, 46, 20, 9, 52


Here, After first iteration max element reach to last of array. Hence, 52 is sorted.

#Round2 : -

13, 24  --> No swap
24, 46  --> No swap
46, 20  --> yes swap
13, 24, 20, 46, 9, 52

46, 9 --> Yes swap
13, 24, 20, 9, 46, 52

46, 50 --> No Swap(Optioal Only we rech till n-1-1 in second iteration.)



#Round3  :-

13, 24 --> No Swap
24, 20 --> Yes Swap
13, 20, 24, 9, 46, 52

24, 9 --> Yes Swap
13, 20, 9, 24, 46, 52

24, 46 --> No Swap

Rond4 : so on...



Note : After each Iteration of outer loop, one element get shifted to end of array. So Iteration i,e Outer loop must run from -
Outer Loop -
0 to n-1
0 to n-2
0 to n-3
0 to n-4

0 to 1  --> Last Iteration

Outer loop run from n-1 to till 1 index.

Inner Loop- At each iteration we need to compare two adjancent element and if first is greater than next elment then we swap it.
Inner LOop must run from 0 to one less than (n-1) i.e till n-2. coz for last next element to check will give error. 

 
# Psecudo

for (i = n-1; i>=1 ; i--){ # Run from n-1 to till 1 index.

    for (k = 0 ; k <= n-1-1; k++ ){ # Run from 0 to till n-2 index.

        if arr[k] > arr[k+1]{
            swap(arr[k], arr[k+1])
        }
    }

}





'''



def bubbleSort(arr):

    n = len(arr)
    for i in range(n-1, 0, - 1): # run from n-1 till 1 index. 

        for k in range(0, (n-2)+1): # run from 0 to till n-2 index.
             
             if arr[k] > arr[k+1]:
                #  swap -
                arr[k], arr[k+1] = arr[k+1], arr[k]

    # Finally the array will be sorted with bubble sort.
    return arr


print(bubbleSort([13, 46, 24, 52, 20, 9]))



# Time Complexity : We use two loops so O(n^2) Time Complexity. as In Outer Loop we use that for the no of iteration and Inner loop for each iteration compare two adjacent values and swapping.

'''  
n
n-1
n-3
n-4
.
.
.
1

n + (n-1) + (n-2) + ..... + 1 = sum of natural no = n(n+1)/2 = n^2/2 + n/2

TIme Complexity : O(N^2) For Worst and Average Time Complexity.

2 3 5 15 20  ---> Best Case

# Bubble Sort Optimization : - We can optimize algorithm further for Bubble sort for Best Case when array is already sorted. i.e -
2 3 5 15 20  ---> Best Case(array already sorted)
In First Iteration --> We didnt swap any, so we assume that array is sorted.Thus we stop the algorithm to check from next iteration.Hence Our Time Complexity will be only single Iteration i.e O(n) for Best Case.

O(N) ---> Best Case Time Complexity for Bubble Sort.
O(N^2) ---> Worst and Average Case Time Complexity for Bubble Sort.
 



'''

