


"""



name = "Prakash" ; here, we defined a 'name' variable which stored string datatype. 
name = "Rahul" ; now name variable get changed from the python memory locatin.
age = 23
price = 25.99


students_count = 1000; here, python interpreter stored 1000 value to meomory location which referenced by students_count variable to access it. So it is just like a lebel for memorial allocation, which can be used to access the stored variable across that label.
print(students_count);

Now, what kind of data stord in python to varibles - Let's see -
#Built In Primitive Data In Python - strings, numbers, boolean

NOte : Python is a case_sensitive language which means upper case and lower case characters have different meanings not same.

is_published = True (TRUE or, true not accepted).
unit_price = 3
rating =4.99
space=3+4j
is_published= False
course_name = "Python Prograaming"

print(type(is_published))  #<class 'bool'>
print(type(unit_price))   #<class 'int'>
print(type(rating))   #<class 'float'>
print(type(space))   #<class 'complex'>
print(type(is_published))  # <class 'bool'>
print(type(course_name))  # <class 'str'>


#Variable Names Definining Rule : Best Praticases-

a) Variable name always use meanigfull for more reading adability like course_name= "Python Prg"

b) Write clean code of defining variable names like small letter all, have underscore for name seperation, have spaces between assigning value to variable that follows python peg8 documentation.

--------------------------------------------------------------------------

#Type Conversion In Python: In python we have built-in function for type comversion from one datatype to another datatype-

int()  ---> converting any convertable datatype into integer.
float()  ---> converting any datatype into float.
bool()  ---> converting any datatype into boolean.
str()  ---> converting any datatype into string.


#In Boolean Context : -
#Falsy Values in Python : There are only three("", 0, None) falsy values in python except this all values present are truthy values.

Falsy values : ""(empty string), 0, None (represt absence of a value)

Example : 

print(bool(0)) #False
print(bool("")) #False
print(bool(None)) #False
 
print(bool(1))  #True
print(bool(-1))  #True
print(bool(5))  #True
print(bool("False"))  #True

#Thus, Except Falsy values( 0, "" and None) all are truthy value.


#Another Builtin Function in python -


i) input() :  this function takes an string data and returns an string datatype output.


It is used to take input from user; as an argument takes a string which will be lebel that display on the terminal for taking input.

NOte: Dont run this code with code runner extension where as run manually in terminal with >python file.py file so that we can able to give input else code runner will run all code at once and that will be read only, not write.

x= input("Enter a Value X : ") #input() return a string
# y=  1+x #HEre at runtime interpreter evalutes and throw run-time error in reading this line of code. As It -

# Will look like y= "1" + 1 (Here, Note: an object can be concatnated if the they were same type but here first is string and second is number so python will throw an error as "typeError".) So need to convert either in same type either entirely in string or number.

y= str(2)+ x 
print(y, type(y)) #23  <class 'str'>

y= 2+ int(x) 
print(y, type(y)) #5  <class 'int'>

# OR, 

print(f"x: {x}, y : {y}") #x: 3, y : 5



ii) type() : a python builtin function where we pass an object as an argument and return its type that which datatype it is of class.

x= input("x: ")
print(type(x))

Ouput Will Look like this : -
x: 1
<class 'str'>


--------------------------------------------------------------------------

#Numbers : In python we have three types of numbers - Integers, Floats, Complex Number

a)  x= 1 #Integers
a)  x= 1.1 #Float
a)  x= 1+2j #Complex Number : a+bi(IN math, where i is imaginary number)

We use 'j' instead of 'i' to denotes imaginary number in python code writting.
Here, x is known as complex number having 1 real value and 2 is imaginalry value.

#For All Numbers Present In Python, we have following Standard Arthematic Opertion We have -

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

#Numbers Methods : - While working with any number datatypes like integer, floats, complex, we can use following methods for it - 

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


#Special Numbers in Python : 
Python has some special numeric values that you can encounter, especially when working with scientific computations or handling edge cases.

NaN (Not a Number): NaN stands for “Not a Number” and is used to represent undefined or unrepresentable values such as the result of dividing 0 by 0.

Infinity and -Infinity: Python also supports positive and negative infinity, represented by float('inf') and float('-inf'), respectively. These are useful in various situations, such as when setting bounds for algorithms or detecting overflow conditions.


# NaN Example
import math
n = math.nan
print(n)   # nan

# Infinity and -Infinity Example
x = float('inf') 
y = float('-inf') 
print(x)  # inf
print(y)  # - inf




-------------------------------------------------------------------------

#String : String in python is nothing but a set of characters used to define a string. It is define with double quotes(Ofen used), Or single quotes. Also can be used thriple quotes(single or double) 



#string Methods or Functions - To perform some operations over given string and get some usefull output-




i) len() function : To get the string length
o=len(course)
print(o); //

OR, print(len(course))

ii) To get a specific character from the string - use Square bracket[] with desire index no -

print(course[0]) ; //Zero index starts from first chat from beginning of string.
print(course[-1]) ; //Negative index starts from first char from end of string.
print(course[-2]) ; //Second character from the end of string.

Note : IN python or in any other progamming languages, string counting starts with zero index and goes upto length-1, Measn for length=4; last index=3.

iii) Slice out or Extract any no of char from string from any position -

syntax : text[start_index : end_index(Exclusive i.e not included)]

text[:end_index] ---> slice out from start index i.e 0 by default to till provided end_index(exclusive).
text[start_index:] ---> slice out till last index of the string from provided start_index.
text[:] --->If we skip with start nd end index, then it slice out complete string i.e we will get copy of original string.


print(course[0:3]); //Pyt ; here 3 indicates index=3 char will be not included.
print(course[0:]); //return same string as original with extraction
print(course[:3]); //Bydefault python put zero; so we get upto 2nd index string from zero index.

print(course[:]); //If we skip with start nd end, gets copy of original string.

Note: print(message[0:])  # upto last index value get.
print(message[:3])  # upto 2nd index value get.
print(message[:])  # copy of the original string.

iv) upper() method -

Methods or Functions, In OOPs, all functions are called as methods.

Note: In python everthings are objects that OOPs concept of visualizing everthing what we see around us. And Object can have properties and methods/i.e function can be accessed using dot notation.

foo="Prakash"
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
print(oldStrin 
g.replace("a", "x")); #replace all found 'a' char with new 'x'
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





------------------------------------------------



#Escape Sequence or Character(\) : Sometimes we need to use same character of set after using before like highlighting a text with double quotes as output from sring define with same doouble quotes -


text = "My name is "Prakash" Verma" // task to print on output, we use escape character to full-fill or use string defining alternatively.

text='My Name is "Prakash" Verma'

OR, 

text = "My name is \"Prakash\" Verma' //Note: whenever we use escape character(\) then just after character gets ignored by compiler/interpreter to  get error and treted as string part then.

Note : \(back slash) ---> escape character
      \"(back slash+any single character) ----> escape sequence

      Examples : -

print("My name is \"Prakash\" Verma")  #My name is "Prakash" Verma
print("Python \"Programming"); # Python "Progamming


#Some Other Escape Sequences in python -


# ----> Hash sign indicate a comment; to write some notes which is executed by python interpreter.

\" or \' ---> To add a single or double quote in output text string.

\\  ---> To include a back slash in output of the string.

\n ---> n for new line, to add a new line from text in output.


#Formatted String : 

first="Prakash"
last="Verma"
full=first+" "+last  #string formatted.
print(full)

#better way of string formatted - can use formate string(f or F formate string)

full=f"{first} {last} 2"
print(full)

# Note: In Format String, we can put any valid express inside curly braces to  get executed, could variable value or direct python express.

full=print(f"{len(first)} {last} 3")

full=print(f"{len(first)} {last} {4+5} 4")


------------------------------------------------




-----------------------------------------------------------------------

#Fundamentals of Programming : -






















"""
