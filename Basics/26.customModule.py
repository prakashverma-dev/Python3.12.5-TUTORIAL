

#3. User-Defined/Custom Module: - Custom or userDefined Module is a Python file saved with .py extension with implemeneted his/her logic for solving some problem and It is ready to use it later anywhere by importing it with 'import' keyword on top of code.

# i) To create a Custom or user-defined module : Write the desired runnable code in a file with .py extension and save it. NOw, we are ready to use 'this specific module' file in other files, by using the import statement.

# Note : Dont create file name starting with number, follow Python Naming rules for Indentifer to name any user Defined python module.Otherwise Cause error while importing. 


# A module/user-defined module file can have methods, function, objects, class, variables. To Import this either follow two syntax -

# a) dot notataion : first import the 'module_file' in the program and then using dot notation to access all methods/functions/attributes like <module_name>.<method_name()> for methods accessing and <module_name>.<variable_name> for accessing varibles/attributes.

# Syntax : Syntax : import <main_module_name>

# b) using 'from' keyword : To import directly the desire methods/functions/variable from main module, start with 'from' keyword then followed by <main_module_name> then followd by 'import' then sub-methods/variables(which can seperated with comma when importing multiple sub-methods/variables) -

# Syntax : from  <main_module_name>  import  <function/methods/variable_name>, <function/methods/variable_name2>, ...

# To Import directly all variables, function, objects whatever present in the main module, use star(*) in place of multiple importing -

# Syntax : from  <main_module_name>  import  * 

# Note : If you import with *, then it has own advantages and disadvantages. coz it imported all sub-variables like function, methods whateevr present in the main module at time.

# Note : When we import user-defined module, It searches module_file in the same/current directory, if not found we cant import it. So, while creating custom module file, remember to create file in same directory. 

'''
# Note : Searching/Locating Python Module : -

Whenever a module is imported in Python the interpreter looks for several locations. First, it will check for the built-in module, if not found then it looks for a list of directories defined in the sys.path. Python interpreter searches for the module in the following manner -

-->First, it searches for the module in the current directory.
-->If the module isn't found in the current directory, Python then searches each directory in the shell variable PYTHONPATH. The PYTHONPATH is an environment variable, consisting of a list of directories.
-->If that also fails python checks the installation-dependent list of directories configured at the time Python is installed.


# Directories List for Modules : Here, sys.path is a built-in variable within the sys module. It contains a list of directories that the interpreter will search for the required module.

import sys    # imported sys module
print(sys.path) # Accessing sys.path, shows system path Directories List for Modules.

'''

# Let's Create a calculate.py file in same director folder, with logic to add two numbers and substract two number -

# (A sperate file, not here -)
# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x - y

# Now, Lets import user Defined Module -
import calculate

# print(calculate) # an object with holding up attribites/propertiers and methods to be executed.
# Note: When we import main module file, we receive an object containing all the variables/methods/function. To use all these, use dot notation.

print("The sum is : ", calculate.add(3,4))
print("The Difference is : ", calculate.sub(4,3))
print("The name is : ", calculate.name)
print("The dictionary is : ", calculate.person1) # accessing dictionary
print("The dictionary's age is : ", calculate.person1["age"]) # accessing dictionary 'age' property


# Importing Directly the calculate's functions and variables in one-line using 'from' keyword -
from calculate import add,sub, name

print("The sum is : ", add(10,4))
print("The Difference is : ", sub(10,2))
print("The name is : ", name)

# Importing module's all present methods/variables/object with star(*) keyword  : It replaces above one, It is shorter synatax to import whatever present in main_module -

from calculate import *
print("The sum is : ", add(50,4))
print("The Difference is : ", sub(10,2))
print("The name is : ", name)
print("The dict is : ", person1)

# Importing main module with re-naming it : We can rename the module while importing it using 'as' keyword followed by new_module_name/alias_name.

# Syntax : import <module_file_name> as <alias_name>

# Note : After importing with alias name, old_module_name no more longer exist for same file.

import calculate as cal 

print("The sum is : ", cal.add(1,4))
print("The Difference is : ", cal.sub(3,3))
print("The name is : ", cal.name)




