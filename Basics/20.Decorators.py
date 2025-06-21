
# Uses of Decorators in Python OOPs : -

# i) @staticmethod decorator : To make any method static which works something like where we do not need to access any object attributes or change instance attribute coz we do not specify self paramter in it.

# DrawBack of static Method : static method canot access or modify class state and generally for uses for utility.

# ii) @classmethod decorator : A class method is bound to the class & receives the class as an implicit first argument. Here, we use @classmethod decorator to convert normal method to classMethod only by passing 'cls' paramter where we can access and modify any class attributes. 
'''
# Syntax: 

    @classmethod         #decorator
    def college( cls):
            pass

'''

# iii) @property decorator : We use @property decorator on any method in the class to use the method as a property. We use @property decorator when we want to convert any instance attribute into function for better work related to that instance attribute.
# 
# Example:


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    def get_percentage(self):
        perc = (self.phy + self.chem + self.math)/300 * 100
        return str(perc) + "%"   


stud1 = Student(80, 70, 85)
print(stud1.get_percentage()) 

# Suppose, Examiner bymistake in chem given 70 marks wrongly, which is 80, so  he will update it i.e modify student1 chemisty marks -
print(stud1.chem) # Ealier --> 70
stud1.chem = 80
print(stud1.get_percentage())


# More about decorators :-
# iv) @getter decorator
# v) @setter decorator




