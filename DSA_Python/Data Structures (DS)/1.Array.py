'''
# What is Array(Static Array) In Programming Language : -

Array/Static Array : An Array can be defined as a storage or container or similar kind of data/items placed in the contiguous memory locations.

Array stores only Hemogenous Elements in it.(Static Array)

Note : Langaugages like C,C++,Java,C# etc. comes with Classic Fixed Sized Array i.e Static Array and We defined the above defination of Classic Array i.e Static Array.

# An Array Can be of Two Type : -
a) Static Array : It the array where size of array is fixed and depends upon user defined size of array. e.g: C,C++,Java,C# Provides Static Array.

b) Dynamic Array : It is the array where size of array is not fixed, it expands or shrinks as per user size. Thus, User doesnot have to define any size of array here. e.g: Python, Javascrpt Provides inbuilt Dynamic Array.


# HomoGeneous and Heterogenous Arrays : -
a) HomoGeneous Array : It contains the elements of same datatype.
b) Heterogeneous Array : It can contain the elements of mixed datatypes.

#Properties : -

i) Array is a linear data structure means items stores in linear-fashion.
ii) Array Items stored in contiguous memory locations. so that our memory get used efficiently.
iii) Array Stores only Homogenous Elements i.e one type of dataype element(either integer or float or string or boolean etc).
iv) Indexing Based : 0,1,2,3,
v) Items Mutabale
vi) Ordered
vii) Duplicates allowed.


# Drawbacks/Disadvantage of Using Array(Static Array) : -

i) Static Array have fixed size to store data.
ii) Needs contigous memory.
iii) Diffcult to insertion and deletion in static array.



# Array Impletation in Python : Though Python doesnot have inbuilt Array but Python Provides list Datatype which works like an Array which is Dyanmic Array in nature.

User-defined Array Can be Implement in Python with three ways -
a) Using Class to define the custom array and its own properties 
b) using Python 'array' module : to work with static Array
c)  using NumPy Array 


import array as arr

myArr = arr.array('i', [2, 4,5 ])
myArr2 = arr.array('d', [2.2, 4.5,5.5])
myArr3 = arr.array('u', ["a", "c","b"])

print(myArr, myArr2, myArr3)
print(myArr.typecode)
print(myArr2.typecode)
print(myArr3.typecode)

# Length of Array -
print(len(myArr), len(myArr2), len(myArr3))


import numpy as np

myArr5 = np.array([4,5,6,"4"])
print(myArr5)



-------------------------------------------------------


# We can Perform some operarion on Each DataTpes or Data Struture : -

myarr = [5,6,17,12,9]

1) Read Operation : To get the value of index no 3, i.e myarr[3]
                    Reading is Fast as we jumped to the exact index(as computer knonw the memory location/address) and we get the value.
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

# Print Even Number from 1 to  Numbers -
# Option1 : - Step Jump to 2 to print all even number[MOST TIME EFFICIENT]
for even in range(2, 11, 2):
    print(even)

# Option2 : -
for num in range(2, 11):
    if num%2 == 0:
        print(num)

# Note :  Time Efficient algorithm Here is OPTION1 coz It takes less no of steps to achive our goal. Thus, Time Efficint Algo.

'''

# Time Complexity :-

Every Problem may have multiple solution, so the steps we write to solve the problem we called it as "Algorithm ".

Suppose, we want to cook any food, then we follow some steps to complete it, Thus that is an algorithm.

To publish a video on vide, we first record it, edit it, setup the content, then pulish it. Thus we followed some steps that is an algorithm for it.

Similary, In Programming Language, To solve any proble we have to follow some steps we called it algorithm.

AND, Where we store our data we called it as data struture.

Note : As One Problme have multiple solution, but we need to pick best one, how would we choose best algorithm -   We pick by Algorithm Analysis : - 


# Once we RUN AN APPLICATION WE WANT : -

a) To may use Less Memory of our device
b) To may use Less Time In Loading application.

We may need both or either one. But, Less Time is very important for any application to load.


# Algorithm Analysis : We optimize the algoritham based on two factors for making algo more efficent : -
a) Space Complexity : To use an algotitm which will take less memory in our device.

b) Time Complexity :To use an algotitm which will take less time in operating.


# To Choose the best Time means Less Time Taken By algorithm : -

i) We do not calcuate time taken by an algorithm by user's machine or CPU. Coz it may vary means RUnTime of execution of code vary from user to user machine.

ii) We calculate TIme of an algoritham or Time COmplexity of an Algorithm using 




# Searching an ELement In sorted array : -
i) Using Linear Search : We search each element in the sorted array from one by one till we do not get our target element.

Ex: myarr = [5,7,9,12,17,20]   (Sorted Array)

target : 17 ---> We go one by one to get our target item.

Best case : If element found at start of array, then it will take one step.
Worst Case : If element at last index of an array, then it will take size of the array step.

Thus, FOr worst Case, as array size increase the num of steps will also increase in the same amount to search.
'''

myarr = [5,-1,5,14,6,3,2,14,23]
target = 23

def linearSearch(myArr, target):
    steps = 0 # To calculate the no of steps for ananlysis time complexity.

    n= len(myArr) # First we will try to get the length of the array.
    for i in range(0, n):
        steps += 1
        if myArr[i] == target:
            print("No of steps for linear search :", steps)
            return i # Returned the index where the target element is found.
        
    print("No of steps for linear search :", steps)    
    return -1 # We returned -1 if target item is not found in the given array.   

# Note : Here we have not used break; coz as soon as we used returned so when algo reached to returned keyword it returned the value to function and funtion will end there. so using break keyword after that doesnot means any sense there.

tagrtIndexed = linearSearch(myarr, target)
print("Linear Search Result Index : ", tagrtIndexed)

'''
ii) Binary Search : Binary Search algorithm searches through a sorted array and returns the index of target value and returned -1 if target value is not found.  

We call binary search coz we divide the array in two parts from middle equally(i.e Bi )

Ex: myarr = [5,7,9,12,17,20]   (Sorted Array MUST NEEDED FOR Binary Search)

target : 17 ---> Let's see how Binary Search works.

Step1 : Find mid_index= start_index + end_index // 2  (To get the floor value); 

if myArr[mid_index] = target_Value  ---> return middle_index.

Step2 : if myArr[mid_index] != target_Value; then we check 

if myArr[mid_index] < target_value  ---> if yes we shift the start_index to the mid_index as left portion value we discard,thus start_index = mid_index

step3 : if above condition false, means taget value is less than mid value, so our value must be lie left-hand side, so we discard right hand side values and shift end_index to mid_index means now our mid_index become end_index.
end_index = mid_index

step4 : again we repeat step1 i.e we find new mid_index from updated start_index and end_index and follow step2 and step3. This will continue till we do not find myArr[mid_index] = target_Value  ---> return middle_index.

So, we use while loop with condition 


  
'''

def binarySearch(myarr, target):
    steps = 0 # To calculate the no of steps for ananlysis time complexity.

    start_index = 0 # lower_bound_index
    end_index = len(myarr) - 1  # upper_bound_index

    while start_index <= end_index :

        steps += 1

        mid_index = (start_index + end_index) // 2

        if myarr[mid_index] == target :
            
            print("No of steps for binary search :", steps)
            return mid_index # Returned index where target value mactched with mid_index value.
        
        if myarr[mid_index] < target :
            start_index =  mid_index + 1 # Shift start_index to one step ahead of mid_index
        else:
            end_index = mid_index - 1 # shift end_index to one step before of mid_index.

    print("No of steps for binary search :", steps)
    return -1 # If target value not found, returned -1 index.

mera_aarr = [3,4,5,23,27,33,46]            
x = 0

print("Binary Search Result Index : ", binarySearch(mera_aarr, x))


'''
# What is Time Complexity : -

# Time Complexity : It the measure of how the running time of an algorithm increases with the size of the input data.

# Time  Complexity measure not on the basis of the respective CPU machine or runtime of an algorithm whereas it is measure using "Big O Notation i.e O(<dependednt_variables>)"

# Big O Notation : It is a concept to mesure time-complexity of any algorithm in program. It can also called as Order of something O(<something>).

# How Big-O We represent in DSA Algorithm : -

i) O(1) : Constant Time Complexity 
ii) O(log n) : Logarithmic Time 
iii) O(n) : Linear Time  
iv) O(n logn ) : Linearithmic Time
v) O(n^2) : Quadratic Time
vi) O(2^n) : Exponential Time
vii) O(n!) : Factorial Time

Note : O(1), O(log n)  ----> Best Time Complexity
        O(n)  ---> It's Okay Time Complexity
        O (n log n)  ---> Try to make it better
        Rest   ---> Worst Time Complexity (Application is not scable as soon as 5 users server okay as soon as 1000, server will struggle. )


# Searching In Linear Search : When we have 5 values ---> 5 steps we take.

    We take Worst Case Senario for searching like element at the last or element is not found in the array   ----> TIme Taken --->   O(n)

    Here, n --->  No of elements in the array.

READing in Linear Search : arr[3] = Value ---> Independent of size of the array  --->   Time take here in reading is constant ----> O(1)

# In BInary Search, Searching Time Complexity : As No of Inputs i.e Data Increases with each steps Data getting halfed.

betweeen the O(1)   --- O(log n)   --- O (n)

log 8 = 3(Steps) OR, log 16 = 4 (Steps, only 1 step increases)

'''
