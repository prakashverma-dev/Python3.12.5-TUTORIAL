
# Types of Functions based on its Defining : - There are two types function in any programming lang based on its strucuture which are -

# a) Predifind or Built-in Functions : Python Provides many built-in fuctions to work with many repatitive tasks like print(""), sum(my_list), etc. These functions code built-in means written by python itself. 

# b) User Defined functions : A function where we define our own custom function with our required task to complete, these functions code written by user itself.

# Note : Any fuction can be identify with its opening and closing brackets beside function name like print() , where 'print' is a function.

# So we will focus on User defined function in this section and will learn about it why we need this, creation, etc.


# Why need function in programming : We need to implement function in programming to avoid repitation of same code again and again for different input or parameters on which our program problem depends. Ex: Print table of any number; Print Sum of positive integers till any number, that depends on user input variable -

# Ex: Print table of 2 -
#Concept : 2 *1, 2 *2, 2*3

for counting in range(1,11):
    print('Table of 2 is : ', 2 * counting)

# Ex: Print table of 3 -

for counting in range(1,11):
    print('Table of 3 is : ', 3 * counting)

#Ex: Print sum of first 10 natural number -

sum = 0
for count in range(1,11):
    sum += count    
print("Sum of first 10 natural number is :", sum)
    
#Ex: Print sum of first 20 natural number -   
# 
#  will repeat the same above code -  

# Thus, To Print sum of different user defined input or Print Table of any user defined number then either we need to take help of python inbuilt input() function or function. Here, By using function code of block will be in concise form and more programm Friendly. So lets Implement function in next section.



# Function : Functions are blocks of reusable code that perform a specific task.

# Input ------>[Fuctiion]---------> Ouput
#  n ------>[Fuctiion(find sum of all nos till n)]--------->  sum


# Creating a function or Defining a function : - we use 'def' keyword followed by function_name along with passed parameters(optional) and then function scope with indentation where either we return some value to function at the end of body or directly we print any value inside function.

# Syntax to Declare a Standard Function :-
'''
    def function_name (parameter1, parameter2, ...):
            #code --> body of function 

            return statement or print statement

Where, def ---> Keyword to define a function
       function_name --> discriptive function name with snake_case naming  
       parameters(optional)  --> Input to the function
       return/print statement ---> Give some output

'''


# Calling a function or Invoking a function : Whenever we create a function or define a function, that doesnot executes untill we dont call it, so we need to call it whereever we need to use that function functionality with passing arguments(optional) to it.

# Syntax : function_name(argument1, argument2, ....)

# Note : The difference between paramters and arguments in function is that parameter we pass while defining any function and arguments we pass while calling same function with no of paramtered declared = expects same no of argument while calling. 


# Example : Define a funcion to print sum of two number -

#Defining a funcion -
def sum_of_two_numbers(n1, n2):
    sum = n1 + n2
    return sum

x = 2
y = 3
#Calling the defined function here -
ans = sum_of_two_numbers(x,y)
print(ans)

# Example : Define a funcion to print sum from user input till 'n' -

def sumUptoN(n):
    sum=0
    for i in range(1, n+1):
        sum += i
    return sum    

# n = 5
n = int(input('Enter n : ')) # Taking n at run time.
output = sumUptoN(n)
print(f'The sum up {n} is', output )

# Suppose, we want to pass another input -
n1 = int(input('Enter n : '))
output2 = sumUptoN(n1)
print(f'The sum up {n1} is', output2 )


# Note : IN Python, we must define function attop an dthe we call it down side , if we try to call function top of function defining then we get error and function will not run.


# NOte : Whenver we dont return any value to function, then It returns the 'none' datatype value we if print it. and Other use case of 'return' keyword inside function is to terminate the function scope immediately as soon as we encountered 'return' keyword. It is some time use when we purposely want to terminate function further code execution.


# NOte : By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.



#Types of Arguments : - Arguments are those we pass to function call, whuch can be passed to a defined function with different ways. 

# Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python:

# a) Positional arguments
# b) Keyword arguments (named arguments)
# c) Default arguments
# d) Arbitrary arguments (variable-length arguments are *args --> arguments and **kwargs --> Keyworded arguments i.e key-value pairs arguments.)

# Lets Take a example - A function which takes 2 number as input and returns their sum -

def add(n1, n2):
    print("n1 :",n1)
    print("n2 :",n2)
    sum = n1 + n2
    return sum

# a) Positional Arguments : While passing arguments to the function when passed arguments, order of sequence is matter i.e position matter then we called it as positional argument. SO Be carefully pass the argumnts in same order as expecting by parameters in function else the value will be received to function wrongly that might throw an error in program.

print("The sum is", add(2,3)) # Here, n1 = 2 and n2 = 3 Passed
print("The sum is", add(3,2)) # Here, n1 = 3 and n2 = 2 Passed

# Thus, when order of sequence for passed argument is matter, then pass in same order as defined at paramters.

# b) Keyword Arguments(Named Arguments) : It is also known as named arguments coz while passing arguments we pass values corresponding to each parameter variables or names. So that user does not need to remember the order of parameters for passing arguments to it.

print("The sum is", add(n2 = 2, n1 = 3)) #In opposite order
print("The sum is", add(n1 = 2, n2 = 3))  # In same order

# Thus, when order of sequence for passed argument is doesnot matter, then we use Keyword argument type i.e pass in any order with specifing parameter names along with passed value.

# c) Default Arguments : - A default argument is the value we already assign to function parameters in case if user doesnot enter any value for passed arguments or missed any value from argument or even called the function without even passing single arguments. The in such case, Default argument values work like a fallback values to function call.

# As we know, we dont assign default arguments beforehand, if function expects 2 arguments, and if we provide even less no of arguments or more no of arguments i.e 1 or 3 arguments, you will get an error, To avoid handled such case beforehand with default arguments.  

def add(n1=0, n2=0):
    print("n1 :",n1)
    print("n2 :",n2)
    sum = n1 + n2
    return sum

print("The sum is", add())  # We skipped passing arguments
print("The sum is", add(2))  #Here, n1 = 2 and n2 = 0 (default value)
print("The sum is", add(2,3))  #Here, n1 = 2 and n2 = 3


# d) Arbitrary Arguments : In Python have two Arbitrary Arguments which are *args(arguments object), and **kwargs(keyworded arguments object) that allow us to pass 'variable length arguments' to function means we can pass any no of arguments at function call using these special objects or keywords -

# *args (Non-Keyword Arguments Object) : When we pass this parameter to function, that means we passed varibale length arguments and This always return a tuple inside the function to work with passed any no of arguments.

# Ex: Sum of user defined no of arguments we dont know how many arguments or inputs user will pass at run time -

# Sol : we use arbitrary length arguments i.e *args or *<any_variable_name> 

def addAnyNoOfArguments(*args):
    print(type(args)) # returns tuple datatype
    print(args) # returns (2,4,5,6)
    print(len(args) ) # length of tuple size
    # pass
  
    sum=0
    for value in args:
        sum += value

    return sum        

print(addAnyNoOfArguments(2,4))  
print(addAnyNoOfArguments(2,4,5,6))  
print(addAnyNoOfArguments(2,4,5,6,5))  


# **kwargs (Keyword Arguments Object ) : It is key-value pairs arguments where we always get the 'dictionary' datatype inside the function. We need **kwargs arguments whenever we need to work upton some key-value pair as input data from user like studentInfo(name = 'Prakash', age = 23, city = 'Delhi' ) and we can pass any no of key-value pair seprated by comma(,)

# Syntax : **<any_variable_name>  recomended to use **kwargs


# Print Student data Info -
def studentInfo(**kwargs):
    # print ( type(kwargs) )  # dict datatype
    # print ( kwargs ) # {'name': 'Prakash', 'age': 23, 'city': 'Delhi'}
 
    # TO Traverse a dictionary in for-in loop -
    for x,y in kwargs.items():
        print(x,'is',y) # HEre x is key and y is value we assumed as variable


studentInfo(name = 'Prakash')
studentInfo(name = 'Prakash', age = 23)
studentInfo(name = 'Prakash', age = 23, city = 'Delhi' )

# Note :  We can pass any no of arguments as key-value pair to keyworded arguments function defined. 



#Pass Keyword In Python : - IN python, We use 'pass' keyword with a) Conditional Statement, b) Loops c) Functions d) Class and whereever there needs an scope with indentation(:), there we can use 'pass' keyword which works as placeholder for that scope means that scope doesnot have any content as of now or doesnot implemented yet, but we want to implement it in the future. In such cases, we can use the 'pass' statement so that python complier doesnot throw any error.

# By passing 'pass' keyword doesnot throw error and in later we can use it to implement -Example:

n = 10
# if n > 10:
    # write code later

# print('Hello') # Here, we will get an error message: IndentationError: expected an indented block

# Pass keyword inside 'if statement'-
n = 10
if n > 10:
    pass # Doesnot Throw any error
print('Hello')


#Pass keyword in function : function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error, Example -

def myfunction():
  pass


#Pass keyword in Clas : We can do the same thing in an empty function or class as well -

def function(args):
    pass
class Example:
    pass


# --------------------------------------------------------------

#Anonymous Function / Lambda Function / Function Expression : In Python, an anonymous function means that a function is without a name. As we already know the def keyword is used to define the normal functions. Same as We use 'lambda' keyword to create a anonymous functions or Lamba Function or Function Express.


# Syntax: lambda arg1, arg2, arg3, ... : <return_expression_code>


#How We Define : While defining Lambda Function, It doesnot need any function name, neither parenthesis to hold arguments nor return keyword. We just use 'lambda' keyword to define followed by any no of arguments then with colon(:) on same line <logic code> which automcatically return resultant value to lambda function, as lamba function is a anonymous function so we need to hold the returning value to any holding variable to print it later. That why lambda or anonymous function also known as 'Function Expression' as well.

# Note : A lambda function can take any number of arguments and must have return expression in same line without return keyword which get returned to lamba function automatically.

# Example : -

# Normal Function - (To add two numbers)
def func(a,b): return a+b

print(func(2,6))

# Lambda Function or Anonymous Function or Function Expression (To add two numbers) -
holding = lambda a,b: a+b

print(holding(2,6))

# Example2 : To add three number using lambda function -
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


#Use-Case Of Lambda Function : The power of lambda is better shown when you use them as an anonymous function inside another function i.e whenever in a situation we need to pass a function inside another function, we use lambda Function.

# Lambda function mostly can be use with higher oder function in python like map(), filter(), sorted() function which all expect first arg as 'a function' and second arg as 'sequence_iteratable_object', Example -


# Multiply each item in list with 2 -

my_list = [3,5,6,7,2]

result = map(lambda item : item*2, my_list) #map() function executes a specified function for each item in an iterable.
print(list(result)) #convert the map into a list, for readability.


# Filter List Items based on a condition (like even no only, greter than 2 etc)

my_list2 = [3,5,6,7,2, -3, -10]
result2 = filter(lambda item : item % 2 == 0, my_list2) #Return only the Even Number
print (list(result2))

result3 = filter(lambda item : item >= 0, my_list2) #Return only positive nummbers.
print (list(result3))



# ---------------------------------------------------------------------

#Problems With Functions -

# 1. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

#Concept : factorial of n = n! = n * n-1 * n- 2 * .... *1 
# factorial of 5 = 5! = 5 * 4 * 3 * 2 * 1 

def factorial(n):
    product = 1
    for i in range(n, 0, -1):
        product *= i

    return product


print("Factorial of 0 is", factorial(0)) # 0! = 1
print("Factorial of 5 is", factorial(5)) # 5! = 120
print("Factorial of 10 is", factorial(10)) # 10! = 36228800

# 2. WAP to calculate Table of any number using function -

#Concept : Table of 2 : 2*1 , 2*2,  2 *3, 2*4, ...
#Concept : Table of 3 : 3*1 , 3*2,  3 *3, 3*4, ...

def tableof(num):
    print(f"The Table of {num} is : ")
    for i in range(1,11):
        print(num * i)

tableof(2)
tableof(3)


#3.  What will be the output of the following code snippet?

x = 50
def func(x):
    x = 2
func(x)
print ('x is now', x)


# x is now 50 (Correct**)
# x is now 2 
# x is now 100
# None

#4. What will be the output of the following code snippet?

def say(message, times = 1):
    print(message * times)

say ('Hello')
say('World', 5)

#a) Hello
# WorldWorldWorldWorldWorld  (Correct)

#b) Hello
# World 5

#c) Hello
# World,World,World,World,World

#d) Hello
# HelloHelloHelloHelloHello

