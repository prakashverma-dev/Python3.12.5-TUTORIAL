

'''
# MCQ1 : What is the purpose of the "init" method in a class in Python?

a. It is used to define private methods within a class. (by __<name_variable/method)
b. It is automatically called when an object is created and allows you to
initialize its attributes. (CORRECT)
c. It is used to define class variables that are accessible by all instances of
the class.
d. It is used to define the inheritance hierarchy between classes.



MCQ2: What is the concept in OOP that allows a class to inherit attributes and
methods from another class?
a. Polymorphism
b. Encapsulation
c. Abstraction
d. Inheritance (CORRECT)


MCQ3 : Which of the following statements about abstract classes in Python is
true?
a. An abstract class cannot have any methods.
b. An abstract class can be instantiated to create objects.
c. An abstract class can be inherited but cannot be subclassed.
d. An abstract class may contain abstract methods, which must be
implemented by its concrete subclasses.  (CORRECT)


MCQ4 : What is the purpose of the "super()" function in Python when working
with inheritance?
a. It calls the constructor of the base class. (CORRECT)
b. It allows the child class to override the methods of the base class.
c. It initializes the private attributes of the child class.
d. It is used to create a new instance of the child class.



'''

# Pratice Questions : -

# Q1. Create Account class with 2 attributes - balance & account no. and then Create methods for debit(-ve), credit(+ve) & printing the balance. then create objects for multiple bank account holder with these implemented features for each user who can add balance/credit, credit balance and if wants anytime get the bank statment balance amount.

class Account:

    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    #Get Net Balance of user - 
    def get_balance(self):
        return f'Your Bank Balnce is : {self.balance}'

    #Credit method to mange balance credit -
    def credit(self, credit_amount):
        self.balance += credit_amount
        return f"Rs.{credit_amount}/- was credited In Account No : {self.account_no}, Net Balance = {self.balance} "
    
    # Debit method to manage balance debit -
    def debit(self, debit_amount):
        self.balance -= debit_amount 
        return f"Rs.{debit_amount}/- was debited From Account No : {self.account_no}, Net Balance = {self.balance}"

# Now Lets create bank account for users/customers -
acc1 = Account(2000, 4300020023 ) # Firstly We added some money to customer1 bank account with his account no.
acc2 = Account(3000, 4300459830 ) # Added Balance to second customer2 with his bank account no.

# Let's check balance and account_no for user1 and user2 -
print(acc1.account_no)
print(acc2.account_no)

print(acc1.balance)
print(acc2.balance)

# Now, Lets Do some Debit and Credit and Final Balance Amount check with user1 account -

# want to add 700 rupees to acc1 -
print(acc1.credit(700)) 

# Want to take/debit 200 from acc1 -
print(acc1.debit(200))

# Now, Suppose at start of month salary credited 40,000/- 
print(acc1.credit(40000))

print(acc1.debit(10000)) # now paying rent 10,000 etc.


# Note : THis is good starter Project for relating OOPs with real-time problem solving using class and objects which solve real-world problem effectively. Rather using other datatypes like list,dict for storing account, balance etc.




# Q2 :  Define a Circle class to create a circle with radius 'r' using the constructor. then 
# Define an Area() method of the class which calculates the area of the circle.(pi * r^2)
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.(2 * pi * r)

import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    # To get Area of circle -
    def get_area(self):

        area = math.pi * (self.radius) ** 2
        return f"Area of Circle is : {round(area, 2)}"
    
    # To get Perimeter of circle -
    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return f"Perimeter of Circle is : {round(perimeter, 2)} "


# Lets create circle object from Circle class -
c1 = Circle(21)

print(c1.radius)
print(c1.get_area())
print(c1.get_perimeter())





#Q3(Inheritance and Polymorphism) : Define an Employee class with attributes role, department & salary. This class also has showDetails( ) method.
# Create an Engineer class that inherits properties from Employee & has additional attributes - name & age.

class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role = ", self.role)    
        print("Department = ", self.dept)    
        print("Salary = ", self.salary)    

#Lets create the employee objects -
emp1 = Employee("Developer","IT", "45,000" ) 
emp1.showDetails() # To get all details about the employee

# Now, Lets Create another subClass -
class Engineer(Employee):
    
    def __init__(self, role, dept, salary, name, age): # addition attributes name age except the Parent Class Employee Attributes.
        super().__init__(role, dept, salary)
        self.name = name
        self.age = age

    def showDetails(self):
        super().showDetails()  
        print("name = ", self.name) 
        print("age = ", self.age) 

# Lets create Engineer object -
engineer1 =  Engineer("Developer","IT", "85,000", "Prakash", 24)
engineer1.showDetails()
# print(engineer1.name)
# print(engineer1.age)





# Q4(Poymorphism - Operator Overloading Implementation) : Create a class called Order which stores item & its price.
# Use Dunder function _ _gt_ _ to convey that : orderl > order2 if price of orderl > price of order2.

# Note : We use Python inbuilt Dunder functions to implement Own Defined Operator Overloading like if we implete class using plus dunder function then it works as per user input. Similary way In this question, we need to use __gt__() dunder function which is analgous to greater than(>) operator in python. It will use to implete the class greater than function as per price of Order Objects.

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    #Let's Add a Dunder function __gt__(greater than) to check if object Order Price Greater than Second Order Price or Not -
    def __gt__(self, user_Order2):
        return self.price > user_Order2.price

# Lets' take Order from Order Class Order Class, with specifying Item and Price of the item -

order1 = Order("Biscuit", 48) 
order2 = Order("Chips", 15) 
print(order1.item)
print(order1.price)

print(order2.item)
print(order2.price)

# Let' check True which Order PRice is greater and gets True or False -
print(order1 > order2) # True ---> Means Price of Order1 > Price of Order2 

