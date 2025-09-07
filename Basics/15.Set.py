'''

#Sets : - It is also a container for storing multiple values in a variable. It is define using curly bracket i.e {} . Set Items are -

a) Unordered : Set Items, sequence of item is not fixed it can change.

b) Unindexed : Since, Set items are unordered, so Sets doesnot have indexing.

c) Unchangable/mmutable : Once a set is created, you cannot modify its existing items, but you can add new items to existing items or can remove existing items.

d) Duplicates Not Allowed : Whenever we define any duplicate values set ignores it. i.e Every Elemeent must be unique in set, it canot be duplicates.

e) Any Datatpe and Mix of Different Datattpes : We can define any type of datatypes to a set.




'''
#1. Creating a Set : Sets are written with curly brackets.


#a) using adding items to set -
myset= {'Doe', 'John', 'May'}
print(myset) # {'John', 'Doe', 'May'}  -- ORder didnot maintain
print(type(myset)) # <class 'set'>

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
#Note: Also, Once a set is created, you cannot change its items, but you can remove items and add new items.

#b) using set() construtor - to convert any iterable object into set -

thisset = set(("apple", "banana", "cherry")) 
print(thisset) # {'cherry', 'apple', 'banana'}

# OR, 
thisset = set(["apple", "banana", "cherry"]) 
print(thisset) # {'cherry', 'apple', 'banana'}



# Duplicate not allowed -
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # {'cherry', 'apple', 'banana'} duplicated ignored by sets.

# Set length -
print(len(thisset))

# DataType of set -
print(type(thisset))

# Checking if an item exists in a set -
if "cherry" in thisset:
  print("Yes It is Present")


# 2. Accessing Set Items : - Though Indexing is not allowd in sets. The other way is using for-in loop to access each items of set -

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) # Printing order of set items varies.


#3. Add an Item to existing set - using add() function -

# Though we know, Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset) # {'apple', 'banana', 'cherry', 'orange'} 

thisset.add("orange") #If we try to add same element in set, Will not add as sets doesnot allow duplicate values.
print(thisset)


# 4. Add a Iterable object(like set, tuple, list) to the set : -- using update(<iterable_object>) method -

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)


# Adding list items to the set -
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)


# 5. Remove an element from set :-  To remove an item in a set, use the remove(), or the discard() method; both works same but using dicard() method if the value which we want to remove doesnot found in set, then it doesnot throw an error.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset) # {'apple', 'cherry'}


# discard() method : - If the 'value' want to remove that doesnot not present in the set then remove() method throw an error, where as if we use discard() method which doesnot throw any error and fullfill the same purpose -

thisset.discard("banana")
print(thisset)


# pop() method :- You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() # Remove a random item by using the pop() method.
print(x) # bananna or any other item got removed

print(thisset)
 

#  clear() method : - It is uses to empty all the items from the set and make it empty set like {}.

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


# del keyword : To delete the set complety from the code with declartion -

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # NameError: name 'thisset' is not defined


#6. To copy a set - use copy() to get a copt set -
thisset = {"apple", "banana", "cherry"}
newset = thisset.copy()
print(newset)  # {'cherry', 'banana', 'apple'}


# 7. Join Sets :- There are several ways to join two or more sets in Python with different purposes -

# a) using union(set2, set3, set4,...) method : - joins the other set with returning a new set.

set1 = {"a", "b", "c"}
set2 = {"d", "e", "a"}

set3 = set1.union(set2) #Though set doesnot allow duplicates so while join duplicates items got discarded.
print(set3)


# b) using update() function : It update the original set with adding another iterable object to exiting set -

set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.

# c) While joining Keep only the duplicates items among the set : - use intersection() for returing common elements in new set. or intersection_update() method  for modifying the original set with common elements in it -

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = {"check", "wow", "apple"}


new_Set = set1.intersection(set2, set3)
print(new_Set) # {'apple'}

print(set1) # Original Set there.


# using intersection_update()  - It will also keep ONLY the duplicates, but will change the original set instead of returning a new set -

set1.intersection_update(set2, set3)
print(set1) # {'apple'}


# d) While Joining discarded the duplicates from the sets : -  use symmetric_difference() for returning a new set or symmetric_difference_update() for modifying the original set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

common_removed = set1.symmetric_difference(set2)
print(common_removed) # {'microsoft', 'google', 'banana', 'cherry'}

print(set1) # didnot modified.

# OR, To modifying the original set - 
set1.symmetric_difference_update(set2)
print(set1) # {'cherry', 'microsoft', 'google', 'banana'}



# -------------------------------------------------------

'''
Example : -

Given three arrays, we have to find common elements in three
sorted lists using sets.

Input : 
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output : [80, 20]

Input : 
ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
Output : [5]

'''

def common_elements(arr1, arr2, arr3):

      set1 = set(arr1)
      set2 = set(arr2)
      set3 = set(arr3)

      common_values = set1.intersection(set2, set3)

      return list(common_values)

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(common_elements(ar1, ar2, ar3)) # [80, 20]


ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]

print(common_elements(ar1, ar2, ar3)) # [5]




