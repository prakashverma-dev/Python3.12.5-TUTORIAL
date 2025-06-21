

# Four Pillars Of OOPs: - In any programming language, there are four pillars of object oriented programming(OOPs) : -

# a) Abstraction
# b) Encapsulation
# c) Inheritance
# d) Polymorphism


# Inheritance : In Real-life, we inherite many things from others. ex: We inherite good qualites from our parents and our parents has also inherited good qualities from our grand-parents.

# Similary, In OOPs when we have some attributes and mathods defined/own by some class, then why we agian going to define same, just we inherite(le-lena) that class into our current class i.e child class.By doing this we follows the OOPs 'DRY Concept' which is 'DON'T Repeat Yourself' Concept. 

# Thus,  When one class(child/derived) inherites/derives the properties/attributes and methods from another class(parent/base).

# Note : In Inheritance, Top Class is also Called as Super Class/Parent Class/Base Class and SubClass is also called as Child Class/Derived Class.

# Example :  Suppose, We have Car As Top-SuperClass have start(), stop() methods and one property as 'color' and then we have another sub-Car as ToyotaCar which also needs the same properties and method from superClass.SO, In python to inherite superClass into subclass we use parenthesis after subclass then we mention the 'superCLass name', now subclass have all the properties/method acccess from superclass into child class -

'''

Class Car:
        Start()
        stop()
        color;


class ToyotaCar(Car):
        -----
        


# Synatax : 

class SuperClass:
    # Attributes and methods of superclass go here.

class SubClass(SuperClass):
    # Addition attributes and methods of the subclass go here. 


'''
# Creating the Parent class -
class Car:

    design = "anonymous"

    def __init__(self, color):
        print("Constrcutor function call from SuperClass")
        self.color = color

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

# Creating the Child class -
class ToyotaCar(Car):
 
    def __init__(self, name):
        self.name = name

# Creating objects from child class-
car1 = ToyotaCar("fortuner", )
car2 = ToyotaCar("prius")

print(car1.name)
print(car2.name)

# Calling methods from SuperClass-
print(car1.start())
print(car1.stop())

# Calling attributes from SuperClass-
print(car1.design)  # SuperCLass Attribute

# print(car1.color) # SuperCLass Intance Attribute, We could not able to inherite, For this we need to use super() inside the child constructor function, We wll see below how to do so -


# Super() Function In ChildClass: super() function used inside childClass to access mainly the constructor function attributes from the Parent Class. It allows us to access all properties and methods from parent class by just sepcifying the super() function then dot notaion to call what we want to call from aprent class -

#  super().__init__(paramter)  ---> To map/call the constructor function instance attributes from the parent class into the child Class. By Specify super() function we get access to parent class then by dot convention we can access all properties and methods from parent class but as well know by doing heritance we get all access bydefault except only the constrcutor function attributes from parent class. so that we could do with super() function.

class Car:
    design = "anonymous"

    def __init__(self, color):
        print("Constrcutor function call from SuperClass")
        self.color = color

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):

    def __init__(self, name, color):
        # Now we mapped the Intance attribute from Parent class into the child class easily using super() method followd by __init()__ function with passing the accessing paramerts in it.
        super().__init__(color)
        self.name = name

        super().start() # we also call methods from superClass easily if needed using super() function.


# Creating objects from child class-
car1 = ToyotaCar("fortuner", "black")

print(car1.name)

# Calling methods from SuperClass-
print(car1.start())
print(car1.stop())

# Calling attributes from SuperClass-
print(car1.design)  # SuperCLass Attribute

# Calling Instance attribute 'color' from SuperClass-
print(car1.color)  # SuperCLass Instance Attribute




# ---------------------------------------------------------------
'''
# Types of Inheritance IN OOPs : - There are five type of Inheritance in OOPs -


a) Single-Level Inheritance : - When there is single Child Class Inherites from single Parent Class, called Single-level inheritance.

                BaseClass/ParentClass
                    |
                ChildClass    

 Ex: Above basic example.               

b) Multi-Level Inheritance : - When the child Class Derives or inherites properties and method from parent class and parent class inherites from his parent and so on, known as Multi-level Inheritance. Multi-Level Inheritance is at one hirachly level.

            BaseClass/GrandParentClass
                    |
                ChildClass/IntermedaryClas
                    |
              ChildClass/Derived Class  
   
# Note : Here, There can be more no of Derived Class can be possible in single hirachly position.
              
        '''
# Example of Multi-Level Inheritance : -

# Creating the Parent class -
class Car:
    def __init__(self, color):
        print("Constrcutor function call from SuperClass")
        self.color = color

    @staticmethod
    def start():
        print("car started 2...")

    @staticmethod
    def stop():
        print("car stopped 2...")

class ToyotaCar(Car):

    def __init__(self, name):
        # super().__init__(color)
        self.name = name

# Creating another Child class -
class Fortuner(ToyotaCar):
    def __init__(self, egnation):
        self.egnation = egnation

# creating objects =
car1 = Fortuner("Diesel")

print(car1.egnation)
print(car1.start()) # Calling from GrandPArent Class


# c) Multiple Level Inheritance: - When a child class inherites properties anf methods from more than one parents at a time. with sepcifying childClass(A,B) -

                # ClassA/BaseClassA            ClassB/BaseClassB
                                        # |

                         # ChildClass(A,B)/DrrivedClass 

# Note : Here, More than one pArent classes can be possible.

class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"    
class C(A,B):
    varC = "welcome to class C"    

#Creating object from Class C -
c1 = C() 
print(c1.varA)
print(c1.varB)
print(c1.varC)

'''
# d) Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

Example : ClassA: 
            ---
          ClassB(A):   ClassC(A):       ClassD(A):
             ---             ---              ---

#e) Hybrid Inheritance: A combination of two or more types of inheritance.

Example: ClassA:
            ---
         ClassB:
            ---

         ClassC(A,B):
            ---

         ClassD(C):
            ----

'''
