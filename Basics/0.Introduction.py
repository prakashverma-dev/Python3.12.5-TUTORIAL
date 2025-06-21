""" 

#  Why Python ?


1. Python has a simple and fewer syntax lines like reading simple English, unlike other languages such as C, C++, Java, etc.

Example : Get First three characters from text "Hello World" i.e Hel  -

C# (C sharp) :  str.Substring(0,3)
Javascript :  str.Substr(0,3)
Python :  str[0:3]   ; Clean and simple the python language is.

2. It supports object-oriented programming, making writing reusable and modular code easy and It is a high level language.

4. Python runs on an interpreter system, meaning that code can be executed on REPL(Read Evaluate Print Loop) on the terminal the system.


5. It supports automatic garbage collection, an automatic memory management technique, where Python automatically manages memory allocation and release i.e deallocate memory automatically which are no longer required by the program.


6. Python has a vast collection of libraries and frameworks, such as NumPy, Pandas, Django, and Flask, that can be used to solve a wide range of problems.

Web development (Server-side) - Django Flask, Pyramid, CherryPy

In Data Science, Python libraries like Numpy, Pandas, and Matplotlib are used for data analysis and visualization.
Python frameworks like Django, and Pyramid, make the development and deployment of Web Applications easy.


7. Python is multi-purpose languages for data analysis, AI/Ml role, automation script, Web apps, mobile apps, desktop apps, sofware testing, Hacking.



#What is Programming language :- It is a process of creating a set of instructions that tells a computer how to perform a task.

Computer understands only 0 and 1, which indicates in circuit as 1 --> Current Flows/ Switch ON;  0 ---> Current Doesnot FLow/Switch OFF.

0100111----> Machine Code That only understands only by Computer

Source Code  ------> 01011 (Machine Code)
(High Level Languages:C++, Java, python)



#What is Python : Python is a general-purpose, dynamically typed, high-level, compiled and interpreted, garbage-collected, and purely object-oriented programming language that supports procedural, object-oriented, and functional programming.

#  Python is a High level language, cross palform, huge community and large ecosystem programming language.
  
#Various Python Impletation : It is as per needs such as, cPython for Python, Jython for Java, IronPython for C++, PyPy for subset of Python.




#How cPython Executes Python Codes : 

C/C++ ----cCompiler-----> Machine Code; Directly converts into Machine Code without any ByteCode conversion in between like C#, Python, Java. Thus, Here It is not run on interpreter system as directly code gets converted into Machine code.

Note : In C,C++ Progamming Languages where cComplier directly converts c or C++ code into Machine code(00112); without any bytecode conversion inbetween so that these languages are not machine portable. Since Machine code specific to type of CPU and Operating System(Windows, Linux, Mac) means suppose if machine code gets executed on Windows, can't be run on MAc or LINUX. Thus, C and C++ are machine dependent languages for Mac or Windows or Linux.


Then Java came to solve this problem to be the language of Machine Dependent for Mac/Window/Linux. Java compiler doesnot convert source code into machine code directly instead it compiles into a portable language called javaByte code(which is not specific to a hardware platform), Now Java provies a interpreter called JavaVirtualMachine which converts the JavaBypte code into the Machine code. With This model, we can run  javabyte code on any platform that have a JVM.

Java ---compiler--> java ByteCode ----JVM(java virtual machine)--> Machine Code
    

Whereas, C#, Java, Python, Javascript  --Machine Independent coz of Conversion into first into portable language i.e into bytecode first then unto machine code.


Python ---cPython--> Python ByteCode ----PythonVirtualMachine-->Machine Code



 

#Version of Python : There are two version of python out there -

a) Python2 : Legacy Version of Python, supported untill year 2020.

b) Python3 : Python for future.

#Installation of Python : Head over to python.org > Install LAtest version of python in system i.e Currenly Python 3.13.2   > Check Add Python.exe to PATH while installation Must .

Check Installed or Not On Your System(On Windows) : Open Terminal/CMD > python --version

On Mack : python3 --version


#Python Interpreter : Python Comes with built in interpreter that means whenever python installed on sytem code can be executed on REPL as soon as writted and gets execued.
# 
# This is Terminal of Widnows whenw we enter into python environment space by entering >python 

Then, we can perform all mathematical operations like -

To come out of Python REPL : Hit> ctrl+Z + Enter (for Windows); OR, HIt > quit() + Enter to return to the OS prompt.

C:\Users\praka>Python
Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+2
4
>>> 2>1
True
>>> 1>2
False
>>> 2>
  File "<stdin>", line 1
    2>
      ^
SyntaxError: invalid syntax
>>>

Note : In programming language syntax error is similar with Grammer in english.


#Run Python Code out of Python Interperter/Interactive Shell  : To run python code either we have 

a) Code Editor : VSCode(or, plane text .py file), Atom, Sublime
b) IDE(Integrated Developement Environment) : PyCharm(code-editor for python)


#VS Code : Download VSCode > Add 'Python' From Microsoft Extension (Get Linting, Autocomplete, code formatting, code snippets, unit testing, debugging)  > Create a file hello.py> print("Hello world!!)

linting or linter: checks the error in python and tells us. 
e.g print "Hello World" or 2+ (pylint works)
PEP(Python Enhancement Proposals) : In python community, there are a lot of documnet present which are called as PEP(python enchancement proposals).
 
There are 1 to Many Number are PEPs present over python site, among these one most popular is PEP-8 which is defined for "Style Guide for Python Code". It is use for code formatting and styling it in a good formatted way.
e.g: x=1(acc to pep8 it looks ugly coz there is no space before and after assignment operator, to do automatically add pep8 extension in ur vs code -)

> add 'autopep 8' extension : Python Code Formatter extension.

#Ways of Running Python Code :- Can be run by -

a) Open Terminal(ctrl+`) In VS Code o r In File Location on system > python <nameofFile.py>

b) With added Python Extension, We get play button to run code immediately.

-----------------------------------------------------------------
                                    

#Python First Program :- Create a file with .py extension, print "Hello World" text -

print("hello world") > Hit Run on Plybutton or Hit terminal>pythjon fulename.py or python filename

Note : Python uses bydefault a new line  to complete a command, as opposed to other programming languages which often use semicolons or parentheses.


Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose


-----------------------------------------------------------------------

                          chapter - 02

#Standard 'Output' In Python :- We use python inbuilt print() function to print the specified message to the screen, or other standard outputs -              

Syntax : 



print(arg1, arg2, arg3,..., sep="-", end=" ", file=file, flush=flush ) : takes minimum one argument and maxium as per use, seperated each argument with comma(by default) and arguments could be value, string, object etc as per use-cases.

Optional Arguments are sep, end, file and flush for printing output with more variations.

sep='separator' 	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
end='end'	 Optional. Specify what to print at the end. Default is '\n' means to next line.

file	Optional. An object with a write method. Default is sys.stdout
flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False.

"""

# Print() Statement Various Usecases : -

# Storing some values into variables and printing them -

name = "Isha"  # string datatype
roll_number = 17  # integer datatype
percentage = 95.8  # float datatype
is_student = True  # Boolean datatype


# 1. Printing a string/text or any datatype directly -

print("Isha is a good girl")
print(17)
print(True)


# 2. Printing Multiple Varibale values or Different Datatypes in same line with one space added bydefault(comma specify the one space seperator bydefault ) -
print(name, roll_number, percentage, is_student)


# 3. Printing Multiple Varibale values with dash seperator(we can use any seperator), sep="-" or sep="-->"
# (sep=" " bydefault sep provides a space)
print(1, 2, 3, 4, sep="-->")  # 1-->2-->3-->4


# 4. Printing Multiple Varibale values or Multiple Arguments with each next line with specifying sep="\n" argument passed - (sep=" " bydefault it is one space, comes in same line)

print(name, roll_number, percentage, is_student, sep="\n")

# 5 . Printing same argument i.e same string in two lines with escape character '\n'-
print("Hello\nWorld")

percentage = 94.3  # varibale value get updated, not new varibale get assigned.


# 6. Printing Direct Any python 'Expressions' -
print("My percentage decreased to", percentage - 1.0)  # 93.3


# concatination of Different Datatypes : - if both datatype is same then concatinate(+) works else it will throw an error. Ex: if both datatype are strings, then after concatinate(+) both strings will get joined and if x = 4 and x =5 --> then after concatination(+) both integers here get added, case:III- if both datatype is different then throw an Typeerror as concatination doesnot work-
# print("Hey Rowy"+5) #does not work
print("Hey Rowy", 5)  # works

print("Hey Rowdy"+"5")  # works with no space
print("Hey Rowdy", "5")  # works with one space added

# Example-

# 7. Printing all datatypes together with (+) for same datatype only and comma(,) can be used for both cases i.e for same datatype and different datatype -

print("My name is"+name+"and roll number is", roll_number)
print("I scored", percentage, "% in exam, My overall score is", is_student)

# 8. Printing two print statement values in same line with space added, end=" " argument -(end="\n" by default it is next line)

print("My name is"+name+"and roll number is", roll_number, end=" ")
print("I scored", percentage, "% in exam, My overall score is", is_student)


# 9. Printing Python expression/variables mixing up with 'string' using 'formatted string or f-string/F-string -


# Formatted String or f-string : It is a way to formate the string in better way where we can mix-up expression value i.e variable or Python expresion with strings easily -

# To use formatted string literals : Begin a string with f or F and then string any single/double/thriple quotes then mix up string text with variables or Python expression, where variable/Python Expression while mixing up with string must be surrounded with curly braces{} and finally ends the string with single/double triple quotes. Rememeber, This always returns a string as whole string literal mix-up.


# Ex1 : 
first = "Prakash"
last = "Verma"
age = 24

# using f-string/F-string to formate the string -
full = f"User first name is {first} , last name is {last} and age is {age}"

# OR

full2 = F"User first name is {first} , last name is {last} and age is {age}"


# OR, Could use any 'Python Expression Direct As well' -

full = print(f"{len(first)} {last} ")

full = print(f"{len(first)} {last} {4+5} ")

print(full, type(full))  # <class 'str'>
print(full2, type(full2))  # <class 'str'>


# Ex2: 
x, y, z = 2, 3, 4

print(f"The value of x is {x} and y is {y}")
print(F"{x} {y} {z}")


"""


#Comments In Python : - Whatever written in comments will be ignord by python interpreter. It is use to instruction to reade or developer.

a) Single Line Comment :  It can be done by # adding before your comments.

ex :  #This is commment which is ignored by interpreter or compiler of python

b) Multiline COmmnent : Python does not really have a syntax for multiline comments like other languages. To add a multiline comment you could insert a # for each line OR, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:


"""
