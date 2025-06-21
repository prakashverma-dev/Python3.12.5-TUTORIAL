

# Numeric Methods : - While working with any number datatypes like integer, floats, complex, we can use following methods for it -

# i) round() : To round-up a number to upto desire decimal place. Bydefault roundup decimal value is zero means round() with no second argument pass return to nearest integer with no deciman part.

# Syntax:  round(number, digits) # Default digit arg is round-off to zero decimal place.


import math
print(round(5.76543, 2))  # 5.77 --> round off to two decimal place
print(round(5.76543))  # 6  --> round off to zero decimal place.
print(round(2.234))  # 2
print(round(2.6))  # 3
print(round(2.9))  # 3
print(round(2.5))  # 2

# ii) abs() : abs() function returns the absolute value of the specified number.means if we pass a negative value we get absolute i.e positive value i.e |-2.8| = 2.8


print(abs(-7.25))  # 7.25
print(abs(-2.81))  # 2.81
print(abs(-29))  # 29

# For Complex No -
print(abs(3+5j))  # 5.830951894845301


# pow() : The pow() function returns the value of x to the power of y i.e x^y same as Arthematic Operator ** i.e x**y means x ^y

# pow(n1, n2) ---> Equivalent to n1 ** n2

# If a third parameter(optional) is present, it returns x to the power of y, modulus of z.

# Syntax : pow(x, y, z)  --->  same as (x^y % 5)

print(pow(2, 3))  # 2^3 = 8  --> same as 2 * 2 * 2

# 4^3 = 64 % 5 = 4 same as (4 * 4 * 4) % 5) = 4
print("power is : ", pow(4, 3, 5))



# sum() : The sum() function takes an iterable object like list, tuple, set. TO add sum of all items and returns a number.

# Syntax:  sum(iterable_object, initial_sum_value) ; bydefault initial_sum_value=0

data = [2, 4, 5, 0, -1]
print(sum(data))  # 10

my_tuple = (1, 2, 3, 4, 5)
print(sum(my_tuple))  # 15

my_tuple = (1, 2, 3, 4, 5)
print(sum(my_tuple, 1))  # 16


# max() and min() :  The max() and min() function returns maximum and minimum number or string from a iterable object or directly values passed as argument. It returns highest or lowest no by comparing with other numbers or strings.
#  If the values are strings, an alphabetically comparison is done.

# max() and min() function either take iterable object or direct values passed as argument.

# Syntax :  max(n1, n2, n3, ...)    OR,     max(iterable)

my_tuple = (1, 2, 3, 4, 5)
print(max(my_tuple))  # 5

# OR,

print(max(4, 3, -2, 4, 10, 0, -1))  # 10
print(min(4, 3, -2, 4, 10, 0, -1))  # -2


# Python math Module : -  To work with mathematical tools we use math module to generate math specific constant values as well as we can perform mathematical basic operation using it.

# To work with mathematical operation, we need to use math module of python, which need to be imported on the top of code -
# module - a sperate file with some inbuilt python code, to make our work easy.


# Here, math is an object so we use dot notation to access it methods nd properties -

print(math.ceil(2.2))  # To get ceiling value of the value i.e 3
print(math.floor(2.2))  # To get floor value of the value i.e 2
print(math.fabs(-2.2))  # absolute value = 2
print(math.fmod(10, 3))  # remainder of x/y i.e 10/3 = 2
print(math.trunc(10.6))  # integer part of number = 10

print(math.isnan(3))  # False
print(math.exp2(3))  # 2 raised to the power number i.e 2^3 = 8
print(math.pow(2, 3))  # x raised to the power y i.e 2^3 = 8
print(math.sqrt(2))  # Square root of number i.e suarerootOF(2) = 1.414

# Note: All trigometrical functions sin, cos, tan etc. befault takes radian as input angle not degree(30Deg). By default angles are in radians, not degrees(i.e right angle is pi/2). SO, To get sin(52.517Deg), you need to convert those degree to radian first i.e 1radian = pi/180.
#
# first we need to convert degrer angle into radian as all angles bydefault takes in radians.
print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))

# math constant values i.e can be access as math object properties -

print(math.pi)  # Value of π = 3.141592…
print(math.e)   # Value of e = 2.718281…
print(math.tau)  # Value of τ = 2π = 6.283185…
print(math.inf)  # Get value as positive infinity = inf
print(math.nan)  # Get value as "Not a Number(NaN)" = nan

# Some Other Probability Math Operations  -

# comb(n, k) :  Number of ways to choose k items from n items without repetition and without order

# factorial(n) :  n factorial

# gcd(*integers)  :   Greatest common divisor of the integer arguments

# isqrt(n)  :   Integer square root of a nonnegative integer n

# lcm(*integers)  :   Least common multiple of the integer arguments

# perm(n, k)   :   Number of ways to choose k items from n items without repetition and with order


# Special Numbers in Python :
# Python has some special numeric values that you can encounter, especially when working with scientific computations or handling edge cases.

# NaN (Not a Number): NaN stands for “Not a Number” and is used to represent undefined or unrepresentable values such as the result of dividing 0 by 0.

# Infinity and -Infinity: Python also supports positive and negative infinity, represented by float('inf') and float('-inf'), respectively. These are useful in various situations, such as when setting bounds for algorithms or detecting overflow conditions.


# NaN Example
n = math.nan
print(n)   # nan

# Infinity and -Infinity Example
x = float('inf')
y = float('-inf')

print(x)  # inf
print(y)  # - inf



#PROGRAM4 Wap To Calculate volume of a sphere -

# Formula : volume =  4/3 * pi * r^3 
import math


radius = float(input("Enter radius of the sphere : "))

# volume = 4/3 * math.pi * (radius ** 3) #OR, 
volume = 4/3 * math.pi * pow(radius, 3)

# Note : n2 ** n1 same as pow(n2, n1) means n2 ^ n1 .
# round(fraction, digit) --> means round off fraction number to given digit place.

print("The Volume of the sphere is :", round(volume,3))



# --------------------------------------------------------

#MCQ1 : What will be the output -
x = 10
y = 5
print( x >y and x < 15)  # T and T --> True (Output)


#MCQ2 : What will be the output -
x = 5
y = "2"
print(x+y)  # --> TypeError (Output) #As we concatinate integer and string OR, x + int(y) = Output as integer    OR,         str(x)  + y = Output as string


#MCQ3 : What will be the output -
x = 8 //3 + 4%2   #8 /3 = 2.666 and 4 % 2 = 0
print(x)  # 2 + 0 = 2 (Followed L TO R coz of same precedence level)


#MCQ4 : What will be the output -

# d = 2 / 7  -->  0.2857