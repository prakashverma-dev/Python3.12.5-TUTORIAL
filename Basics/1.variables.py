"""


#Variables In Python : It is use to store data into computer memory.

Synatax : <variable_name> = <variable_value> 

Python has no command for declaring a variable like other programming languages.

a variable value can be changed with time,that can be updated later on.

name = "Shradha"  -- variable = value
age = 23
age = 24
price = 23.599

Here, a variable is a name given to a memory location in a program. 

MEMORY : [] []  [] [] []
         age       name

Here, once we assign a varible value to a variable, then python assign its value to a random memory space in computer with variale name get stored/saved. Now, Untill we dont change that the value accross that variable name, every time we get the same value from saved memory in computer, whenver we call with same variable names. 

# Changig value to memory location -
name = "Shravya" ---> now at same memory location/variable name different value get saved.
age = 23

# Assigning Value to a variable/Assignment Rule or Operator : -

# a = b 

# In math, a = b shows both values are equal but in porgamming langage it indicates we assigning righ-hand-side value into left-hand-side. thus, RHS value get stored/saved into LHS variable. 

# Ex: age2 = age (the same age value used to store in age2)
print(age2) # 23
print(age) # 23 #orinal value remain same.



# Knowing Type of stored value i.e Datatpe using type() function -

name = "Shradha"
age =  -25
price = 25.99
print (type(name) )
print ( type( age) )
print (type (price))


"""



#Variables and their declarationns In Python : -

# Variables : In Programming, Variables are containers which are used to store some data to computer memory space randomly.

# Declaration Synatax :  <variable_name> = <variable_value> 

# OR, Python allows us to Declare Many Values to Multiple Variables in one line:

# <var_name1> , <var_name2>, <var_name3>, so on. = <value1>, <value1>, <value1>, so on.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# NOte : Make sure the number of variables matches the number of values, or else you will get an error.'

# Also, We can assign single same Value to Multiple Variables in one line -
x = y = z = "Orange" # all variables will hold the same value.
print(x)
print(y)
print(z)

# Have You noticed, In Python, there is no keyword to declare a variable type, like other programming languages.

# Ex: In C-Progammig -

#int x = 5   ---> here In c, we need to tell variable which kinda datatype we are going to store

# Note : Python is 'Dynamically Typed' language means we do not need to tell explicitally to the variable while declaring that which datatype we are going to store, python compiler automaticaly/implicitally (due to Dynamically Typed ) get recognized that user which type of data want to store in variable either float, integeer, string etc.  Ex:

#Memory Represenation of variables : -

# In Progamming, container means some memory space in the computer, where data get allocated randomly in any vacant space. [] [] []

# Thus, Variables Points to some computer memory space or address of memory space.

x = 5 #Here, python automatilly determines which datatype get stored in variale i.e integer, we didnot explicitally need not to specify like other some programming lang.



x = 10 # this 'x' value get stored into memory space randomly in computer. which can be indentified with 'x' variable. or address of 10 value in memory space.

# what if update the avlue -
x = 10 # Now, 'x' location/address value in memory space get updated with new value.

#  Note : In Porgaming, once we assign any value to a variable, then that variable allocates some random memory space in computer to store that value, untill user doesnot change or update.

# store data can be different types which knwon as datatypes in programming languages.
x = 5 # Integer datatypes
y = "JOHn" # string
z = 5.2 #float
b = False #Boolean



#Naming Rules For Identifier : - In Programming Languages, Identifers can be variable names, function names, class names, and other names which needed to use to assign something in python program.


# Some Common Rules for Naming These Indentifier/Variables in Python are -

# NOte : Python is a case_sensitive language which means upper case and lower case characters are not same but different. THus, remeber to use variable name accordingly.

# i) An indentifier or variable name can only contain uppercase(A-Z), lowercase(a-z), digits(0-9) and an underscore(_) OR, It can be the combination of all these with exceptions. and Indetifiers can't be any special symbols like !,#,@,%,$ etc.  
# Ex : a-z, A-Z, 0 -9, _ But not % @ Not allowed. Examples :  myVariable, variable_1, variable_for_print 

# ii) An indentifer or variable name must start with either any letters or with underscore character, NOt start with any digit or number. Ex: name or _name, name1 valid But 1name, *name Not valid.


#iii) Variable names are case-sensitive (count, Count and COUNT are three different variables).


# iv). Dont use Python reserved keywords like break, if, class, def etc. as indetifiers or variable names.

# v) In Python, while naming any variable or indetifier we follow 'snake_case" naming convention, recommended by python, where all characters must be in lower case and words can be sperated with underscore. Ex: over_time = True unlike, in other languages mostly uses 'lower camel case Convention' where first word, first char letter is small and next word first char must start with capital letter. e.g: overTime = True

# vi) As per python peg8 documentation, while assigning value to variable names, user must keep one spaces between both sides i.e assigning value to variable for clean code. Ex: hey = 2 --< had one space before and after assignment operator.

# vii) Identifier can be of any length but it is recommended to use simple, short and meaningful name for better readibility and programming experience across developers. like course_name= "Python Prg"




#Keywords in Python : CHeck Videos of Table LIsts.(There area round 33 reserved keywords. )

# Examples : To check which one is valid or invalid varaibles names.


# Examples : Let' store some values in variables -


name = "Isha" #string datatype
roll_number = 17 #integer datatype
percentage = 95.8 #float datatype
is_student = True #Boolean datatype
age = 23























