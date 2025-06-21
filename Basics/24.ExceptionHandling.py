# Exception Handling in Python : Suppose, we are wrriting code and we are unaware that code might produce an error at run-time and further after error occured complete code get interrupted and wait for the error to resolve to procced python compiler to execute further. To solve this, Like other programming laguage Python have also 'Exception Handling' try-except-else-finally' block.

# In Programming, Exception means an error occured in the code. then Python interpreter will normally stop and generate an error message.These exceptions can be handled using the try statement.The Main motive of exception handing is that 'to not stop the flow of the code'.
'''

try:
    # We write code In try block Which Might throw an exception/error.
except:
    # When error occured, this block get executed(optional we can provde the exception Type like ValueError, TypeError, ZeroDivisionError, Exception)
else:
    # Block executed when there is no error in try block/some result get display based on if error found or not.    
finally:
    # This block get executed evertime whether an error occured or not.This is optinal block to include in exceptional-handling.

# Note : When We get an Eception, either we just throw the error or Python have inbuilt ErrorType which we can also display/throw to user for better understanding of the code/error. Built-in ExceptionsTYpes are : ArithmeticError, Exception(Base Class of all Exceptions), LookupError, SyntaxError, TypeError, ValueError etc.

# Note : While handling exception, there must try-except two block require to handle the code.


The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try - and except blocks.


Q1: Implement exception handling in python by showing division operation.

You can show exception - "ZeroDivisionError"
Input:
a = 10, b = 2
Output:
Cleanup: Division operation completed.
5
Input:
a = 5, b = 0
Output:
Error: Cannot divide by zero

Summary : We divide number if get divided by zero we get exception and throw the exception as well as we will handle the exception to not stop code further.

'''
print("Python Code Get Strarted...")
a = int(input("Enter a :"))
b = int(input("Enter b :"))

try:
    # We write code In try block, which we think that the code might produce an error or exception.
    result = a / b
except ZeroDivisionError:
    result = None
    print("Error : Cannot divide by Zero")
else:
    print("The Divison Result Is : ", result)    
finally:
    # This is optinal code of block in exception handling, Could Include or not coz it must get executed everytime whether exception occurred or not.
    print("We tested our logic!!")

print("Python Code Get Ended...")

#Q2 :Since, print(x) will raise an error, if we write the code directly without x defining.

# try:
#   print(x)
# except:
#   print("An exception occurred")
# finally:
#   print("The 'try except' is finished")  

# Here, The try block will generate an exception, because x is not defined. Since the try block raises an error, the except block will be executed. Without the try block, the program will crash and raise an error:-