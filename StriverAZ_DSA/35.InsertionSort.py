'''   

Insertion SOrt : Takes an element and place it in its correct position.

14, 9, 15, 12, 6, 8, 13

Step1 : Size1 Array : Start with Index 0 i.e 14 and and it is sorted with size 1 array
14, 9, 15, 12, 6, 8, 13

Step2 : Size2 Array : increase the size of arraty till index 1, and look if it sorted or not by looking at end element if not place it to correct position if last element < just previous element.
9, 14, 15, 12, 6, 8, 13

Step3 : Size3 Array : Is 15 at correct postio, yes it is at correct postion; here 15 < 14 become false so doesnot further check.
9, 14, 15, 12, 6, 8, 13

Step4 : size4 Array : is 12 at correct postion --> No, then check 12<15 true swap --> 
9, 14, 12, 15, 6, 8, 13

12<14 true swap -
9, 12, 14, 15, 6, 8, 13

12 < 8, false so no further swap.

STEP5: size5 array : is 6 at cirrect postion, no --> check 6 < 15 --> swap -->
9, 12, 14, 6, 15, 8, 13

6< 14
9, 12, 6, 14, 15, 8, 13

6<12
9, 6, 12, 14, 15, 8, 13

6<9
6, 9, 12, 14, 15, 8, 13

Step6 : size6 array : is 8 at correct postion, no --> 

6, 8, 9, 12, 14, 15, 13

Step7 : size7 array : is 13 at correct postion, no ---> 

6, 8, 9, 12, 13, 14, 15

step8 : size8 array : is 15 is at correct postion, yes coz 15<14




Pesudo Code - 

for(i = 1 ;  i<= n-1 ; i++){

    key = arr[i] # The first element to check; which we mentioned it as key value.
    j = i - 1 # j index intialized with one less than i index.

    while (j >= 0 && key< arr[j]){

        swap(arr[j], arr[j+1])

        j = j - 1;
    }

}

 

30 20 40 10
j      i

'''

def swap(a, b):
    return b, a

def insertionSort(arr):
    n = len(arr)

    for i in range(1, (n-1)+1): #1 index to n-1.
        
        checkElm = arr[i] # First Element start to be checked.
        k = i - 1 # k is index which always checks less than checkElem index.

        while k >= 0 and checkElm < arr[k]:

            # swap(arr[k], arr[k+1])
            arr[k], arr[k+1] = arr[k+1], arr[k]

            k = k - 1 # To decrement

            print("Loop Runs")
             
    print(arr)

# insertionSort([14, 9, 15, 12, 6, 8, 13]) # Worst and Average Case
insertionSort([1, 2, 3, 4, 5]) # Best Case (while Loop never runs for this.)

'''
# Time Complexity : 

# Worst and Average Case -
 5, 4, 3 2, 1
# for each iteration while loop runs n - times i.e 

1 + 2 + 3 + 4 + n-1 = n(n+1)/2 = n^2

O(n^2) Worst Case
O(n^2) Average Case

# Best Case -
1, 2, 3, 4, 5

for Best Case, while loop never gonna run so only runs the for loop i.e outer loop hence it runs till n-time. This BigOf(n) time Complexity for Best Case.

O(n) Time Complexity for Best Case.(coz no swap happend coz all are in correct order.)





'''