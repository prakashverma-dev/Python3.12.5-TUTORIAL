'''
# What is 'pip' : The 'pip' is the package manager for python like we have 'npm' pachange manager for nodejs. We use 'pip' to install any external-module or package which is not inbuilt in python, via terminal to our sytem, like this -
# Syntax : >pip install <external_module_name>

Hit to terminal, Run following command -
>pip install flask    # ---> Installs 'Flask' Module 
>pip install pyjokes  # ---> Installs 'pyjokes' Module
>pip install camelcase


# 1) To Check if PIP is Installed In Your system or NOt : Hit terminal or Navigate your command line to the location of Python's script directory, and type the following -

> pip --version   # pip 24.2 


#2) To Show All Installed Packages/external Modules In Your system : Use the list command to list all the packages installed on your system -

> pip list


# TO check a perticular module/package installed or exist(With its version and location) -

> pip show moviepy

# To uninstall and Install a perticular(might be old) version -
# Example -
> pip uninstall moviepy
> pip install moviepy==1.0.3
 
#3) To Remove a Installed Package : Use the uninstall command to remove a package-

> pip uninstall camelcase

Then, PIP Package Manager will ask you to confirm(y/n) that you want to remove the camelcase package: Press 'y' and the package will be removed.






-----------------------------------------------------------------------


# What is a Module/Package In Program :-  Module or Package in programming is nothing but a set of well written codes for doing some specific task, which we just import in our code with 'import' keyword and easily use it.


Modules/Packages contains some functions/methods/classes/variables to work with problems.


# TYPES OF MODULES  : - There are mainly three types of modules or packages in Python -

1. Built-in Modules (Preinstalled in Python like math, date, os, random, string etc.) 
2. External Modules (Need to install using pip like numpy,tensorflow, flask, pyjokes etc.) 

3. User-Defined Modules (User Creates his custom package/module by writing own logic code and save it with .py file and then import it anywhere)


# To use any type of modules/package : Import that Externally Installed/ Inbuilt/user-defined modules or package via 'import' keyword followed by <module/package name> and then use it code with calling its methods or properties/attubues -

Syntax : import <module_name>

Syntax : from  <module_name>  import  <function/methods/variable_name>   --->  To Import Directly the sepecific method/function/variable of that module into our program, we use 'from' keyword.


 
'''


#1. External Modules : External Modules are those which python does not have inbuilt in their library, we need to install via exteral sources via 'pip' command followed by install and then <module_name> after that we can use it -

# A external module is a code library written by somebody else (usually) which can be imported and used in our programs. There are many popular external modules in python -

# Ex: flash(for developing web-apps), django(a packaage or module), pyjokes(for generating random python jokes for us), camelcase(working with paragraph) etc.  

import pyjokes

myjoke = pyjokes.get_joke()
print(myjoke) # we get random python jokes

# using "camelcase" module : -

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt)) # Lorem Ipsum Dolor Sit Amet
# Note : hump() method capitalizes the first letter of each word.




# 2. In-built Modules : There are several built-in modules which are pre-installed in Python, which you can import in code without installing it seperatly like external modules and then use it. 

# math, random, string, os, datetime, platform etc are Inbuilt/pre-installed modules.


#1) Python 'random' Module : Though Python does not have a random() function to generate a random number, but Python has a module called 'random' that can be used to make random numbers with variation of random numner in result-

# Random module have following methods to generate number with variations -

# i) random.randint(a, b) : This function generates a random integer including the both specified a and b range (both inclusive).

import random
x = random.randint(1, 10)
print(x)  

# ii) random.uniform(a,b) : The uniform() method returns a random floating number including the two specified number range (both included).

print(random.uniform(1,5)) # 2.22223, 4.83434399684379


# iii) random.randrange(a,b) : The randrange() method returns a random number from the specified range a(Inclusive) and b(Not Inclusive).

import random
print(random.randrange(1,5))

# OR, using 'from' keyword to directly call module's methods/functions/variables -
from random import randrange
print(randrange(1,5))


# iv) random.choice(<iterable_object>) : The choice() method returns/picks a random item from specified iterable object/sequence. Iterable object can be a string, a list, a tuple, a range of number or any other kind of sequence.

import random

mylist = ["apple", "banana", "cherry"]
text = "WELCOME"
myrange = range(1,4) # 4 NOt Included

print(random.choice(mylist)) # aaple, cherry
print(random.choice(text)) # W , O , E
print(random.choice(myrange)) #1, 3,1, 2

# v)  random.random() : It Doesnot not take any arguments. The random() method returns a random floating number between 0 and 1.

import random
print(random.random()) # 0.34344. 0. 8999993

# vi) random.sample(<iterable_object>, k)) :  The sample() method always returns a list which contains randomly selected multiple unique Items(as per 'k' value provided) from the iterable object/sequence.

# Note: The specified number (k=2) cannot be longer than the length of the original sequence.

import random

mylist = ["apple", "banana", "cherry"]
text = "HELLO"
myrange = range(1,6) # 6 Not Included

print(random.sample(mylist, k=2))
print(random.sample(text, 2))
print(random.sample(myrange, 2))

# vii) random.shuffle(mylist) : The shuffle() method only takes a list and reorganize/suffle the order of the items in the list with keeping all items and modifies the original list.

# Note: This method changes the original list, it does not return a new list.

import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)




# -------------------------------------------------------------------

#2) Python 'string' Module : - Python 'string' module is the collection of all string constants which contails all ASCII letters/Characaters for strings like uppercase, lowercase,digits and punctuations which correspond to ASCII CODE in program.

import string

print(string.ascii_letters) # Prints all ASCII letters, both lowercase and uppercase.
print(string.ascii_lowercase)# Prints All lowercase ASCII letters from A_Z.
print(string.ascii_uppercase) # Prints All uppercase ASCII letters from a-z.
print(string.digits) # Prints All ASCII decimal digits from 0-9.
print(string.punctuation) # Prints All Special Characters like #, %, $, ^ etc.

print(string.hexdigits) # Prints All characters used in hexadecimal numbers from 0-9 and A-F.
print(string.whitespace) # PRints all the white space present in program like spaces, tabs, and newlines.
print(string.printable) # Prints ALL ASCII characters at a time, including letters, digits, punctuation, and whitespace(spaces, tabs, and newlines).

# Here, all string value return is type of 'string datatype'.
import string

x = string.digits
y = string.punctuation
print(type(x)) # <class 'str'>
print(type(y)) # <class 'str'>


# ---------------------------------------------------------------------------

#3) Python 'datetime' Module : A date in Python is not a datatype of its own, but we can import a module named 'datetime' to work with around dates with its methods and properties -


# The 'datetime' module is further categorized into 6 main classes -

# i) date() : It is use to work with only Date. Its attributes are year, month, and day.


# a) To create a Date : use date() method of 'datetime' module with following syntax -

# Syntax : datetime.date(year, month, day)

import datetime
mydate = datetime.date(2025, 3, 2)
print(mydate) # 2025-03-02

# b) To Get Current Local Date Only : To get current local date, use today() function of the 'date' class is used -

# today() function comes with several attributes (year, month, and day). These can be printed individually. 

currentLocalDate = datetime.date.today()
print("the Current Date is ", currentLocalDate)

print("the Current Year is ", currentLocalDate.year)
print("the Current Month is ", currentLocalDate.month)
print("the Current Day is ", currentLocalDate.day)

 
# ii) time() : It is use to work with only time. Its attributes are hour, minute, second, microsecond, and tzinfo.



# iii) datetime() : It is a combination of date and time classes. It provides both classes attributes together: year, month, day, hour, minute, second, microsecond, and tzinfo. 

# To Create a date along with time : use datetime() method of 'datetime' module with following syntax -

# Syntax : datetime.datetime(year, month, day)
import datetime

mydate = datetime.datetime(2025, 3, 2)
print(mydate)  # 2025-03-02 00:00:00

# To get Current Date and time : use either now() or today() method of datetime() object.

# Further, These now() and today() methods comes with properties like year, month, and day, time, sec etc to print all these indivisually.

currentDatetime = datetime.datetime.now()
currentDatetime2 = datetime.datetime.today()

print(currentDatetime) # 2025-06-01 20:57:23.860654
print(currentDatetime2) # 2025-06-01 20:57:23.860654

print(currentDatetime.year)
print(currentDatetime2.year)



# iv) timedelta() - A duration expressing the difference between two date, time, or datetime instances to microsecond resolution. 


# v) tzinfo() - It provides time zone information objects.

# vi) timezone() - A class that implements the tzinfo abstract base class as a fixed offset from the UTC (New in version 3.2).




# ----------------------------------------------------------

# 4) Python 'platform' Module : 'platform' module to know your user system details.
 
import platform 

print(platform.system()) # Windows
print(platform.architecture()) # ('64bit', 'WindowsPE')
print(platform.platform()) #  Windows-10-10.0.19043-SP0
print(platform.machine()) # AMD64



# --------------------------------------------------------------

# 5) Python 'uuid' module : Python has inbuilt 'uuid' package or module in it unlike other langauages, It uses to generate random unique code -

import uuid
unique_id = uuid.uuid4().hex[:6]

print(unique_id) # random, 6 character code







