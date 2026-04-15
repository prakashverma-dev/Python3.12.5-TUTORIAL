'''

Note : In Python, objects are either mutable or immutable objects, depending on whether their content (state) can be changed at same stored location or assigned a new location to store.

Immutable Objects : The objects which can not be changed after they are created. Any operation that alters their value in mututabl object results/returns in a new object. Ex:

int
float
complex
string
tuple
bool
Unicode
etc..

Mutable Objects : At same address, if data get changed of object after its creation, those objects called as mutable objects.  

Mutable Objects can be modified after creation, without changing their identity.

List
Dictionary
Set
user-defined Classes(depending on defined attributes by user)
etc..



#Common immutable types:

int  e.g., a = 5
float - e.g., b = 3.14
complex - e.g., c = 1 + 2j
bool - e.g., flag = True
str - e.g., name = "Alice"
tuple - e.g., t = (1, 2, 3)
frozenset - e.g., fs = frozenset([1, 2, 3])
bytes - e.g., b = b"hello"





Common mutable types:

list - e.g., lst = [1, 2, 3]
dict - e.g., d = {"key": "value"}
set - e.g., s = {1, 2, 3}
bytearray - e.g., ba = bytearray(b"abc")
Most user-defined classes (unless made immutable by design).


'''






# 1. Integer Immutable Check : -

# Note : We use id(<variable>)  to know the address stored location in memory.
x = 5
print(id(x)) # address of stored above variable 'x' i.e a box container --> 140728556561656
x = 12
print(id(x)) # address of stored above variable 'x' i.e a box container --> 140728556561880


# Hence, Data stored at different location not get updated at same location or get changed.
x = 5 # now x started pointing previous stored dat location address rather creation a new location or conatiner.
print(id(x)) #  140728556561656 ---> same address location of x = 5

y = 5
print(id(x)) # 140728556561656 --> doesnot created a new location rather started pointing 'y' to previous conatiner to save memory space extra.

y = 7
print(id(y))# 140728556561720 --> now address got changed as new value assigned to y so 'y' started pointing to new address location.

# Hence, integer in Python is Immutable datatype or object. 

# 2. Float Immutable Check : -
weight = 50.33
print(id(weight)) # 2088458493008

weight = 52.33
print(id(weight)) #  2088458493008

# Thus, Different address get stored hence float is also imutable datatype.


# 3. Boolean Immutable check : -
a = True
print(id(a)) # 140728555653888
b = True
print(id(b)) # id of a and b will be same coz value is same.

a = False
print(id(a)) # 140728555653920

# Both addresses are not same --> Immutable Object.

# 4. String Immutable check : -

name = "Prakash"
print(name)
print(id(name)) # 1450390283600
name = "Rahul"
print(name)
print(id(name)) # 1450390284032
# Both addresses are not same --> Immutable Object.
# Also, we can not change after it creation -
print(name[0]) # R
# name[0] = "J" # address is fixed and we canot modify data at same address in immutable objects.
# print(name) # TypeError: 'str' object does not support item assignment



# Mutable Objects : List, Dictionary, Set


lst = [2,3,4,6]
print(lst) # [2, 3, 4, 6]
print(id(lst)) # 2507308971648

# Lets change at same address-
lst.append(12)
print(lst) # [2, 3, 4, 6, 12]
print(id(lst)) # 2507308971648

# Note : In list at same address data is get updated, means list is mutable object.
# Note : Diffrence between list and string is that string is immutable and list is mutable object.

# ----------------------------------------------------------------------

'''
# Pass by Reference and Pass by Value in Function : -

#1) Pass by Value : When a immutable object(int,str,float,tuple) passed to function, then a copy of object is created and assigned to local variable in function.

if any change is made to them inside function do not affect the original variable values outside function.


'''

# Example : Pass by value -
def addOne(x):

    print(id(x)) # 140728556561656
    x = x + 1

    print("Inside Function:",x)
    print(id(x)) # 140728556561688


x = 5
addOne(x)
print("Outside Function:",x)
print(id(x)) # 140728556561656


# Pass By Reference : Here we pass mutable objects(list, dict, set) to function.

# a reference to actual object is passed to function
# changes inside the function will affect the original object.
# Here doesnot create any copy, it affects in original object.


# Example : Pass by reference -
def modifylist(lst):

    newlst = lst
    newlst.append(7)
    print("Inside Function:", newlst)

    # lst.append(7)
    # print("Inside Function:", lst)

lst = [4,5,6]
modifylist(lst)
print("Outside Function:", lst) 