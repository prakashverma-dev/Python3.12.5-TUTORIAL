

# Abstraction : It is one of the Pillar of OOPs. Abstraction means chupa-hua. Abstraction is a process of hiding implementation details of a class means how does a class implemented hided and only showing the essensitail feature or details to the user which actually needed. tus, Abstraction tells hide all unncessary things from user i.e implemenation and only shows the necessaru things to user.

# Abstraction tells that focus on the 'what of an object do' rather than 'how the object do'.


# Ex: Suupose, a car when starts we only focus on starting, not how it interally get started from engine and what are the steps it took to start we werenot interested.

# Python some Inbuilt function like text.replace(), text.upper() etc. we just use that without worring that how it has been implemented.


class Car:
    def __init__(self):
        self.accelerator = False # Initially all are False means Car is stopped.
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car Started")

car1 = Car()       
car1.start() # Now Here this method get executed, we didnot worried/concern about other steps like clutch, accelerator to be get True which happened at run-time. We didnot see uneccesary details in runing this method.

# Hence, In Code whenever we hides unnessary details and only shows up the nessary details to user known as abstraction process.

# Abstract Class : An abstract class may contain abstract methods, which must be implemented by its concrete subclasses. By using Abstract Class we dont create any object but we can inherite into another subclass.

# Example : 

#Animal is Abstract Class which just doing -
class Animal:
    def speaks():
        pass

class Dog(Animal):    
    def speaks():
        print("Dog Speaks")

class Cow(Animal):    
    def speaks():
        print("Cow Speaks")


# --------------------------------------------------------------- 

# Encapsulation : - It the procces of bundling/wraping data(Attributes) and methods(functions) into a single unit(called class) and restricting "sensitive" data is hidden from users.

# It is the  basic principle of OOPs(object oriented programing) which tells bundle up the attributes(data) and methods(functions) togther in one entity, as class.

# A class is an example of encapsulation as it encapsulates/binds all the data(attributes) and related functions(methods) in single unit like a capsule, known as Encapsulation.

# Encapsulation = Bundle of (Attributes + Methods)


'''
The meaning of Encapsulation, is to make sure that "sensitive" data is hidden from users.

To achieve this, you must declare class variables/attributes as private (cannot be accessed from outside the class).

If you want others to read or modify the value of a private member, you can provide public get and set methods.

#Real-Life Example : Think of an employee's salary -

The salary is private - the employee can't change it directly
Only their manager can update it or share it when appropriate

Note : Encapsulation works the same way. The data is hidden, and only trusted methods can access or modify it.

Why Encapsulation?
a) It is considered good practice to declare your class attributes as private (as often as you can). Encapsulation ensures better control of your data, because you (or others) can change one part of the code without affecting other parts.
b) Increased security of data.


'''





