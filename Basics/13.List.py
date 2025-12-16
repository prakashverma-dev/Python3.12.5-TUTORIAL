

'''
#Python Collections(Arrays) : There are four collection data types in the Python programming language:

1. List : It is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple : It is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set : Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary : Dictionary is a collection which is ordered** and changeable. No duplicate members.


Note : When choosing a collection type, it is useful to understand the properties i.e purpose of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security. 


-------------------------------------------------------------------




#List :  It allow us to store multiple type of datatyes together in a single variable. We can store all types of items (including another list) in a list.  We use square bracket i.e [] to create a list. Here, Stored data in list are called as 'List Items' which are -

a) Indexed : Indexing start from 0,1,..so on of Items; also negative indexing -1,-2,...so on.
b) Ordered : After inserting items or updating, it will remain in same order.
c) Changeable(mutable) : Original Data of list can be changed at run-time.Hence, we can modify, replace or delete the items.
d) Duplicates Allowed : Items can be duplicates in list
e) Any Datatype & Mix of different datatype : Can hold any other datatpes like [1.2, True, "Ram", [2,4,6]]



Note: Python does not have built-in Array datatype, Instead 'Python Lists' can be used. Lists are similar to arrays (dynamic arrays that allow us to store items of different data types and automatically grows and shrinks).


To work with excalty array datatype you will have to import a library, like the NumPy library via >pip install numpy .

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

 

'''



#1. Creating a list in Python :  we use sequare [] to create a list where items seperated with commas. A Python list can be created/define with three ways -

#a) with directly items added -
fruits = ["apples", "banana", 2, 3.4, True]
print(fruits)
print(type(fruits))
print(len(fruits)) 

#b) with empty list - Then later add the items using assignment operartor or list method.
wow = [] 
wow.append("w") # Wow[0] = "w"
print(wow)

# NOte : 'list' object supports item assignment coz of 'mutuable' items(changable items) whereas 'tuple' object doesnot support item assignment coz tuple items is immutable i.e unchangable.

#c) with list() constructor to convert any iterable object into list -
wow2 = list((3,4,5))
print(wow2)  


#Checking List Length i.e Length Size : - use the len() function
print(len(fruits)) #  5


#Checking type of List -
print(type(fruits))  # <class 'list'>


# Checking if an item is present in the list -
if "banana" in fruits:
    print("Inside The List")

# Checking if an item is not present in the list -
if "kiwi" not in fruits:
    print("kiwi is not part of list") 



#2. Indexing In List : - Elements in a list can be accessed using indexing. Python indexes start at 0, so a[0] will access the first element, while negative indexing allows us to access elements from the end of the list. Like index -1 represents the last elements of list.

#To access an item in list, we use square barackte with list indexing number-     
fruits[0]
fruits[1]

# Accessing items using negative indexing(-1 --> lastitem, -2 --> before one, so one)

fruits[-1]
fruits[-2]
fruits[-3]


# To access a range items i.e sub-list from main list : -  
# my_list[start_index : end_index(Exlusive)]   Here, We can also access sub-list using negative indexing.

print(fruits[1:3])  # ['banana', 2]
print(fruits[-3:-1]) #using negative indexing # [2, 3.4]



#3. Changing/Updating Items In a list  : - 
# a) At an Index:   list = [10,20,30] -->  list[1] = 40 --> [10, 40, 30]
# b) In a range :  list = [10,20,30] --> list[1:3(Exlusive)] = [40, 50]

 
my_list = [10,20,30]
my_list[1] = 40
print(my_list) # [10, 40, 30]

my_list2 = [10,20,30]
my_list2[1: 3] = [40, 50]
print(my_list2) # [10, 40, 50]

my_list3 = [10,20,30]
my_list3[1:3] = "Rahul" #Must Be a List or Iterable object, here string each character treated as Item for list.
print(my_list3)

#4. Adding Elements to a list : - We can add elements to a list using the following methods: -

# append(<single_value>) --> It is list method only and It use to add only one specified item to the end of list. i.e this method takes only one argument could be any datatype(string, number, object etc.)
# insert(<at_index>, <item>) --> To insert one or more items at/from the particular index in the main list by keeping old items with indexing get changed.
# extend(<iterable_object>) -->To merge another list or iterable object (list, set, tuple, etc.) to the end of the main list, we use extend() method.

# Example : -

IPL = ["CSK", "MI", "RCB"]

# Adding an element to the end of the list -
IPL.append("PUNJAB")
print(IPL)  # ["CSK", "MI", "RCB", "PUNJAB"]

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a) # ['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]

#Adding an element to '2' Index using insert -
IPL.insert(2,"Dev")
print(IPL) # ['CSK', 'MI', 'Dev', 'RCB', 'PUNJAB']

# TO add or merge another any list or iterable object into the main list at the end, use extend() method -
more_teams = ["Delhi", "Rajstan Royals"]
IPL.extend(more_teams)
print(IPL) # ['CSK', 'MI', 'Dev', 'RCB', 'PUNJAB', 'Delhi', 'Rajstan Royals']


#5. Removing Elements from Array : - 

# remove(<item_tobe_removed>)  ---> It removes specified one item from existing list item from any position. It removes the first occurrence of the element with the specified value.

# pop(<index>)  ---> It removes an item with provided index and if we ommit the argument takes -1 as index value bydefault i.e removes the last item.

# clear() ---> The clear() method empties the list. The list still remains, but it has no content. It doesnot need any argument to pass.

#using 'del' keyword ---> The del keyword also removes the item from the specified index. The del keyword can also delete the list with creation.

a = ['apple', 'banana', 'cherry']

a.remove("apple")
print(a) # ['banana', 'cherry']

# a.pop(1) # removes item from index '1'
# print(a) #  ['banana']

a.pop()   # removes last item
print(a) #  ['banana']


#Clearing all items from the list -
thislist = ["apple", "banana", "cherry"]

thislist.clear()
print(thislist) # []


# using 'del' to remove any item from the list -
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # ['banana', 'cherry']

# using del to delete the list completly i.e its creation as well -


thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) # Runtime Error as There is no 'thislist' is not defined.


#6. Iterating or Looping over a list : -
my_list = ["apple", "banana", "cherry"]

#i) using for-in loop -

for i in my_list:
    print(i) # here, i represents each items of the list.
    

#ii) using for-in with accessing index ( via range() function) -

for i in range(len(my_list)):
    print(i)  #Here, i represent the indexing of list items.
    print(my_list[i]) # Here, we accessing item corresponding to its index.



#iii) using for-in with accessing indexing (with help of enumerate() function) -
for index, item in enumerate(my_list):
    print(index) # index represent the indexing of items.
    print(item) # accessing items directly from string.


#iv) Using a while loop : Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes. Remember to increase the index by 1 after each iteration.

i = 0 #indexing of list items
while i < len(my_list):
    print(i) # Will get indexing frm list items
    print(my_list[i]) # Will get the item corresponding to indexing
    i += 1 #Updating the indexing


#v) using list comprehension :List Comprehension offers the shortest syntax for looping through lists or Making some operations over each items returning a new list.


thislist = ["apple", "banana", "cherry"]
new_list = [x for x in thislist]
print(new_list)  # We get a copy of main list as we do not applied any operation to each item.

# To get each item from list -
[print(x) for x in thislist]





#7. List Comprehension In Python : - It is usefull when applying some sort of operation over each item and to get a new sub-list from it. We use List Comprehension, When we want to make a new list from items of an existing list.

# Syntax : 
#   new_list = [<returning_variable i.e item > for <item> in <old_list> if <condition== True> ]

# This return value is a new list, leaving the old list unchanged.

# Example : [23, 10, 5, 20]  ---> get LIst whose items are greater than 20.
# Example2 :  Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

'''

#Way1 : General Way -

newlist = []
for item in list:
    if item>25
        newlist.append(item)

#Way2 : Simple Way or Shorter way of achieving Same -        

newlist = [item for i in list if item>20]


'''
# Ex1: Filter out list whose value greater than 20 - 
sample_list = [23, 10, 5, 20]
newlist = [ item for item in sample_list if item>20 ]
print(newlist) # [23]

# Ex2: Filter out list that contains only letter 'a' - 

fruit = ['banana','apple', 'cherry']
newfruit =  [ item for item in fruit if 'a' in fruit]
print(newfruit) 

# Normal Way -
newlist = []

for x in fruit:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Ex3 : Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
cap_fruits = [item.upper() for item in fruits]
print(cap_fruits)


# Ex4: Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# Note : IF we do not apply any operation condition to the each item in the list, we get a copy of main list -

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newfruit) # Same List we get.


#Note : We can use 'List Comprehension' To Iterate Over Range with or without conditin in return list -

newlist = [x for x in range(10)]
print(newlist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Accept only numbers lower than 5 from range 0 to 10 -
newlist = [x for x in range(10) if x < 5]
print(newlist)




#8. Sorting A List : - It uses to sort the list alphabetically or numberically in ascending order(by default) and descending order(with passing reverse=True) using sort() method.

# a) Ascending Order(By default) : -

fruit = ['banana','apple', 'cherry']
fruit.sort() # It will short in ascending order by default
print(fruit) # ['apple', 'banana', 'cherry']

# Sorting a number in ascending order -
num = [5, -1, 0, 24, 45, 2, 1]
num.sort()
print(num) #[-1, 0, 1, 2, 5, 24, 45]

# b) Descending Order : -

fruit.sort(reverse= True)
print(fruit) # ['cherry', 'banana', 'apple']

num.sort(reverse= True) # For Sorting in reverse order i.e descending order
print(num) # [45, 24, 5, 2, 1, 0, -1]


#9. Reversing A List Items : - using reverse() method to reverse the order of  any list, either string list or number list -

num = [5, -1, 0, 24, 45, 2, 1]
num.reverse()
print(num) # [1, 2, 45, 24, 0, -1, 5]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # ['cherry', 'Kiwi', 'Orange', 'banana']


# 10. Copy a list : - You can use the built-in List method copy() to copy a list.

fruit = ["apple", "banana", "cherry"]
newfruitnew = fruit.copy()
print(newfruitnew) #Get copied

# using list() method or constructort to copy -
mylist = list(fruit)
print(mylist)

# using List Comprehension to copy -
mylist2 = [item for item in fruit]
print(mylist2)


# using : (slice) operator to copy
mylist = fruit[:]
print(mylist)



# 11. Concatinate/Join Lists : There are several ways to join, or concatenate, two or more lists in Python -

# using '+' operator -
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# using extend() method to concatinate -
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


#12. Nested List In List : - Whebever we define a list inside another list called as nested List. A nested list is a list within another list, which is useful for representing matrices or tables. We can access nested elements by chaining indexes. -

listt = [10, 20, [30 , 40], 50]
print(listt[2]) # [30, 40]

#Getting an item from sublist inside main list -
print(listt[2][0]) # 30 


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2])

# Example : 

myfruit = ['banana','apple', 'cherry']
myfruit.insert(2, ["kiwi", "papaya"])
print(myfruit)   #   ['banana', 'apple', ['kiwi', 'papaya'], 'cherry']

# Want to access 'kiwi' item -
print(myfruit[2][0])  # kiwi



# --------------------------------------------
'''
Q1. Given a list in Python and provided the index of the elements,
write a program to swap the two elements in the list.
Examples:
Input : List = [23, 65, 19, 90]  ; idx1 = 0 , idx2 = 2
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5] ;  idxl = 1, idx2 = 4 
Output : [l, 5, 3, 4, 2]

# Concept : First assign replacing item into a temp variable before swaping -
temp = List[1]
List[1] = List[4]  #Index '1' got value of index '4' and we lost the orginal index 1 value.
List[4] = temp


'''

def swapItems(mylist, index1, index2):

        temp = mylist[index1]
        mylist[index1] = mylist[index2]
        mylist[index2] = temp
        return mylist


Input1 = [23, 65, 19, 90]
idx1, idx2 = 0 , 2 

Input2 = [1, 2, 3, 4, 5]
idx1, idx2 = 1  , 4

# print(swapItems(Input1, idx1, idx2))  # [19, 65, 23, 90]
print(swapItems(Input2, idx1, idx2))  # [1, 5, 3, 4, 2]