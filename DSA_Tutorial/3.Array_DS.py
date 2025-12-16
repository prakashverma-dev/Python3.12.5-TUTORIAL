'''

# What is Array/Static Array In Programming Language : -

Array/Static Array : An Array can be defined as a storage or container or similar kind of data/items placed in the contiguous memory locations.

Array/Static array stores only Hemogenous Elements in it.

Note : Langaugages like C,C++,Java,C# etc. comes with Classic Fixed Sized Array i.e Static Array and We defined the above defination of Classic Array i.e Static Array. 

# An Array Can be of Two Type : -
a) Static Array : It the array where size of array is fixed and depends upon user defined size of array. e.g: C,C++,Java,C# Provides Static Array.

b) Dynamic Array : It is the array where size of array is not fixed, it expands or shrinks as per user size. Thus, User doesnot have to define any size of array here. e.g: Python, Javascrpt Provides inbuilt Dynamic Array.


# HomoGeneous and Heterogenous Arrays : -
a) HomoGeneous Array : It contains the elements of same datatype.
b) Heterogeneous Array : It can contain the elements of mixed datatypes.

#Properties of Array : -

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








'''