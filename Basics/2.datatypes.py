'''
#Python Datatypes : -

                Python DataTypes
                        |
Numeric      Mapping     Set     SequenceType   Boolean  None                   
               |
      Dictionaries                     |
                                    a)Strings
                                    b)List 
                                    c) Tuple
|a)Integer
b) Float
c) Complex


Overall, There are 10 Datatypes and more...



#Numeric Datatype : a) Int --> 100, -5, 256 (all are whole number) 
# b) Float : decimal numbers - 2.5, -1.8
# c) Complex Number : 1+2j, 60+250j


#Text Datatype : string ---> represented by single(' ') or double quotes(" ")(prefered for string defining)

Boolean Datatype : contains boolean values i.e either True and False (Here, must T or F must be in capital character) 

#Sequence Datatype : whenever we want to store  sequence of data or collection of data we use Sequence Datatypes like List or Tuple -

    a) List : It is define by square bracket[] and data stored in list are mutable i,e changable at run time means original data store in list can be changed later. We can store sequence of data or collection of any datatypes.

sequence of integers -- [1,2,3,4]  --->   can be change later.
sequence of strings --> ["lis", "pia", "dia"]  ---> can be change later.


    b) Tuple :  It is also collection of items ie any datatypes. Here, We use curly bracket() to define a Tuple which is not mutuable data i.e immutable means data can not be modify later on or at run time in any stages remember.

    Example : (2,1,3,3,2) ("wow", "hey", "good")   ---> can't be change later.


#Set datatype : It is un-ordereded collection of unique items, define using curly braces {}

fruits = {"apple", "banana", "cherry}


#Mapping Datatype : It has dictionary datatype where we store key-value pairs. It is define using curly braces{} with assignment operator to define a dictionary corresponding to the variable or indentifier.

Ex: storing a student data as key-value pair -

 student1 = {            
"name" : "Rahul"
"rollno" : 123
}

 student1 = {
"name" : "Kavya"
"rollno" :345
}

Here, student1 and student2 are dictionary datatypes.



#None Datatype : It is special datatype where we store no value in variable i.e nothing then we use it. MOst use-case whenever we want to nullify any store data, we updata that variable with none datatype. It is represnt null value.




-----------------------------------------------
#type() function : It is python inbuilt function to know the datatype of any passed data. It accepts a Required one argument as passed dataype value or stored varible to know which datatype it is. Also this type() function accepts two optional argument related to base class and namespace for base class.


'''

print(type(-23))  # <class 'int'>
print(type(-23.2))  # <class 'int'>
print(type("HEy")) #  <class 'str'>
print(type(True))  #  <class 'bool'>
print(type(False)) 
print(type(2+3j)) # <class 'complex'>
print(type(None)) # <class 'NoneType'>
print(type(["wow", 2])) # <class 'list'>  list same as Array
print(type(("wow", 2))) # <class 'tuple'>  tuple 
print(type({"wow", 2})) # <class 'set'>  --> set(unordred)

print(type({"name" : "hey", "rollno" : 23}))  #  <class 'dict'>  --> dict same as object 


#Hence, there are around 10 standard inbuilt python datatypes and more datatypes are range(comes under sequence datatype), frozenset(comes under set datatype) and Binary DataTypes(bytes, bytearray, memoryview)

# ---------------------------------------------------------------------------

#Type Casting : It is a process of converting one datatype to another, if it is convertable otherwise throw an error as TypeError.

# int("123" )  --> 123
# float("123") --> 123.0
# str(123) --> "123"str
# int(3.14) ---> 3 (float to int)



# Example : 
# int() --> Convert any convrtable datatype into integer datatype
# float() --> Convert any convrtable datatype into float datatype
# complex() --> Convert any convertable datatype into complex datatype
# str() --> Convert any convrtable datatype into string datatype
# boo() --> Convert any convrtable datatype into boolean datatype

# list()  -- > convert any iterable data/object into list.(Note: In python everthing is an object)
# tuple() --- > convert any iterable data/object into tuple
# set() ---> convert any iterable data/object into set.

# dict() -->  only convertable a list,tuple, set to a dictionary if it contains elements that are key-value pairs (usually as 2-element tuples or lists.


# Note : You cannot convert any complex data into another datatype but you can convert any other datatype into complex number/datatype.
# x= int(3+2j); #passed argument must be except complex number. Can't converated

print("We learning type casting ")

text= "hey prakash"
text2= "345"
# print(type(int(text))) #Canot converated as it is not convertable
print(type(int(text2))) # converated as it is convertable


num=1
str1 = str(num)
print(type(str1))

#Converting into Integer or Integer Datatype :

x = int(1)   # x will be 1
y = int(2.8) # y will be 2 (converted into only integer value not float as output)
z = int("3") # z will be 3

#Converting into Float : -

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


#Converting into String : -

x = str("s1")   # x will be 's1'
y = str(2)      # y will be '2'
z = str(3.0)    # z will be '3.0'


#Converting into Complex : - If convertable -

x = complex(2) #convert from int to complex:
print(x, type(x))  # 2+0j 

#Converting into Boolean : - If convertable -

# Note : In context with boolean, There are around seven Falsy values i.e( ""(empty string), 0, None (represt absence of a value), [], (), {}, False (False Boolean Value itself) )  and except these seven falsy values all values present are truthy values.

# Example : 

print(bool(0)) #False
print(bool("")) #False
print(bool(None)) #False
print(bool(  [] )) #False
print(bool( ()  )) #False
print(bool(  {} )) #False
print(bool(  False )) #False
 
print(bool(1))  #True
print(bool(-1))  #True
print(bool(5))  #True
print(bool("False"))  #True
print(bool("Hello"))
print(bool(15))
bool(["apple", "cherry", "banana"])

# Note : Almost any value is evaluated to True if it has some sort of content.
# Note : Empty list, tuple, set, and dictionary retuns False, if doesnot have single content e.g [], (), {}  returns False.

# Note : Some Values are False - In fact, there are not many Falsy values that evaluate to False, except empty values - such as  (), [], {}, "",  0, None. And of course the value False evaluates to False.

# Example
# The following will return False:

print( bool(False) )
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})




#Converting tuple datatype into list -
my_tuple= (1,2,3,4) #tuple datatype
my_list = list(my_tuple)
print(my_list, type(my_list)) # Output: [1, 2, 3, 4]

# print(list(2)) #canot converted

#Converting list datatype into tuple -
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (1, 2, 3, 4)

# Note : Only Iterable data can be converted either into list, tuple, set.
# print(set(2))

# List to Set:
my_list = [1, 2, 2, 3, 4]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4}


#Tuple to Set:

my_tuple = (1, 2, 2, 3, 4)
my_set = set(my_tuple)
print(my_set)  # Output: {1, 2, 3, 4}

# Note : In case of converted into set, It automatically remove duplicate values and are unordered.




# ---------------------------------------------------------

                                                
#Standard 'Input' In Python : - Python ibuilt function input() used to take user input from user at run-time in terminal or CLI.

# Synatax : input(Arg); 

# Where, Arg : Takes only 1 Argument that is string datatype only which is a prompt message to user to provide a value.

# Example : 

# x = input('Enter your name:')
# print('Hello, ' + x)



#Taking Input In Python : input() function - It accepts only one argument as string and return a string. It runs in CLI window in run-time of program.

name = input("Enter Your Name : ") #Return always string value.
print(type(name))  #String
print(name)

#Suppose, We want student roll to be enter as Integer value, so take help of type casting to convert string data into integer data -

roll_no = int(input("Enter your roll : ")) #now integer will be stored
print(type(roll_no)) #integer


#PROGRAM1 : Sum of 2 given number with taking user inputs and print the sum.

num1 = int(input("Enter First Number : ")) #We type casted to store num as integer datatype.
num2 = int(input("Enter Second Number : "))
sum = num1 + num2 
print("The Sum of these two number is",sum)


#PROGRAM2 : #Task to make following individual digit of number as '235' as Integer itself In output -

a, b, c = 2, 3,5

sum = str(a) + str(b) + str(c)
integer_sum = int(sum)
print("Result is : ", type(integer_sum), integer_sum) # <class 'int'>   235 


#PROGRAM3 : WAP to convert temperature from celsius to Fahrenheit -

# Formula :  C = (F - 32) * 5/9    OR, (9*C) / 5  = F - 32

#taking input as celsius from user -
celsius = float(input("Enter Temperature(In celsius) : "))

#Converting cel to fahren -

fah_temp =    (9 * celsius) / 5 + 32
print("Temperture in Fahrenheit :", fah_temp)

