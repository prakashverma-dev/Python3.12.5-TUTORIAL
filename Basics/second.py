x=43
y=34
z=4

print(x,y,z); #Here, print() seperator works as printing multiple value at once in one line with space provided.

print(F"""{x} {y} {z}""")

#f-string :It is formatted string literal for "To use string along with variable in output".
# 
# How to use : To use formatted string literals, begin a string with f or F and then string double or thriple quotes now we can able to mix string with a variable or a pthon expression. TO do so, enclose any python express or variable inside the curly braces{} and normal string as it is.

x= 34
y=56
print("The value of x and y is :", x,y)
print("The value of x is ",x,"and the value of y is",y) #with string concatination

print(f"The value is {x} and y is {y}")

foo="prakash verma is good boy   "
print(foo.upper())

# Note : here upper() method returns a new string so that original string is not affected.
print(foo)

# OR, 

name_capital=foo.upper()
print(name_capital)


print(foo.lower())

#title() method : -
print(foo.title()) #capitalized each first char from the pragraph or string.


#strip() method : It is use to trim any white space from begginning and end of the string. It is mostly usefull when we receive input from user.so we want we get only string data no any extra spaces which might not run later code.
print(foo.strip()) #removes white spaces from beginning and end of the string.

#lstripp() - left strip(to remove white space from biginning of the string) and rstrip() - right strip(to remove white space from end of the string)

#find() : To get index start index of passed character or string of original string and if doesnot find returns -1.

# NOte: As we know python is case -sensitive langauge so if we pass character in capital letter which isnot present then we also get -1 as didnt find.

print(foo.find("verma")) # v char start index is 8
print(foo.find("Verma")) # -1 as this string doesnot found in original string.
print(foo.find("V")) # -1 as this string doesnot found in original string.

#replace("") : To replace all found character or sequence of character with a new character or sequence of characters and if doesnot found returns the orginal string.

oldString="Hey Prakash"
print(oldString.replace("a", "x")); #replace all found 'a' char with new 'x'
print(oldString.replace("A", "x")); # "Hey Prakash"
print(oldString.replace("ax", "x")); # "Hey Prakash"
print(oldString.replace("ak", "x")); # "Hey Prxash"

# in operator : to check a character or sequence of character exist in original string or not and return true or false boolean value, we use 'in' operator.

print("wow" in oldString) #False
print("He" in oldString) #True
print("HE" in oldString) #False
print("Hey" in oldString) #True

# Note : in operator and find() method differnce is that find() method returns the starting index of existing string and in opertor returns the true or false value of existance string or not.



#not in operator  : use to check a string or character doesnot exist in original string with returning true or false boolean value.

print("wow" not in oldString) #True
print("HEy" not in oldString) #True
print("Hey" not in oldString) #False

print(10 + 3) #Addition
print(10 - 3) #Substraction
print(10 * 3) #Multiplication
print(10 / 3) #Single Division (Can get floating point number)
print(10 // 3) #Double Division (for must get integer value, no floating value)
print(10 % 3) #Modulus (For getting Remainder of the Division)
print(10 ** 3) #Exponant i.e Left^Right(left to the power of right; here 10^3=1000)

#Special Operator : Augamanted Assignment Operator -

x = 10 #Want to increament x by 3
x = x + 3

# OR, USE Augmanted Assignment Operator -
x += 3 #(same as x=x+3)

# Note: we use addition as one example for augmentated assignment operator we can use other arthemetic operator for same cause.

#Numbers Methods : -

# i) round() : To round-up a number to integer value only; no deciman part.

print(round(2.234)) #2
print(round(2.5)) #2
print(round(2.6)) #3
print(round(2.9)) #3

# ii) abs() : absolute value of a number means if we pass negative value we get positive value that absolute |-2.8| = 2.8

print(abs(-2.8)) #2.8
print(abs(-2.9)) #2.9

# To work with complex math operation, we need to use math module of python, which need to be imported on the top of code - 
#module - a sperate file with some inbuilt python code, to make our work easy.

import math

# Here, math is an object so we use dot notation to access it methods nd properties.

print(math.ceil(2.2)) #To get ceiling value of the value i.e 3
print(math.floor(2.2)) #To get floor value of the value i.e 2
print(math.fabs(-2.2)) # absolute value = 2
print(math.fmod(10,3)) # remainder of x/y i.e 10/3 = 2
print(math.trunc(10.6)) # integer part of number = 10

print(math.isnan(3)) #False
print(math.exp2(3)) # 2 raised to the power number i.e 2^3 = 8
print(math.pow(2,3)) # x raised to the power y i.e 2^3 = 8
print(math.sqrt(2)) #Square root of number i.e suarerootOF(2) = 1.414

#Note: All trigometrical functions sin, cos, tan etc. befault takes radian as input angle not degree(30Deg). By default angles are in radians, not degrees(i.e right angle is pi/2). SO, To get sin(52.517Deg), you need to convert those degree to radian first i.e 1radian = pi/180.
#  
print(math.sin(math.radians(30))) #first we need to convert degrer angle into radian as all angles bydefault takes in radians.
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))

#math constant values i.e can be access as math object properties -

print(math.pi) # Value of π = 3.141592…
print(math.e)   # Value of e = 2.718281…
print(math.tau) # Value of τ = 2π = 6.283185…
print(math.inf) #Get value as positive infinity = inf
print(math.nan) #Get value as "Not a Number(NaN)" = nan

#Some Other Probability Math Operations  -

# comb(n, k) :  Number of ways to choose k items from n items without repetition and without order

# factorial(n) :  n factorial

# gcd(*integers)  :   Greatest common divisor of the integer arguments

# isqrt(n)  :   Integer square root of a nonnegative integer n

# lcm(*integers)  :   Least common multiple of the integer arguments

# perm(n, k)   :   Number of ways to choose k items from n items without repetition and with order

x= input("Enter a Value X : ") #input() return an string
# y=  1+x #HEre at runtime interpreter evalutes and throw run-time error in reading this line of code. As It -

# Will look like y= "1" + 1 (Here, Note: an object can be concatnated if the they were same type but here first is string and second is number so python will throw an error as "typeError".) So need to convert either in same type either entirely in string or number.

y= str(2)+ x 
print(y, type(y)) #23  <class 'str'>

y= 2+ int(x) 
print(y, type(y)) #5  <class 'int'>

# OR, 

print(f"x: {x}, y : {y}") #x: 3, y : 5