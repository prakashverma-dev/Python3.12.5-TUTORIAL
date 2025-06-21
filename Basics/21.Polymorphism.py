

# PolyMorphism : It is one the pillars of OOPs. 'Poly' means many and 'morph' means forms(chehre). When one thing uses in multiple/many ways depending upon the context known as polymorphism. It get achieved through method overriding or overloading.

# The word "polymorphism" means "many forms", and In programming, Polymorphism refers the any methods/functions/operators with the same name but act/perform differently as many forms as per objects or classes.

# Types of Polymorphism : It mainly two types -
''' 1) Compile-Time Polymorphism(Method or Operator Overloading) : This type of polymorphism is determined during the compilation time of the program. It allows methods or operators with the same name to behave differently based on their input parameters or usage. It is commonly referred to as method or operator overloading.

# It is achieved through two ways - a) method Overloading : Here,  Methods with same name but different paramters and b) Operator Overloading : 

'''

# a) Built-in Functions Polymorphism/Built-in Functions Overloading  : As we known in python function works some task as per needs. Though, len() function which works differnly as per objects provided, It is the function polymorphism example -

# i) 
x = "Hello World!"
print(len(x)) # For string len() returns no of total characters in string.

# ii)
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) # For list,tuple len() function returns the number of items present.

# iii)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict)) # For dictionary, len() function returns the no of key/value pairs in the dictionary.


# b) Operators Polymorphism/Operator Overloading : - In python, we have 'operator Overloading' for best example of polymorphism -

#Operator Overloading : When same operator is allowed to have different meanings accoring to the context, called operator overloading.

# Example : In Python '+' Plus operator, polymorphism forms -

print(1 + 2)  # Here, Plus(+) Operator acts as 'Arthematic Addition'
print("Apna" + "College")  # Here, Plus(+) Operator acts as 'String Concatination' 
print([1,2,3] + [4,5,6])  # Here, Plus(+) Operator acts as 'List Merge'
print((1 + 3j) + (4+6j) )# Here, Plus(+) Operator acts as 'Complex Number Addition.'

# Thus, As per datatypes Plus(+) Operator Perform different actions or tasks, It is known as Operator Overloading and it is a type of Polymorphism.



# 2)Run-Time Polymorphism(Method Overriding In OOPs) : - This type of polymorphism is determined during the runtime/execution of the program.It is achieved thorough method overriding.

# In OOPs, Polymorphism occurs when a subclass provides a specific implementation for a method already defined in its parent class, commonly known as method overriding for OOPs.

# Polymorphism in OOPs/Method Overriding In OOPs, when we have multiple classes with heritance with common name for all class, then working of the same method name.


class Animal:
    def speaks(self):
        print("Animal Speaks")
        
class Dog(Animal):
    def speaks(self):
        print("Dog Speaks") 

class Cat(Animal):
    def speaks(self):
        print("Cat Speaks") 

class Cow(Animal):
    def speaks(self):
        print("Cow Speaks") 

#Lets Create Instance for the class -
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the same methods -
dog.speaks()
cat.speaks()
cow.speaks()

# Thus, Here same methods calls different class methods at a time tho we have the superCLass inheritance(Note: attributes or methods first look into own class if not found then go to parent or superclass)





'''

# Operators and their corresponding 'Dunder function' In Python - It is use in impletation of polymorphism for overloading, like plus(+) operator have its meaning defined in their classes for addition, concatination, merge etc. Similary way, using Dunder function we can define our own methods using OOPs class.

a + b	   #addition	    a.__add__(b)
a-b	     #subtraction   	a.__sub__(b)
a*b  	#multiplication	    a.__mul____(b)
a/b  	 #division	        a.__truediv____(b)
a % b     #addition	        a.__mod____(b)


# Note : __init__ is also a one of the dunder funtion in python which are prebuilt rules for defining or constructing something in python.


'''

'''
#Good Example of Inheritance with PolyMorphism In OOPs : Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenancecharge. So total fare for bus instance will become the final amount = totalfare + 10% of the total fare.

# Example:
# Vehicle Fare: 5000
# Bus Fare: 5500.0


Concept : class Vechicle:
                seating capacity #as attribute
                get_fare():
                    fare = seating_capacity * 100

        #another Derived class as 'Bus' from Parent Class- 
         class Bus:
         
            get_fare():
                #Updated Fare with 10%

                

'''

class Vehicle:
    # Bases On Seating Capacity Attribute we are going to calculate the fair -
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare_charge(self):
        fare_charge_vechicle = self.seating_capacity * 100
        return fare_charge_vechicle

# Creating the derived Class which inheriting the above parent class -
class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    # Updating the fair with Bus Maintaince Charge with previous charge -
    def fare_charge(self):
    
        # Final Charge of Bus with Vechicle Charge -
        vehicle_fare = super().fare_charge()
        maintance_fare = 0.1 * vehicle_fare # With maintance
        final_charge =  maintance_fare + vehicle_fare
        return final_charge

#Now creating a vechicle object with Provided 50 Seating capacity
vehicle1 = Vehicle(50) 
print("Vehical Fare : ", vehicle1.fare_charge())

#Now creating a bus object - (with same no of seating capacity)
bus1 = Bus(50)
print("Bus Fare : ", bus1.fare_charge())


# Note : In Case, when We work with Inheritance i.e Inherite Parent Class Into Child, then when we create Object from Child Class, then If we call attributes or methods from this created object, then It Firstly Look into Own Class(firstly into Instance Space then Moved to Class Space of Child) after if it do not found and inheritanc is applied then it starts looking same attribute and methods in the Parent Class. Thus, If a method with same name and we called method from child object then It get called from child Class rather PArent class.
# Looking Order of attribute or methods, if called from child class object -

# Child Class -----> Parent Class        



