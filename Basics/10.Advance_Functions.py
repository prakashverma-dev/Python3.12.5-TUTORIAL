
                             #Topic - 1


# Nested Function : When we define one function inside another function that function defining kwown as nested Function.

# A function that is defined inside another function is known as the inner function or nested function. Nested functions can access variables of the enclosing scope. Inner functions are used so that they can be protected from everything happening outside the function.

def outer_function():
    x = 1 # variables in the outer function

    def inner_function():
        y = 2 # variables in the inner function
        result = x + y
        return result #Returing value to Inner function

    return inner_function() #Returing value (i.e Inner function returned result) to Outer function    
  

# Now Outer Fuction Call -
output = outer_function() 
print(output) 

# Steps of Nested Function Flow : call Outer Function() ---> Execute Outer function all and at  the end gets Rturn value as 'Inner Function Call' ---> then Inner function execution starts working ----> which will further return some value to inner function that will get value Inner Function holds as result.



                            #Topic - 2 

#Python Scope and Local & Global Variables In Python : -

#Scope : When A variable is created in the specific region either inside function or outside region, called scope.


#Global Scope or Global Variable : When variables are created outside of a function or main body of the Python code, that belongs to the global scope and those varaibles known as global variables.


#Note: Global variables are variables which are accessible from within any scope like inside local scope as well as global scope i.e accesible inside of functions and outside of functions. Examaples : 

# Ex1: 
x = "awesome"

def myfunc():
  print("Python is " + x) # Accessible Inside Function

myfunc()
print(x) # Accessible Ouside Function

# Ex2: 

x = "awesome"

def myfunc():
  x = "fantastic" # here, Local Variable get Updated as x can access oustide function scope.
  print("Python is " + x) # Python is fantastic # local variable(by updated) used.

myfunc()

print("Python is " + x) # Python is awesome # glocal Variable used.

# 'Global' Keyword : - Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function. To make that variable global variable, Firstly declare the variable with 'global' keyword, which makes variable global, like global x and then assign the value to the variable. Ex:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Now Local Variable accesible coz of 'global' keyword.

# Ex2: 

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x) # 200 as local variable x = 200, converted to global variable and value of x get updated.



#Local Scope or Local Variable : A variable created inside a function belongs to the local scope and that variable known as local variable to the function, and that local variable or function variable only accesible within the function. Remembver, it can't accessible outside of function i.e out side of local scope. Ex1: 

def myfunc():
  x = 300
  print(x)

myfunc()
# print(x) # get an error as : NameError: name 'x' is not defined

# Ex2: For Function Inside Function -
def myfunc():
  x = 300  # local variable of function1
  def myinnerfunc():
    y = 200
    print(x) # Accessible Inside Function2
  myinnerfunc()
# print(y) # Can't accessible coz this is outside of Function2 and inside function1.

myfunc()
# print(x) # But Can't accessible outside of function scope or local scope.

# 'Nonlocal' Keyword : The nonlocal keyword is used to work with variables inside nested functions. The nonlocal keyword makes the variable belong to the outer function.

# using nonlocal keyword to make any variable accessible outside of nested function to outer function easily. i.e Upward direct flow of accessing of varaible get easy using 'nonlocal' keyword before varaible. Ex: 

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello" 
  myfunc2()
  return x # by using 'nonlocal' keyword, Inner Function Variable now accessible to outer function but not accsssible to global scope.

print(myfunc1())
# print(x) # Not accessible to here. 


# Ex2: 
def myfunc():
  x = 300  # local variable outer function
  def myinnerfunc():
     
    nonlocal x
    x = 200
    print(x) # Accessible Inside inner function
    # nonlocal x
    
  myinnerfunc()
  print(x) # Ealier, It was not accessible, but using 'nonlocal' keyword inside innner function, now it is accessible in outer function only. Not in global scope.

myfunc()
# print(x) # But Can't accessible.




                            #Topic - 3

#BeforeHand Need Concept of Mutuable Objects and Immutable Objects In Python-
'''

In Python, objects are either mutable or immutable, depending on whether their content (state) can be changed after creation.

Immutable Objects
These objects cannot be changed after they are created. Any operation that alters their value results in a new object.

Common immutable types:

int – e.g., a = 5

float – e.g., b = 3.14

complex – e.g., c = 1 + 2j

bool – e.g., flag = True

str – e.g., name = "Alice"

tuple – e.g., t = (1, 2, 3)

frozenset – e.g., fs = frozenset([1, 2, 3])

bytes – e.g., b = b"hello"

Mutable Objects
These objects can be modified after creation, without changing their identity.

Common mutable types:

list – e.g., lst = [1, 2, 3]

dict – e.g., d = {"key": "value"}

set – e.g., s = {1, 2, 3}

bytearray – e.g., ba = bytearray(b"abc")

Most user-defined classes (unless made immutable by design).

'''                            

# 'Pass by Reference and Pass by Value' Into Function Argument : -   







                            #Topic - 4                          


'''

# Recursion Function : -  " When a function calls itself repeatedly", to solve bigger problem by breaking into subproblems known as recursive function.


Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

synatax : Def recurse() :
              -----
              recurse()   ---> calling own function itself/ "Recursive Call" known as.

              -----
          recurse()    


Factorial of n : -

n! = n *  [ (n-1) * (n-2) * (n-3) * ...... * 1 ]
(n-1)! =  (n-1) *  [ (n-2) * (n-3) * ...... * 1 ]
(n-2)! = (n-2) * [ (n-3) * ...... * 1 ]

Thus, We can also write -
n! = n * (n-1)!    ---> i.e in terms of n again.

5! = 5 * 4! (if we know 4! value)

Thus, here, we divided big problem into subproblem.
n!   ----> Problem
(n-1)!   ----> SubProblem

Hence, Recursion do the same, In Recursion same fuction get called inside to repeat the function untill a stopping point and solves the main problem in breaking into sub problems.


# Recursive function must have two parts "Base Case" and "Recursive Case" : -

Base Case : Stopping COnditon of Recrusive Function.
Recursive Case : The logic where function calling itself to solve the problme in subproblem or in reapeated times untill base case doesnot stop it.

'''
# Ex :Factorial of a 'n' -
# using for-loop -
def factorial(n):

  fac= 1
  for i in range(n, 0, -1):
    # print(i)
    fac *= i

  return fac  


print(factorial(5))

# using Recursive function -
def factorialRecursive(n):

    # Base case -
    if n == 0:
      return 1
    
    # Recursive case -
    result = n * factorialRecursive(n-1)

    return result # Each time at Inner function call it returns the current value to preceeding call stack function.

# n = int(input("Enter nth value for factorial : "))
print(factorialRecursive(3))

# Q1: WA Recursive Programm to print number from n to 1.
# Logic : n --> (n-1) ---> (n-2) ---> .....  ---> 1

def showNumber(n):

    # Base Case
    if n == 0:
      return

    # Recursive Case
    print(n)
    showNumber(n-1)  

showNumber(10)



# Q2: WA Recursive Programm to print number from n to 1 In Reverse Order like Print 1, 2,3.
# Logic : n --> (n-1) ---> (n-2) ---> .....  ---> 1

# Note : We implement the logic same as Higher to lower but We keep the printing part after the Recusive Case Function coz It will execute after the call stack will start empty.

def showNumberDecending(n):

    # Base Case
    if n == 0:
      return

    # Recursive Case
    showNumberDecending(n-1)  

    print(n) # It will Execute once the Recursive function call will ends.

showNumberDecending(10)


# Q3: WA Recursive Programm to print Sum from 1 to n. 
# Input : n = 5
# Output : sum = 15

# Logic : sum =  n + (n-1) + (n-2) + (n-3) + .... + 1.
#         sum = n + sum(n-1)


def sumNto1(n):

  if n == 0 :
    return 0 # coz sum needs to get added.
  
  sum = n + sumNto1(n-1)
  return sum # will start executing once the recursive call get ends.
  
print(sumNto1(5))

# Q4 : WA Recursive Programm to print Fibonacci Seeries nth number or term  -
# Input : n = 7
# Output :  8  (as, 7th term in  0,1,1,2,3,5,8 is 8.)

# And, Further Print the Fibonacci Complete Sequence till nth term.
# Input : n = 7
# Output : 0,1,1,2,3,5,8 is 8 (Total 7 number from 0 to till 8)

''' Fibonacci Sequence are those whose first element is 0 and next element is 1 and then further elements are sum of previous two elements.

# Nth term of fibonacci Sequence :- first two terms are Fixed.
  
    nth term = (n-1)th term + (n-2)th term 
       1     =     1        +       0   (here n = 3)
       2     =     1        +       1   (here n = 4)
       3     =     2        +       1   (here n = 5)
       5     =     3        +       2   (here n = 6)
       8     =     5        +       3   (here n = 7)

'''
# Printing Only the Nth term of Fibonacci Series as per user want nth term only-
def fibonacci(nth):

  if nth == 1: # First Term is zero at, nth = 1
    return 0
  elif nth == 2: # Second Term is 1 at, nth = 2
    return 1
  else:
    return fibonacci(nth - 1) + fibonacci(nth - 2)

print("5th Term in Fibonnaci Sequnce : ",fibonacci(5))
print("6th Term in Fibonnaci Sequnce : ",fibonacci(6))
print("7th Term in Fibonnaci Sequnce : ",fibonacci(7))

# Now, Let's Print the Complete Fibonacci Sequence till nth term -

def fibonacci_Sequence(n):
    
    for i in range(1, n+1):
       print(fibonacci(i))

fibonacci_Sequence(7)  # We get till 7th term all Fibonacci Sequence.


