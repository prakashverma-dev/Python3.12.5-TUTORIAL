'''   
# Hashing : It is one of the most important topic in DSA.

# Defination of Hashing : Prestoring and Fetching when requires.

Hashing is the process when we declare an empty array of n+1 size with bydefault '0' elements each, which will known as hashing array and later as per freqency count(the number of times each element appears in the array), we consider array's item as hasharry index ordering to increase the value of hasharray elements corresponding indexed.

Note : IN hasharray, We will map  array's item as hasharray indexing for increasing the indexed value for hasharry when it found again with hasharr[arr[i]] += 1 or hasharr[item] += 1 and lastly we return the hasharray element as freqency count by return hasharr[item].

"counting the frequency of any element present in the array" --> if it not present we return 0 and if it is present we return the no of times that element is present in the array of total looping.


arr = [1, 2, 1, 3, 2]

1 ---> 2 times
3 --->  1 times
4 --->  0 times

# Ways1(Brute Force Approch) : using Counter variable //linear Iteration we doing -

f(item, arr){

    count = 0
    for(i=0; i<n; i++ ){

        if(arr[i] == item){
            count = count + 1
            }
    
    }
    return count;

}

print(f(arr = [1, 2, 1, 3, 2],  2)) # 2

Time Complexuity : O(n): running the loop for n-times.
Time Complexuity : O(1)


# Way2 : Hashing Approch -
Here, we create the prefetch array of input size and by default we store zero in all the element.
'''

# Ways1(Brute Force Approch) : using Counter variable, looping through each items and if it is matches with desire item we increase the coounter value by +1 -


def checkFeqNaive(arr, n, item):
     
      count = 0 # Next we gonna use hasharr.
      for i in range(0, n):
            if arr[i] == item:
                  count += 1

      return count


# Input -
# 5
# 1 3 2 1 3
# 5
# 1
# 4
# 2
# 3
# 12

# Ways2(Array Hashing Approch) : using Array Hashing Approach, here we firstly assign a hasharray with zero items all with any no of array size as depends on maximum target eleement to check, that we dont know we could take max 10^6 array size in worst case.

'''
hasharr = [0] * (10**6)  --> In python to create user defined array size.
hasharr = [ 0, 0 , 0 , 0 , 0 , 0 ]
            0  1   2   3   4   5   ---> indexs of hasharray

mainArr = [10, 5, 10, 15, 10, 5]
Now, -
# Item : 10 to be checked(we made hasharray indexed as our target num to be search if found increase the corresponding item value from 0 to 1 and keep doing till end loop.)
10 -->
hasharr[item] = 1 (from 0 to 1) # at 10 index of hasharray increase the value 1
5 -->  
hasharr[arr[i]] = 1

10 --> come again
hasharr[arr[i]] = 2 at index arr[i] means the main array element corresponding to hasharr indexed values.






'''
def checkFeq(arr, n, item):

        # print(arr, n, item) # here k is item we need to check 

        # Creating a prehash array of n+1 size -
        hasharr = [0]* 13   # consider 13 size array. 
        # hasharr = [0]* (10 ** 6)   # consider 10^6 hasharray size.
        # hasharr = [0]* pow(10, 6 )  # consider 10^6 hasharray size.
        # hasharr = [0] * (max(hasharr) + 1)  # we could max(hasharr) to find max element then we assign size as one +1.

        for i in range(0, n):

            # item of main array i.e arr[i] corresponding to hasharray indexed value to get updated as per times each item appears. For ex : arr= [1, 3, 2, 1, 3]
            # 1 --> +1
            # 3 --> +1
            # 2 --> +1   
            # 1 --> +2   
            # 3 --> +2   
            hasharr[ arr[i] ] += 1   

        # return hasharr 
        return hasharr[item] # after each iteration we will return the value cooresponding to target item.



# Note : We can declre maximum size of array we can declare upto 10^6 inside main or 10^7 to globally.



# Ways3 : In Number hashing we can hasharray with HASHMap of python ie dictionay to solve storing freqeuncy is optimized way with we can store any number of size we do not need to define size pre.
# 
#   
# using Hashmap (dictionary in python )

# In HashArray, we used indexing as reference to increase frequency value.
# In HashMap i.e Dictionary, we will use dict's 'key' as referenc to increase corresponding its value for freqency increase. It's easy coz in hashmap we dont have to define size of hashmap, we save space of hashmap as only stores the key value which value we gonna check.

 
def arr_frequency(arr, n, item):

    hashmap = {} 
    for i in range(n):
        hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
    
    return hashmap.get(item, 0)   # Safe return if 'item' is not present.


# Note : .get() method use in dictionary to access value corresponding to that 'key' value like square bracket use, ex : 
# dict = {}
# print(dict.get(0, 0))
# get(key, <default_value>) : Here, we assign any default value if key is not present in the dictionary.
 
  

# Way4 : using defaultdict (here default value errror will not throw )

from collections import defaultdict

# def arr_frequency(arr, item):
#     hashmap = defaultdict(int)
    
#     for num in arr:
#         hashmap[num] += 1
    
#     return hashmap[item]




'''        
# Output -
2
0
1 
2
0

'''

# Input Driver code -
n = int(input())
arr = list(map(int, input().split(" ")) )

t = int(input()) 
# print(n, arr)
# print(t, type(t))

for _ in range(0, t):
    item = int(input())
    # print(checkFeq(arr, n, item )) # will loop till k doesnot ends. 
    # print(checkFeqNaive(arr, n, item )) 
    print(arr_frequency(arr, n, item)) 


