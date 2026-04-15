
'''  

Linear Search : From Given array, We need to tell first occurance of that given element index and if not occured even once return -1.

arr [] = [6, 7, 8, 4, 1]; num = 4  ---> 3
arr [] = [6, 7, 8, 4, 1]; num = 10 ---> -1

# First Occurance from left side of array -
for(i=0; i<n; i++){

    if (arr[i] == num){
        return i
    }


}

return -1
# Last Occurance from Righ side of array - Loop reverse
for(i=n; i<= 0; i--){

    if (arr[i] == num){
        return i
    }


}

return


# 





'''


def linearSearch(arr, n, val) :
    #write your code logic 
    for i in range(n):

        if arr[i] == val:
            return i

    return -1