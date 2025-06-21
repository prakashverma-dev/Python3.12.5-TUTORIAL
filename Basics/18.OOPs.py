'''

#1. Basic Concept on OPPs : -

# OOP stands for Object-Oriented Programming.

Almost everything in Python is an object, with its properties and methods.

We use OOPs, To map with real world scenarios, we started using objects in code.

# The flow of Programming Paradigm or Model In Sofware Development Problems -

Procedural Programming  ---> Fuctional Programming ---> Object Oriented Programing

# What is Procedure Oriented Programming(POP) :  Procedural Programming can be defined as a programming model or Paradigm where programs are executed in sequencial manner. They focus heavily on splitting up programs into named sets of instructions called procedures, analogous to functions. 

It all about doing code one by one, sequencely with or without function and data/variable data limited to function scope only, Where as In OOPs, the main focus on the object which consisist of attributes(variable_data) and as well as methods(functions).

In procedural programming, the program is divided into small parts called functions, where function_variable_data limited to function scope.

NOte : Procedural programming is about writing procedures or functions that perform operations on the data, while object-oriented programming is about creating objects that contain both data/attributes and functions





# What is Object Oriented Programming(OOP) : It is a programming paradigm or Model where the software design resolves around objects(consisit of attributes/data and methods/functions) rather than functions data only.

An object is any real-life entity that has properties i.e attributes  and behaviors i.e methods/function. For example, a parrot is an object. It has -
attributes - name, age, color, etc.
behavior/function - dancing, singing, etc.


In object-oriented programming, the program is divided into small parts called objects.


Note : Object Oriented Programming - As the name suggests uses objects in programming. Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc. in programming. The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

Note : Object-oriented programming can be defined as a programming model which is based upon the concept of objects. Objects contain data in the form of attributes and code in the form of methods. In object-oriented programming, computer programs are designed using the concept of objects that interact with the real world. 



#2. Why use OOPs Programming Paradigm over Procedure Oriented Program : -

a) OOps helps to mimic real-world entities and their interactions. Ex: Suppose a car is an real-world object or entity which has some properties and its interaction like get_flue, accelerate.

b) OOPs helps code reusuability like functions but with more concise way in OOPs.

c) For Complex Problem, Organization and maintainability of code in oops is more good.

d) OOP helps to keep the Python code DRY "Don't Repeat Yourself", and makes the code easier to maintain, modify and debug.

NOte : Tip: The "Don't Repeat Yourself" (DRY) principle is about reducing the repetition of code. You should extract out the codes that are common for the application, and place them at a single place and reuse them instead of repeating it.


# Difference bewtween Procedural Oriented Programming V/S Object-Oriented Programming : -

i) In procedural programming, the program is divided into small parts called functions.	In object-oriented programming, the program is divided into small parts called objects.

ii) Procedural programming follows a top-down approach.	Object-oriented programming follows a bottom-up approach.

iii) There is no access specifier in procedural programming.	Object-oriented programming has access specifiers like private, public, protected, etc.

iv) Adding new data and functions is not easy.	Adding new data and function is easy.

v) Procedural programming does not have any proper way of hiding data so it is less secure.	Object-oriented programming provides data hiding so it is more secure.

vi)In procedural programming, overloading is not possible.	Overloading is possible in object-oriented programming.

vii) In procedural programming, there is no concept of data hiding and inheritance.	In object-oriented programming, the concept of data hiding and inheritance is used.


viii) In procedural programming, the function is more important than the data.	In object-oriented programming, data is more important than function.


ix) Procedural programming is based on the unreal world.	Object-oriented programming is based on the real world.


x) Procedural programming is used for designing medium-sized programs.	Object-oriented programming is used for designing large and complex programs.


xi) Procedural programming uses the concept of procedure abstraction.	Object-oriented programming uses the concept of data abstraction.

xii) Code reusability absent in procedural programming,	Code reusability present in object-oriented programming.

xiii) Examples: C, FORTRAN, Pascal, Basic, etc. 	Examples: C++, Java, Python, C#, etc.


# 3. Classes and Objects :- OOPs is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOPs, object has attributes thing that has specific data and can perform certain actions using methods.


# OOPs have two major/main concept - a) Classes and b)Objects


a) Classes :- It is user-defined datatype in python, like python have predefined/built-in datatypes are string, number, list, tuple etc. 'Classes' are one of those user-defined datatype by which we can create any object which have own defined properties and methods to apply one rather like dependent on predefined properties or methods.

Classes are blueprint or template for many objects.

NOte : The building block of Object-Oriented programming in C++ is a Class. It    a user-defined data type that act as a blueprint representing a group of objects which share some common properties and behaviours. These properties are stored as data members, and the behaviour is represented by member functions.

For example, consider the class of Animals. An Animal class could have common properties like name, age, and species as data members, and behaviors like eat, sleep, and makeSound as member functions. Each individual animal object (such as a dog, cat, or elephant) can be created from this blueprint, and each will have its own unique values for the properties (like the name and age), but all will share the same behaviours defined by the class (like eating, sleeping, and making sounds).

Note : Everything in OOPs, is associated with classes and objects, along with its attributes and methods. For example: in real life, a car is an object. The car has attributes, such as weight and color, and methods, such as drive and brake.

Attributes and methods are basically variables and functions that belongs to the class. These are often referred to as "class members".

b) Object : Object is an instance of type class. There can be multiple instances of same class. Like We can create/define multiple list datatype of 'list class' at different places.

These objects mimic real-world entiries. Ex: GIven a student_form(Name :____. Age: ____, Address: ______ ) to a class to fill by each student, so here student_form is a class and form filled by indivisual students will be one instance of student_form i.e an object.

Ex2: For example -- 'Car' is Class have common properties/attributes(like length, color) and have actions/methods/functions( like get_fuel(),  get_age()  )

By above Class 'Car' we can make multiple sub-instances of it i.e called as objects which holds same attributes and methods with its own feature like objects can be of 'Car' are 'Audi' , "Nissan' and 'Volvo' .

EX: A real-life entity 'Fruit' Class have - 'Apple' , 'Banana' , 'Mango' Can be the Objects of 'Fruit' Class. 
  
An Object attributes/properties and Methods can be access with dot notation.

Note : When the individual objects are created, they inherit all the variables and functions from the class.

#4. Creating a Class In Python : - In Python, List, string, tuples are built-in objects of their respective classes. 

A Class is like an object constructor, or a "blueprint" for creating objects.We use 'class' keyword followed by classname to define a class, where class Name first char follows cap letter -

Syntax: class <class_name>:
            name = "Rahul Kumar"
            

#Creating an object of above Class :- We can create as many as objects of same class with different data passed -

object1 = <class_name>()     ---> We created an object of above class with calling here.
print(object1.name) 


'''
# Creating a Class of 'Student' -


class Student:

    # attribute i.e class attribute(variable defined inside class called attributes or class attributes)
    name = "Rahul"  # Same name defined for every object.


# Creating an object or instance of the class -
s1 = Student()
print(s1)
print(s1.name)

# NOte : The variables defined inside a class are called attributes or class attributes. All Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute


# Creating a Class of 'Car' -
class Car:
    color = "blue"
    brand = "mercedes"


# Creating an object(from class)
car1 = Car()
print(car1.color)
print(car1.brand)

# Creating another object(from class)
car2 = Car()
print(car2.color)


# Constructor Funtion / __init__ Function : It is a special function designed especially for the class which speciality is that it gets invoked automactially every time when any object is created from the Class where we directly pass the arguments value to the class call which values goe to Constructor Function. In Python, constructor function is named as __init__ function where ___init___ resembles the constructor for setting up the attributes for the obejects.

# All classes to have a init__ function/constructor function to initialize/setting up the attributes for the objects. IF we do not create constructor function then python bydefault create a constructor function for us.


# Syntax : To Defining constructor or __init__ function, Always define constructor funtion inside class, start with 'def' keyword followed by double underscore(__) and then 'init'keyword and ends with same double underscore(__).This constructor function have following paramters - a) must take self paramter(indicate created object instance) as first argument and b) next paramters(optional) to initialize the objects.

'''
class <ClassName>:
    def __init__(self, parameter1, parameter2, ):
        # Initialize instance variables here.

Here, parameter1, parameter2 to initialize the objects.     
'''

# Note: construtor/init function always takes first 'parameter' as 'self' which indicates/points the each object created by this class. Here, 'self' paramter can be any name but we use 'self' name accoss python program.

# self parameter is a reference to the current instance/object created out of the class. It allows us to create the attributes and methods for the object.Here, these defined attrbutes known as 'Instance Attributes' AND defined method known as 'Instance Methods'

# constrcutor function can have multiple parameters but 'self' parameter must be first one.


class Student2:

    demo = "We learning OOPS"  # Class attribute
    print("Function outside of init function")

    def __init__(selff, fullname=None, age=None):
        print("Adding a new student")
        print(selff)

        selff.fName = fullname  # Instance attribute  defined
        # Here, we assigned/created a new variable name 'fName' to that created objects.Here, 'fName' is Instance Attribute i.e Object attribute i.e Object Variable.

        selff.userage = age  # Instance attribute drfined


Ram_student = Student2()
# print(Ram_student)  #  print(self)   ---> Both Are same

# Note : whever any object created or invoked then constructor function auto get called.

Rahul_student = Student2()
# print(Rahul_student)  #  print(self)   ---> Both Are same


# Creating a new object with passing 'Arguments' to the constructor function -
Simran_student = Student2("Dev", 23)
print(Simran_student.fName)  # Accessing 'Instance Attribute'
print(Simran_student.userage)  # Accessing 'Instance Attribute'

print(Simran_student.demo)  # Accessing 'Class Attribute'


# NOte : Here, we used Class and Object to store 'Dev' and '23' Data, which can be stored into a string or list or tuple or dictionary datatypes as well. But we use OOPs(class and Object) to store data in more organize and hirachly way with data privacy and binding.

# Construtor Function Can be two types : - a) Default Constructor : Which get created by python, if we do not creat it, it holds only self parameter.

# b) Parameterized Constructor : It is the user constructor created where aprat from self paramter, other parameters also defined.

class Student3:

    # Class Attribute - Common to all objects
    collegeName = "ABC College"

    fName = "ByDefaultName"  # Class attribute

    # default construtor
    def __init__(self):
        pass

    # Parameterized Constructor
    def __init__(self, name, age):
        # Instance Attribute - Restricted to created object only.
        self.fname = name
        self.userage = age


# creating instance of the class -
sita = Student3("Sita", 22)
print(sita.fname)
print(sita.userage)


# Accessing Class attribute via two ways -
# a) via object created -
print(sita.collegeName)

# b) via main Class -
print(Student3.collegeName)  # gives the same name as It is a class attribute.

# Notw :  We cannot access 'Intance attributes' using Class Name Directly.It is restricted with only created objects and could be accessible from those objects.

# Note : a) If 'class attribute' have same variable name as 'Instance Attribute' then Precedance of Intance Attribute >> Class Attribute. We generally dont use same name by if used then we use for 'bydefault_value' for that variable/intance attribute.

# b) We can access 'Class Attribute' with 'Class_Name" as well as with any created "Object Names".


# Class Attributes and Instance Attributes In Class : -

# a) Class Attribute : It own by class and these attributes common to all objects created with this class.
# b) Instance Attribute : It own by construtor function which differ for each object created as per 'Data' passed to the variables.

# Note : Where to use Class_Attribute - a) The variable data which may be common for all objects that we keep inside the 'class attribute' so that it doesnot require memory again and again for each objects, if we create so indivual. b) Use in case of fallback variable values for Instance Variable under constructor function.


# A class stores two things : -
#
# a) Data(Attributes) : Class attributes(dirctly we defined in Class Scope)/Instance attribute(we create/define instance attribute for obejects using constructor method(we could done that via creating a normal method as well), why we chose construtor method not any normal method coz constructor method automatically get invoked/called whenever any object created, whereas when we would have defined instanace attributes using normal method(would worked) but we need to call that method for invoking/executing each created attributes for the class. )
#
# b) Methods : It is will be the Instance Methods means it must have self parameter, which is basically methods for created object from the class.
#
# Thus, A class is collection of two things attributes and Methods for objects.


# Creating Instance methods for objects : - To create a Intance/object methods,pass self parameter in any Normal Methods, which created under class.

class Student4:

    # Here 'name' is class attribute(work as fallback variable for Instance 'name' attribute)
    name = "Dev"

    def __init__(self, fName, age):
        self.name = fName  # Here, 'name' attribute is instance attribute.
        self.age = age

    def sayhello(self):
        return "Hello, user..."

    # Used Object attributes Inside the methods -
    def sayhello2(self):
        return f"Hello, user...{self.name}"

    def get_age(self):
        return f"Age is {self.age}"


student1 = Student4("Surya", 24)

# Calling Class attribute 'name' -
print(Student4.name)
# We can call it via any Class name as well as any created object name, as Class Attributes are 'CLASS LEVEL' attribute, accessible for both.
print(student1.name)

# Calling Object/Instance attributes 'name' and 'age' -
print(student1.name)
print(student1.age)

# Calling Object/Instance Method/s -
print(student1.sayhello())
print(student1.sayhello2())
print(student1.get_age())

# Modify Object Properties/Attributes :-  We can modify any 'instance attribute' or 'class attribute' name as well  -
student1.name = "Rocky"  # Changing Instance Attribute Value
print(student1.sayhello2())

# Delete Object Properties/Attributes : we use 'del' keyword to delete any object properties/Instance attribute as well as Class attribute or, entire created object itself.
#
# Syntax: del obj1.age      OR,    del obj1


# Whenever we create any objects from class, it occupier some memory space in computer, To delete some unwanted created object or object attribute then we can use 'del' keyword to perform same -

# Deleting instance attribute 'age' property from the student1 object -
print(student1.age)
del student1.age
# print(student1.age)

# Deleting class attribute 'name' property from the Student4 class -
print(Student4.name)
del Student4.name
# print(Student4.name)

# Deleting the student1 object completely :-
print(student1)
del student1
# print(student1)


# Static Methods Inside Class :  It is special type of method that can use inside class which dont need 'self' parameter while function defining. For defining static methods inside class we need to call 'Decorator of @staticmethod which basically converts the normal method into static method' else while executing this method ask for 'self' parameter assingning.

# Satic Methods work at 'Class Level' means any Object can access this. And this method can be directly call by 'Classname' as well as any Object Created Name. Like 'Class attributes' which is also "CLASS LEVEL".

# Decorator '@staticmethod' Converts a normal function into a static method.
# When we Convert a function to a static method, then function doesnot expect 'self' parameter as an implicit first argument.

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    @staticmethod  # decorator
    def hello():
        return "hello Prakash"


car1 = Car("ABC", "Volvo")
print(car1.name, car1.model)
# Executable coz we converted normal function into satic method. else we would have getting error.
print(car1.hello())

# We can call 'Class Level' Methods Directly via ClassName As well, when they are not associated with any objects -
print(Car.hello())

# Note : Decorator In python : 'Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it

'''

# Summary :  We basically In A class, we can create three types of methods -

 i) Constructor/init Function' : To create or initialize the attributes i.e properties for the objects.

ii) Normal Methods/Intance Methods : To create instance/object methods, we directly define any normal funtion with passing 'self' paramter as first arg after constructor function.

 iii) Static Methods : It is 'CLASS LEVEL' method, which doensot need to pass 'self' paramter which can be access diretly via Class name as well as Object name(To convert a normal function into static method, use decorator @staticmethod')

'''


# Q1. Create student class that takes name & marks Of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:

    # Object Attributes or Properties Defining using Constructor Function -
    def __init__(self, studentName, s1, s2, s3):

        self.studentName = studentName
        self.sub1marks = s1
        self.sub2marks = s2
        self.sub3marks = s3

    # Object Method to Print the average of student all subjects marks -
    def get_avg(self):

        average = (self.sub1marks + self.sub2marks + self.sub3marks) / 3
        return f"Hi {self.studentName}, Your average score is : {average}"


# Creating an object from Class/Creating an intance of class -
student1 = Student("Shyam", 23, 7, 10)
print(student1.get_avg())

# We can modify instance attribute or class attribute name as well  -

student1.studentName = "Prakash"
# print(student1.studentName)

print(student1.get_avg())  # name get changed.


'''
Q2: Write a Python class named Rectangle to represent a rectangle shape.
The class should have the following functionalities: -

a) A method named set_dimensions that takes two parameters width and
height and sets the attributes of the rectangle object accordingly.

b) A method named area that calculates and returns the area of the
rectangle

c) A method named perimeter that calculates and returns the perimeter of
the rectangle

Use this to create objects of the class and print the width, height, area and
perimeter.


'''


class Rectangle:

    # Setting up the attributes for this class(for creation of objects from it)
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    # For setting up the attributes we can also create the constuctor function(which automatically invokes whenever we create any object, we pass arguments to the class call which goes to constructor function)  -

    def __init__(self, width, height):
        print(
            f"A rectangle is created with height : {height} and width : {width}")
        self.width = width
        self.height = height

    # Method To calculate area of the rectangle from this attributes-
    def area(self):
        return self.height * self.width

    # Method To calculate perimeter of the rectangle from this attributes-
    def perimeter(self):
        return 2*(self.height + self.width)

# Creating the objects from this class -


rectangle1 = Rectangle(3, 4)

# setting dimension data to rectangle-
# rectangle1.set_dimensions(3,4)

# Printing rectangle height and width -
print("The height and width are : ", rectangle1.height, rectangle1.width)
# Finding area and perimeter of the rectangle-
print("The area is : ", rectangle1.area())
print("The perimeter is : ", rectangle1.perimeter())

# Creating another rectangle, (here we use construtor function to initialize the attributes for objects)

# when we pass arguments to class call then, it directly goes to the constrcutor function.
rectangle2 = Rectangle(5, 3)

# when we pass arguments to class call then, it directly goes to the constrcutor function.
rectangle2 = Rectangle(1, 7)


# Access Modifiers : - These are used to control the visibility/accessed of attributes and methods/functions of the class.

# Access specifiers control how the members (attributes and methods) of a class can be accessed.

# They help protect data and organize code so that only the right parts can be seen or changed.

# Access Modifiers is of three types :
# a) Public Access Modifier: When a class attributes and methods can be accessed directly by any class, ouside of class, within class or anywhere, are Public Access Modifier. As of now whatever we studied are fall into Public Access Modifier where the attributes and methods where accessed ouside of the class.

# public methods and fields can be accessed directly by any class.

# Example :
class ABC:
    def __init__(self):
        self.check = None  # 'Check' is Public Attribute.

    def get_number():  # 'get_number()' is Public method.
        pass


obc1 = ABC()
print(obc1.check)
print(obc1.get_number())


# b) Private Access Modifier : Private methods and fields can be only accessed within the same class it is declared, Not outside of class, even from derived class from supper.

# Private Attributes and Methods in Python : -  Private Attributes and methods are meant to be used only within the class and are not accessible from outside of the class. Python uses the '_' symbol to determine the access control for a specific data member/atrribute or a member function/method of a class.

# Generally, In OOPs, Sometimes we do not want our attributes and methods from class, could access outside of the class Scope, then we use 'Private attributes or methods' by putting double underscore(__) before defining that attribute or method for class  -

# Note : Basically, when we define any private attribute or private methods within class then most of the time, some other method inside class trying to use these private methods or private attributes. thus, Internally we can access priavte attribute and method anywhere within class.

# Example : Whenever any information is sensitive or we do not want to pass outside of the class then we make that attribute or method as private -

class Account:

    __name = "anonymous"  # here, '__name' is private class attribute

    def __init__(self, acc_no, acc_pw):
        self.acc_no = acc_no
        # Here, '__acc_pw' is now private instance attribute.
        self.__acc_pw = acc_pw

    def get_password(self):
        # hence, we can access private attribute inside class only not outside of the class.
        print(self.__acc_pw)

    # Making a method private -
    def __hello(self):
        return "Hello person"

    # Calling Private method inside class for another method -
    def welcome(self):
        return self.__hello()


class SubAccount(Account):

    def __init__(self, acc_no, acc_pw):
        super().__init__(acc_no, acc_pw)


# A user creating his account from class 'Account' -
acc1 = Account(12345, "abcde")

print(acc1.acc_no)
# print(acc1.acc_pw) # Accessing acc_password printing or making it public is security gap and priavacy glitch.

acc1.get_password()  # calling method to execute.

# print(acc1.name) # will not able to access class attribute
# print(acc1.__hello()) # will not able to access method

print(acc1.welcome())

subacc1 = SubAccount(12345, "abcde")
# print(subacc1.name)  # Not accessible from Parent Class as well.

# Note : In Python, we conceptually make private attribute or methods, not exacly like other programming lang(java, c++). since Python uses the concept of Name Mangling for achieving data hiding.

# Unlike other languages like Java and C++, Python uses Conceptual Implementations of Public/Private Data Hiding or Scoping, It doesnot exacly same like OOPs in Java, C++.


# c) Protected Access Modifier : Members(attributes and methods) declared as protected can not be accessed outside the class, but they can be accessed within class as well as in child classes or subClasses i.e Inheritance Classes.

# We protect aatributes and methods by using a single underscore "_" before defining any aatributes or methods for the class.

# Protected methods and fields can be accessed within the same class as well as in its subclass.

# Note that: the python interpreter does not treat it as protected data like other languages, it is only denoted for the programmers since they would be trying to access it using plain name instead of calling it using the respective prefix.


class ABC:

    _name = "Rahul"
    def __init__(self):
        self._check = "yes" # '_Check' is Protected Attribute.

    def _get_number(self):  # '_get_number()' is Protected method.
        pass

obc1 = ABC()
# print(obc1.name)
# print(obc1.check)
# print(obc1.get_number())

class ABC2(ABC):

    def __init__(self):
        super().__init__()
        print(self._name)
           

abc2 = ABC2()


# Summary : In OOPs, by default all aatributes and methods are Public, as per use-case and requirement we can make them either protected or private.
