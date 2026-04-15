'''
Arrray : -

nums [5, 6, 17, 12, 9]
    
# In Array We can perform follwoing operation -


a) READ  --->nums[0] (Direct jump to memory location in array; Reading is easy and fast) --> O(1)
b) Search  ---> O(n) for linear search and O(logn) for binary search.
c) Add ---> O(n)
d) Delete ---> O(n)


Search : We searching for values we dont know at which index or location our value is present.
            nums[0]  --> nums[1] ---> nums[2] ---> nums[n]

 Searching is not easy and not fast; depends on no of total elements.

Add/Insertion Item : At the end item insertion is easy as we get the size of array and we can insert to end but adding value in between in linear DS: suppose want to add at 2nd index then we need to add a new block to end and move all element to one step next and add the desire element at our 2nd place.

Insertion is not that easy depends where we inserting; if it is at the end then easy but if it is at intermiddiate then its deoends on no of elements in the array.

Deletion : Deleting from end is fine but deleting from intermediate postion is tricky like we need to shift one step down.Thus it depends the no of elements after that index if it is zero fine but if more no then we need that no of left shift each time.




# We can Perform some operarion on Each Data Struture : -

myarr = [5,6,17,12,9]

1) Read Operation : Suppose, To get the value of index no 3, i.e myarr[3]
    
    Reading is Fast as we Directly jumped to the exact index(as computer knonw the memory location/address) and we get the value.

2) Search Operation : We do not search for index, we search for a value from array one by one from index 0 to last index untill we do not get.

Here, we are basically searching all elements if item present at last index.

Suppose, array size is 1000, then time taking in searcing will take much time as we assume we search till last item.

Ex: Seaching Item 9 in the myarr.

3) Insert Operation : Adding value at the end of arrau location is easy but adding value at intermidiate location we need to have a vacant location which we create by shifting all right side element to one step ahead.

Thus, Time taking in Insert Operation at last index is easy.

But, Time taking in insert opertion at intermidiate location depends upton how many items are present at the right side coz one step shift has to do by each item.

4) Delete Operation : Deleteing an item from array is also easy if item at last index but if item we do from intermidiate index number.

Then, Time taking in Delete Operation at last index is easy.

And, Time taking in delete operation at intermidate location depends how many items present at the right side of the deletion item coz as soon as intermidiare item delete all values from right side shift to left side by step.


# Let's Understand Why "TIME TAKEN BY EACH OPERATION" Is Important :-

i) Time taken by any operation we do not calculate by respective CPU and Machine coz it vary from users to users. Thus, Runtime of a code doesnot decide the Time taken or speed of the code or Time COmplexity of the code.

ii) No of steps is very important in any operation, as more steps will take more time will take to perform the operation and We really concentrted upon the less time for any operaration.

iii) No of steps takes by a code to execute the operation, directly proportion to time complexity of the code.

'''

# Print Even Number from 1 to 10 Numbers -
# Option1 : - Step Jump to 2 to print all even number[MOST TIME EFFICIENT]
for even in range(2, 11, 2):
    print(even)

# Option2 : -
for num in range(2, 11):
    if num%2 == 0:
        print(num)

# Note :  Time Efficient algorithm Here is OPTION1 coz It takes less no of steps to achive our goal. Thus, Time Efficint Algo.
