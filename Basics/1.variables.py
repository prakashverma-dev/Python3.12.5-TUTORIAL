

#Variables and their declarationns In Python : -

# Variables : In Programming, Variables are containers which are used to store some data to computer memory space randomly. Just Like In our kitchen we stores groceries in different conatainers.

# Each Containers or Variable Names have the memory locations allocated in our computer memory space which is randomly.


# Any variable value can be changed with time, that can be updated with time.

# Note : Python has no command for declaring a variable like other programming languages.

# Variables can hold different datatypes data in it like string, float, number etc.

# Variable Declaration Synatax :-
#   <variable_name> = <variable_value> 


# name = "Shradha"  --> variable = value
# age = 23
# age = 24
# # price = 23.599

# Here, a variable is a name given to a memory location in a program. 

'''
# Variables Memory Represenation : - Variables means memory locations given to our computer memory space randomly.

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


# Variable Type In Python : Python is 'Dynamically Typed' language means we do not need to tell explicitally to the variable while declaring that which datatype we are going to store, python compiler automaticaly/implicitally (due to Dynamically Typed ) get recognized that user which type of data want to store in variable either float, integeer, string etc.  

# Ex: In C-Progammig -

#int x = 5   ---> here In c, we need to tell variable which kinda datatype we are going to store


'''


#Multi-Variable Declartin Syntax In Python :-  Python allows us to Declare Many Values to Multiple Variables in one line:

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






# Identifier : - In Programming Languages, Identifers can be variable names, function names, class names, and other names which needed to use to assign some value to it in programming.

#Identifier Naming Rules : In every programming languages there are some common Naming rules for Indentifier(Variables etc.). In Python we have following Indefierfer Naming Rules  -- 


# NOte : Python is a case_sensitive language which means upper case and lower case characters are not same but different. THus, remeber to use variable name accordingly.

# i) An indentifier or variable name can only contain uppercase(A-Z), lowercase(a-z), digits(0-9) and an underscore(_) OR, It can be the combination of all these with exceptions. and Indetifiers can't be any special symbols like !,#,@,%,$ etc.  
# Ex : a-z, A-Z, 0 -9, _ But not % @ Not allowed. Examples :  myVariable, variable_1, variable_for_print 

# ii) An indentifer or variable name must start with either any letters or with underscore character, NOt start with any digit or number. Ex: name or _name, name1 valid But 1name, *name Not valid.


#iii) Variable names are case-sensitive (count, Count and COUNT are three different variables).


# iv). Dont use Python reserved keywords like break, if, class, def etc. as indetifiers or variable names.

# v) In Python, while naming any variable or indetifier we follow 'snake_case" naming convention, recommended by python, where all characters must be in lower case and words can be sperated with underscore. Ex: over_time = True unlike, in other languages mostly uses 'lower camel case Convention' where first word, first char letter is small and next word first char must start with capital letter. e.g: overTime = True

# vi) As per python peg8 documentation, while assigning value to variable names, user must keep one spaces between both sides i.e assigning value to variable for clean code. Ex: hey = 2 --< had one space before and after assignment operator.

# vii) Identifier can be of any length but it is recommended to use simple, short and meaningful name for better readibility and programming experience across developers. like course_name= "Python Prg"



# store data can be different types which knwon as datatypes in programming languages. (5 dataype)
x = 5 # Integer datatype
y = "JOHn" # string datatype
z = 5.2 #float dataype
b = False  #Boolean datatype
b = True  #Boolean datatype
c = None # Null Dataype

# We will see them later in datatype.

# Knowing Type of stored value i.e Datatpe using type() function -

name = "Shradha"
age =  -25
price = 25.99
print (type(name) )
print ( type( age) )
print (type (price))



#Keywords in Python : CHeck Videos of Table LIsts.(There area round 33 reserved keywords. )

# Examples : To check which one is valid or invalid varaibles names.

























