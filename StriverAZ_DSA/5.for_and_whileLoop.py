
# for and while loop : i) For loop use mostly when we want to loop over any task again and again with know where to where it will loop.

# ii) For while loop, it also loops but here we dont known

# Example with Working Logic :- 

# 1) for-loop : Unlike other programming languages, for-loop is runs a bit different in python but achieve the same task though it makes us easy to run; here we use range() function to descripe from where to where we want to run for loop.
# Note : we can run for loop over any iteratable object in python which directly give us the values.

'''
Syantax : 

for <A_VARIABLE> in <SEQUENCE_OBJECT>:

    # Print("Perform Task/Do a Pushup")

# SEQUENCE OBJECTS : [1,2,3,4]
                     (1,2,3,5)
                      range(1,4)
                      

range(1,4) SEQUENCE OBJECT : It is use to display some range number starting from 0 bydefault to just less than given value.

# range(0,10,1) === range(10)  ---> Here range runs 10 times i.e from 0 to 9.
# range(0,10,2) === range(0, 10,2 ) It is must here --> Here range runs 5 times i.e 0 to 9 with step of +2.

# for-loop over an array of size -

from array import array
arr_int = array('i', [1, 2, 3, 4])
size = len(arr_int)

# range(0,size, 1) ---> +1 step i.e default case.
# range(0, size, 2) ----> +2 step jump of iteration
# range(0, size, -1) ----> -1 step jump down of iteration i.e decreasing loop
# range(0, size, -2) ----> -2 step jump down of iteration i.e decreasing loop by step 2.

# Note : 'Step' in for-loop is python way to jump the iteration steps how fast using range() function like - 

'''

#Note : What is Indexing in array : It's very important that before iterating over any data structure, one should get the size of the DS, so Iteration will take place from 0 to n-1, where n is the size of that data structure.

# size = len(arr_int)

from array import array
arr_int = array('i', [1, 2, 3, 4])

size = len(arr_int)
for i in range(0, size):  # it loop from zero to just less than size value. 
    print(i) # 0 1 2 3    ---> index of array
    print(arr_int[i]) # 1 2 3 4    ---> value corresponding to indexing.

for _ in range(0, 10, 2):
    print("Ram Sita") # we use _ when we dont want iterable number to use in for-loop.
# Here range runs from 0 to 9 i.e 10 times total prints "Ram Sita".

for item in [3,4,5]:
    print(item) # Directly can print item iterating direct over list.

for num in range(12, 15):
    print(num) # It will print 12, 13, 14.

# Decreasing Loop/Reverse Looping over an array with its input size -
# NOte : We know over an array element index goes from 0 to n-1; where n is size. So for reverse looping -
# size - 1     ---> n -1 loop starts
#  - 1     ---> just before -1 i.e till index 0.

from array import array
arr_int2 = array('i', [8,9,10,11])

n = len(arr_int2)
for i in range(n-1, -1, -1) : # the third -1 for jumping step down by 1.
    print(i) # 3 2 1 0
    print(arr_int2[i]) # 11 10 9 8 


#2) While Loop : - Here while loop more focus on condtion as primary means untill while loop condition is TRue, it runs and when it get false it stopped.

pushup = 0    #---> Initialization done before start of while loop must.
while pushup <=15:  #---> Condition /Conditon of while loop to stop when/ means ending loop condtion.
    print(f'{pushup}.Did a pushup')  # -->Operation /Perform the repitive task inside while loop

    pushup = pushup + 1  # --->Updation/ Update the initiation value for next looping condition to be checked. 

# NOte : Here while loop run 16 times i.e from 0 to till 15 i.e total

# Note: remember to increment initialization, or else the loop will get stuck in infine loop and terminal gets hanged.

# Best Use-case of while loop : When we are more concern over the ending condtion of the loop, we use use while loop. Example : taking password from user till it is not correct -

pw = input() # works only for first time password taking.

while pw != "rwdy":  # Condition to match our stored password or not; if matched exist the while loop as it becomes Flase while loop.
    print("Incorrect Password, Please Enter Correct Password!")
    pw = input() # updation of Condition value to re-check else it will take old pw value.



print("Congrats.. You Have Succefully Entered password Correctly!")




# use of 'break' statement -
# Problem : Find the given key value in the list and assign -1 if not exist any key value -
lst = [2, 3, 4, 5, 17 ,23, 29, 31]

k = 17 # our key value to loop in the list
ans = -1 # Assigned -1 index if not found any key value; already we assumed, if found we just simply update this ans variable.
n = len(lst)

for i in range(0, n): # from 0 to n-1 looping
    if lst[i] == k:
        ans = i
        break # break statment as soon as encountered it exist the current for-loop and move to the next line.

print("The Key value index is : ", ans) # if found we get the index; if not we will get -1 as index.

# This is also known as LInear Search having Linear Time Complexity i.e O(n).




# ------------------------------------------------------------------------------

# Better Understanding of while loop and continue statement : -


# while loop : a while loop is used to repeatedly execute a block of code as long as given while loop condition is true.

# Most Use : Use while loop when you exactly dont know beforehand that "how many times you wanna run the loop".

i = 1
while i < 5:
    
#     print(i) # 1 2 3 4
    i += 1
    print(i) # 2 3 4 5

# Note : if you print index value after updating increment value it prints the updated i value for current looping.

# use of continue : as soon as 'contine' encounter it immediately jump to the next round of iteration of loop with ignoring whatever next of continue statement for the loop.

i = 1
while i < 5:

    i += 1
    continue
    print(i) # Will not print anything as each time loop get continued with ignore forehead statements.


                                         



