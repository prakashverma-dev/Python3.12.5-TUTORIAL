''''
# Tuple : It is also used to store multiple items in a single variable. We use round brackets i.e () to create a tuple. Tuple items are -

a) Indexed : Indexing start from 0,1,..so on of Items; also negative indexing -1,-2,...so on.
b) Ordered : It will remain in same order after creation or adding up
c) Unchangeable/Immutable : Very Important, The Items inside tuple we can not change at run time i.e we can update or change.

d) Duplicates Allowed : Tuple can hold duplicates values
e) Any Datatype Or Mix of different Datatypes : (1, 2, 4) ; (False,True);  (1, True, 3)

NOte : In List and Tuple all things are same apart from one major property of tuple i.e Tuple items are Unchangable and Rest All Properties between List and Tuple are same like Supports Indexing, Ordering, Allowing Duplicates Items. 

# NOte : 'tuple' object does not support item assignment whereas 'list' item support item assignment.


'''

# 1. Creating a tuple : - Tuples are written with round brackets. It can be created using two ways only -


#a) Defining with assigning Tuple items -
colours = ("red", "apple", "green")
print(colours)
print(type(colours))

# NOte : Once a tuple is defined or created we can not change its data even we can modifying or add new data to existing tuple. SO be caution while creation with right data.

#b) Defining with tuple() constructor - To convert any iterable object into tuple -
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

# OR, 
thistuple = tuple(["apple", "banana", "cherry"])
print(thistuple)



# When Creating Tuple With One Item : You must have to add a comma after the first item, otherwise Python will not recognize it as a tuple, and recognize it as string.

color = ("red")
print(color)
print(type(color)) # gives string

color = ("red",)
print(color, type(color)) # now tuple <class 'tuple'>


# To check Tuple Length - len() function
print(len(color))

# To check Tuple Type - type() function
print(type(color))

# To check if an item exists in a tuple or not using 'in' operator -
thistuple = ("apple", "banana", "cherry")
if "banana" in thistuple:
    print("Yes, 'banana' is in the fruits tuple")



#2. Accessing Tuple Items In tuple : - You can access tuple items by referring to the zero based indexing number like list, using square brackets:

thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

# Accessing With negative indexing -
print(thistuple[-1]) # cherry
print(thistuple[-2]) # banana

# Range Accessing with range indexing - It always return a tuple.
print(thistuple[1:3]) # ('banana', 'cherry') 
print(thistuple[-2 :]) # ('banana', 'cherry')


#3. Update Tuple Items :- Once a tuple is created, Tuples Items are unchangeable or immutable, meaning that you cannot change, add, or remove items once the tuple is created, So that assigning new value is also not allowd once tuple created -

myTuple = ("Ram")

# myTuple[0] = "Dev" # Item Assignement not allowd as Tuple is Immutable.
# myTuple[2] = "Sita"  # Not Updatable or Changable.

print(myTuple[0]) # Accessing Item Allowed with indexing

# Note : 'tuple' object does not support item assignment.

# Note : To work with changing tuple data, then You can convert the tuple into a list and apply list methods and then convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Note:  Once we converted tuple into list, we can aplly append(), extend(), remove(), del operator etc. 



#4. Looping/Traversing Through Tuple Items - Follow same as List -

my_tuple = ("apple", "banana", "cherry")

#i) using for-in loop -

for i in my_tuple:
    print(i) # here, i represents each items of the tuple.
    

#ii) using for-in with accessing index ( via range() function) -

for i in range(len(my_tuple)):
    print(i)  #Here, i represent the indexing of tuple items.
    print(my_tuple[i]) # Here, we accessing item corresponding to its index.



#iii) using for-in with accessing indexing (with help of enumerate() function) -
for index, item in enumerate(my_tuple):
    print(index) # index represent the indexing of items.
    print(item) # accessing items directly from string.


#iv) Using a while loop : Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes. Remember to increase the index by 1 after each iteration.

i = 0 #indexing of list items
while i < len(my_tuple):
    print(i) # Will get indexing frm list items
    print(my_tuple[i]) # Will get the item corresponding to indexing
    i += 1 #Updating the indexing


#v) using list comprehension :List Comprehension offers the shortest syntax for looping through tuple or Making some operations over each items of tuple returning a list remeber.

thislist = ("apple", "banana", "cherry")

# To get each item from tuple -
[print(x) for x in thislist]


# TO get tuple items as List items using list-comprehension -
new_list = [item for item in thislist]
print(new_list)  # We get the tuple items as list items.




#5. Unpacking A Tuple : Unpacking a tuple is a way to unpack each items of a tuple into different variable at the same time. like object/array destrution in Javascript.

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple: 
fruits = ("apple", "banana", "cherry")

# TO unpack fruits tuple into three different variables -
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3) # apple banana cherry

# OR, 
(fruit1, fruit2, fruit3) = fruits
print(fruit1, fruit2, fruit3) # apple banana cherry

# Note : Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.


# Using Asterisk i.e * while unpacking Tuple Items : If the number of variables is less than the number of values, you can add an * to the variable name and the remaining values will be assigned to the variable as a 'list' -

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
  
print(green)  # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry


#6.Concatenates/Joins Two Tuples : - using '+' Operator -
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) #  ('a', 'b', 'c', 1, 2, 3)



'''
Tuple vs Lists Difference : -

i) Iterating through a 'tuple' is faster than in a 'list'.
ii) Lists' are mutable whereas 'tuples' are immutable.
iii) Tuples that contain immutable elements can be used
as a key for a dictionary.


'''


# Example : -

'''
Reverse a tuple -

Input : tuples = ('z', 'a', 'd', 'f', 'e', 'k')
output : ('k', 'e', 'f, 'd', 'a', 'z')

Input : tuples = (10, 11, 12, 13, 14, 15)
Output : (15, 14, 13, 12, 11, 10)

'''

def reverse_tuple(myTuple):

    return myTuple[::-1]


input = ('z', 'a', 'd', 'f', 'e', 'k')
input2 = ( 10, 11, 12, 13, 14, 15)
print(reverse_tuple(input))  

# Generalized Way of Doing -

def reverse_tuple2( myTuple):

    my_list = []
    my_index = []
    # for item in reversed(myTuple):  #using reversed() method for decrement looping over any iterable object.
    for item in myTuple[::-1]:
        my_list.append(item)


    print(my_list)    
 

reverse_tuple2(input)        
reverse_tuple2(input2)    







