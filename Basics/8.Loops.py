

# a) for Loop : In Python, there is only one primary type of for loop i.e for-in loop which iterate over any sequence of elements(like range(), string, list, tuple, set, dictionary, or any iterable objects) always.

# i) for-in over range() function /Or, Standard Looping : we use range() function to set the range of looping which always returns the sequence object with bydefault indexing start from zero. THus, Unlike other language we do not to set starting index and updating index with checking condition, it all does by range() function inbuilt -


# Syntax : for index in range(0,10,2):
                    # print(i) # will get indexing from 0 to 9 with stepping +2 each time.
# Note : range(start_index(0 bydefault), stop_index(excluded i.e less than), steps(+1 increment bydefault i.e i++ or i = i+1 or i += 1 ))

# Here,  start_index =(optional) starting value of indexing( Default is 0 )
# Here,  stop_index =(Required) loop stops before reaching this value i.e less than this value or before ending point.
# step = (optional) +1 for Increment By +1 each time(Default is 1)
#                       or
#        -1 for Decrement by -1 each time(Default is 1)

#: a) Increment Looping/Positive Steps -
for index in range(0, 10, 2):
  print(index)  # 1, 3, 5, 7, 9

#: b) Decrement Looping/Negative Steps -
for index in range(10, 0, -2):
  print(index)  # 10, 8, 6, 4, 2

# Note: For Decrement Loop, use must start index wil upper boundary and go to less than given boundary with providing steping value as negative as -1 or -2, tho bydefault it is +1.

# Note : We can give only ending point as Required to range() function, ex: range(5) same as range(0,5,1) ---> Coz Befault start_index is 0 and step_value  is +1, if user intenstionally doesnot change it.


# range() : The range() function returns the range object which we can see after converting it into list or tuple or set or Can d irectly use with for-loop.

x = range(0, 6)  # returns a range object sequence like from 0 to less than 6 and be seen by converting into any Sequence datatypes like list, tuple, set -

print(x)  # range(0, 6) we will get it as it is.
print("The Sequence Data is : ", list(x))  # [0,1,2,3,4,5]
print("The * unpack sequence range Data into Indivisual :", *x)
print("Indexing of", x[1])  # 1
print("length of Sequence :", len(x))  # 6
print("Membership Check :", 5 in x)  # True


# The range() function always generates/returns a sequence of numbers starting from given number and ends before given number with bydefault '1' stepping; starting from 0 Index (by default), and increments by 1 (by default), and ends before specified number i.e less than given number.

# Syntax : range(start_index(0 bydefault), stop(excluded_index), step(+1 increment bydefault ))

# range(5) ---> Generates Number starting from 0(befault) to before 5 i.e till 4.   (same as range(0,5,1) )

x = range(0, 4)
for num in x:
  print(num)

# same as range(0, 4, 1) as range() function takes starting index 0 bydefault and step by +1 by default.
x2 = range(4)
for num in x2:
  print(num)


# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(0, 4, 2), Here It is must to sepecify in same order of arguments passed.
x3 = range(0, 8, 2)


# We can use for-in loop to iterate over any range(), list, tuples or any sequence of elements.

# ii) for-in over string/looping through a string :

for item in "banana":
  print(item)  # b, a, n, a, n, a

for index, item in enumerate("banana", 1):
  print(index)  # 1   2   3   4   5   6
  print(item)  # b   a   n   a   n   a


# iii) for-in over list :
for num in range(10, 15, 1):
  print(num)  # 10 11 12 13 14

# Note*** : for-in-loop loops over items not over indexing, remember.

fruits = ["apple", "banana", "graves"]

# Iterate over List Items -
for item in fruits:
  print(item)

# To Iterate over items along with its indexing -

# using range(len(list))  -
for i in range(len(fruits)):
  print(i)  # For indexing
  print(fruits[i])  # Items accross Indexing

# OR, - using built-in enumerate() function -

for index, value in enumerate(fruits):
  print(index)  # 0       1      2
  print(value)  # apple banana  graves

for index, value in enumerate(fruits, 1):
  print(index)  # 1       2      3
  print(value)  # apple banana  graves


# NOte: enumurate(iterable_object, setting_start_index(default is 0))


# Decrement Iterating over items of List - we use reversed() function where we pass a <iterable_object> to iterate loop from backwards i.e from end -

alph = ["a", "b", "c", "d"]
for item in reversed(alph):
  print(item)

# We can also Do same using slice operator[::-1] with passing -1 step value - 
alph = ["a", "b", "c", "d"]
for item in alph[::-1]:
  print(item)



#   -------------------------------------------------

# Examples : Print "Hello World" 10 times -

for i in range(1, 11):
 print(f"{i}. Hello World")

 # Examples : Print "Hello World" with stepping +2  -
for i in range(1, 11, 2):
 print(f"{i}. Hello World")

 # Examples : Print "Hello World" 10 times with only provided ending point i.e same as range(11) as range(0,11,1)
for i in range(11):
 print(f"{i}. Hello World")

 # Examples : Print "Hello World" 10 times with not putting 'index' parameter in for loop instead just put underscore character(_) when we arenot intereted in printing looping index though we can still print with underscore i.e print(_) -
for _ in range(11):
 print(" Hello World")
#  print(_) #indexing


# break and continue keyword : - These keywords one and only used within loops( like for-loop, while-loop in python) for controlling the flow of any loops.

# These keywords not used directly inside if-else statement untill it is not within any loops means when there is any if-else statments present within loop then we can use it otherwise not.

# If break and continue keywords use outside of a loop, it will cause a compile-time error for the program.

# break : As soon as we face 'break' keyword inside any loop, then Exits the current loop immediately and move to the next line of code, regardless of loop condition getting True.
# NOte : If there is two loops or multiple nested loops then it exits only the current loop means innermost enclosing loop only.

# continue : Just like 'break' keyword we exit the current loop, similary in the continue keyword as soon as face, then "skips the current loop iteration execution and move to the next iteration within the same loop."
# NOte : If there is two loops or multiple nested loops then it skips only the current loop iteration and move to next iteration within the same loop.

# Hence, When loops are nested(a loop inside another loop), 'break' and 'continue' only affect the innermost loop not the outerloop.

# 'break' Statement in for-loop :- exits the current loop immediately and move to next line of code in program i.e outside of current loop -


# Task1 : As soon as "banana" encountered exist the loop immediatly and do not print other items -
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break  # As soon as break encountered exit the for-loop immediatly
  print(x)  # apple

# Task2 : As soon as "banana" encountered print it and and do not print rest items -
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)  # apple, banana
  if x == "banana":
    break  # As soon as break encountered exit the for-loop immediatly


# 'continue' Statement in for-loop : - with 'continue' statement we can stop the current iteration of the loop, and continue with the next iteration within same loop.

# Task : Do not print banana means skip the banana priting from the list and print rest items -
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# 'pass' keyword in for-loop : - for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error. Ex :

for x in [0, 1, 2]:
  pass
print("Normal Code")

# Nested for-loop : - A nested loop is a loop inside a loop. For nested loop, It Firstly complete entire execution of innerLoop for each iteration of outerloop value. Example :-

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
      print(x, y)  # red apple
                  #   red  banana
                  #   red  cherry

'''  The Output is : -
  red apple
  red banana
  red cherry

  big apple
  big banana
  big cherry

  tasty apple
  tasty banana
  tasty cherry
                '''


# ------------------------------------------------------

# while loop : The major difference between for-loop and while-loop is that In for-loop no of iteration we know beforehand but in while-loop we dont know excatly the no of iteration of the loop beforehand untill while(<condition>) doesnot get False. Thus, for-loop used for couting-loop but while-loop use for indefinite no of loops use case like user password entering means untill user doesnot enter the correct password the loop will remain ruuning and show to prompt to enter the password.

# For while, when no of iteration we dont know have idea. While loop runs till a condition is True.Thus before every iteration it checks if the condition is still True or False and if False then It ends while loop and move to next line of code.

# Initialization is done before the loop and update is handled inside the loop body.

''' Synatax :

    i= 0    --> Initialized the condition before.
    while i<10  ---> Provided the condition for initialization
        #code
        i += 1  ---> Updating the previous Initialization every time.

# i += 1 ---means i = i + 1 (previous value of i=0)

Note: remember to increment i, or else the loop will continue forever and terminal gets hanged.






#Q : Take password from user untill he/she can't enter the correct password, and show the prompt to enter password again and again untill he doesnot enter the right password.

initial_pw= ""
while(initial_pw != "rowdy"):
  initial_pw = input("Enter the password : ")

  
password = "" # Initial Password
while password != "Rowdy@123":
    print("Wrong Password Entered...")
    password = input("Enter the password : ")

print("Successfully Loggined!") 
    



# 'break' Statement in While loop : - exits the current loop immediately and move to next line of code in program i.e outside of current loop. Ex:

#Task : As we know we dont know priorer iteration in while loop, so task is Exit the loop when i is 3:

i = 1
while i < 6:
  print(i) # 1 2 3
  if i == 3:
    break
  i += 1


# 'continue' Statement in for-loop : - with 'continue' statement we can stop the current iteration of the loop, and continue with the next iteration within same loop. Ex : 

Task : Continue to the next iteration if i is 3 -
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) # 1 2 4 5 6

'''
# Q: Print even number from 1 to 100 using while loop -

even = 2  # smallest even number = 2
while even <= 100:
  print(even)
  even += 2  # even = even + 2  #updating i or intial or previous iteration.

# Q: Predict the output -
j = 0
while j <= 10:
  print(j)  # 0 1 2 3 4 5 6 7 8 9 10 (when j =11 then condition gets False and while loop ends)
  j = j + 1

# Q: Predict the output -

x = 1
while x == 1:
  x = x - 1
  # 0 and stops coz x = 0 became so conditon gets False after first iteration checking.
  print(x)


# Q: Predict the output -

i = 10
while i == 20:
  print("Computer Buff!")  # Will not print never as Condition get False

# Q : Predict the output -

x = 4
y = 0
while x >= 0:
  x -= 1
  y += 1
  if x == y:
    continue
  else:
    print(x, y)  # 3,1  2,2(skip)  1,3    0,4   -1, 5


# Q : Predict the output -
x = 4
y = 0
while x >= 0:
  if x == y:
    break
  else:
    print(x, y)  # 4,0   3,1

  x -= 1
  y += 1

# Note : As soon as we enclounter 'break' keyword loops end there immidiately.cc


# --------------------------------------------------------

# Pattern Printing Problems :

# Q1 : Print the given pattern -

# For n = 1
# *****  (5 starts)

# For n = 2
# *****
# *****

# For n = 3
# *****
# *****
# *****

#Concept : rows = 3, columns = 5(five no of stars) ; what to print = "*"

n = int(input("Enter number of row or Enter n : "))

for _ in range(0, n):
  print("*" * 5)
  #OR, print("*****"")

  
# Q2 : Print the given pattern
# For n = 4 (4 rows and 4 number in each row)
# 1234
# 1234
# 1234
# 1234

# for n=6
# 123456
# 123456
# 123456
# 123456
# 123456
# 123456


  
  