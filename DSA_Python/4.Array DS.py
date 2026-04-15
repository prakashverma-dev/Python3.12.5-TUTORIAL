'''






'''
# importing array module as armd -
import array as armd
from array import array      # we can also directly import the array() function as well
# arr_int = array('i', [1, 2, 3, 4])


# creating an array with integer type
myarr = armd.array('i', [1,2,3])
print (myarr)
print (type(myarr))
print (myarr.typecode) # to know typecode of that array

# creating an array with float type
myarr2 = armd.array('f', [1.1, 2.2, 3.3])
print (type(myarr2), myarr2)
print (myarr2.typecode)


# Double (more precision float)
arr_double = array('d', [1.23, 4.56, 7.89])
print(arr_double)


# Character array
arr_char = array('w', 'hello')
print(arr_char)


# length of array : TO iterate over areay -
print(len(myarr))
print(len(myarr2))


# Note : There are TypeCodes avaialable for array module for various data types -
''''

'i' ---  integer type ---> 2 Byte
'f' ---  float type ---> 4 Byte
'd' ---  float double type ---> 8 Byte
'u' or 'w' ---  unicode character type ---> 2 Byte


'''

# Array Operations : -

#1) Accessing Array Element using Indexing -
from array import *  # means imort all function from array module to here.
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

#2) Iteration over array : To print all value or access it -

#Note : What is Indexing : It's very important that before iterating over any data structure, one should get the size of the DS, so Iteration will take place from 0 to n-1, where n is the size of that data structure.
# size = len(arr_int)


# Note : 'Step' in for-loop is python way to jump the iteration steps how fast using range() function like - 
# range(0,size, 1) ---> +1 step i.e default case.
# range(0, size, 2) ----> +2 step jump of iteration
# range(0, size, -1) ----> -1 step jump down of iteration i.e decreasing loop
# range(0, size, -2) ----> -2 step jump down of iteration i.e decreasing loop by step 2.

arr_int = array('i', [1, 2, 3, 4])

size = len(arr_int)
for i in range(0, size):
    print(i)
    print(arr_int[i])

#3)  Insertion of an Item In an Array : -
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60) # at index 1 added 60.
for items in array1:
  print(items) 

# we can add Item at the end of array using apend -
array1.append(70)
for items in array1:
  print(items)

#4) Updation of an array element -
from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80  # updating index 2 value with new value 80
for x in array1:
   print(x) 

# 5) Deletion Operation 
from array import *
array1 = array('i', [10,20,30,40,50])
array1.pop() # Removes the last index item
for x in array1:
   print(x)

array1.pop(1) # Removes any particular index item
for x in array1:
   print(x)

#we can use remove() method with specifying the array value to remove :- (when we want to remove with knowing the item value) -
array1.remove(30)
for x in array1:
   print(x) 


#6) Slicing Operation : Slicing in python is the part of indexing accessing but with a range. Slicing is the process of getting a sequence from the data structure which will have a starting index and an ending index. Since, python arrays provide indexing, slicing operations provide extensive usage of arrays.
from array import *
array2 = array('i', [10,20,30,40,50])
                    #  0, 1, 2, 3, 4   ---> +ve indexing
                    # -5 -4,-3,-2, -1 ---> -ve indexing
array3 = array2[1:3] # want to get sub-array from index2 to before index 3.
print(array3) # [20, 30]

# using negative indexing -
print(array2[1:-1]) # from index 1 to before -1 index(i.e last index ) # [20, 30, 40]

#Note :  Reversing the array elements using slicing -
print(array2[::-1])


#6) Search Operation : You can perform a search operation on an array to find at which index a target element exist in the array or not, We can search an element in array with following ways : -

# a) using python built-in index() function ---> O(n) Time Complexity.
# b) using Linear Search Algorithm ---> O(n)
# c) using Binary Search Algorithm  ----> O(logn)

# a) using python in-built index() method : - index() provide the target element to be find from the array.

from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40)) # '3' gives index of found element from array.



# 7) Sort Operation : Sorting of an array elements can achieve it with one of the following approaches −

#a) Using a sorting algorithm -
      # Bubble Sort, Selection Sort, Insertion Sort ---> O(n^2)
      # Quick Sort ---> O(n^2) for worst case, O(n logn) for average case
      # Merge Sort ---> O(n logn) for both worst and average cases.

#b) Using the sort() method of List DS ---> O(n logn) 
#c) Using the built-in sorted() function ---> O (n logn)


# a) Using a sorting algorithm : using bubble sort - #  We implement the classical bubble sort algorithm to obtain the sorted array. To do it, we use two nested loops and swap the elements for rearranging in sorted order.
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a) # array('i', [4, 5, 6, 9, 10, 15, 20])



# b) Using the sort() method of List DS : - In python array module doenot have inbuilt sort() method like python list DS, so we convert the array into list using .tolist() method then we can use sort() method, it change the orignal array -

orgnlArray = arr.array('i', [10,5,15,4,6,20,9])

orgnlArray_list = orgnlArray.tolist() # converting array into list to perform sort method.
print("Original Array :", orgnlArray_list)

#ascending order
orgnlArray_list.sort()
print("Array after sorting:", orgnlArray_list)

#descending order
orgnlArray_list.sort(reverse=True)
print(orgnlArray_list)

# c) sorted() method :  sorted() function returns a new list containing all items from the iterable in ascending order. Set reverse parameter to True to get a descending order of items.
import array as arr
orgnArr = arr.array('i', [20, 2, 12, 4, 0, 6, 18,])
sorted_Arr = sorted(orgnArr) 

print("Sorted Array :", sorted_Arr )
print("Original Array ",orgnArr)



# 8) Reverse Operation : Reversing an array is the operation of rearranging the array elements in the opposite order. There are various methods and approaches to reverse an array in Python including reverse() and reversed() methods -
# using reverse() method of list : Since Array module doesnot have reverse() method, we can convert array into list using tolist() and then use list reverse() method -
numericArray = arr.array('i', [10,5,15,4,6,20,9])
numericArray_list = numericArray.tolist()

# reversing
numericArray_list.reverse()
print("Reversed Array : ", numericArray_list) 

# using slicing operation -
numericArray = arr.array('i', [88, 99, 77, 55, 66])
print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)



# 9) Join Operation :   The process of joining two arrays is termed as Merging or concatenating. Python provides multiple ways to merge two arrays such as append() and extend() methods.




# --------------------------------------------------------------------------------------------

# Excercise : -
# Example 1
# Python program to find the largest number in an array − 

# Example 2
# Python program to store all even numbers from an array in another array −

# Example 3
# Python program to find the average of all numbers in a Python array −

# Exercise Programs
# Python program find difference between each number in the array and the average of all numbers

# Python program to convert a string in an array

# Python program to split an array in two and store even numbers in one array and odd numbers in the other.

# Python program to perform insertion sort on an array.

# Python program to store the Unicode value of each character in the given array.



# -------------------------------------------------------------------------------------

## Array Implemenation using numpy External libray : -

# NumPy stands for 'Numerical Python' powerful Python library that is widely used for scientific computing, data analysis, and numerical computing tasks.

# Install numpy external libray : > pip install numpy

import numpy as np

# Creating array with integer type -
myArr5 = np.array([4,5,6,7])
print(myArr5)

# Note : For defining any array here using numpy module, we dont have to give Typecode, numpy module auto defined it for corresponding data types.

# Creating array with integer type -
myArr5 = np.array([4,5,6,7])
print(myArr5)

# Creating array with float type -
myArr5 = np.array([4.4, 5.2,6,7])
print(myArr5)

# Creating array with char type -
myArr5 = np.array(["ram", "shyam", "sita"])
print(myArr5) 

