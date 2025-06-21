
#Number or Numeric Datatypes : There are three numeric types in Python:

# int  -  Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# float  -  Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# complex - Complex numbers are written with a "j" as the imaginary part:

# x = 3+5j
# y = 5j
# z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function:

# Example
print(type(x))
print(type(y))
print(type(z))




# ---------------------------------------------------------------------------


'''
#Operators In Python : Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

print(10 + 5)

Note : We use plus(+) operator also for concatination of two similar datatype if present, like string concatinate i.e two join two strigs, two number concatinate means two number get added, similartly so on. In two or more same datatype is not present, then python interpeter will throw an typeError.

#Python divides the operators in the following categories:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

 
#Arthemetic Operators : - Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	    Example	
+	Addition	        n1 + n2
-	Subtraction	    	n1 - n2
*	Multiplication	    n1 * n2
/	Division	    	n1 / n2(Always returns the float value means in decimal)

//	Floor division	    n1 // n2(Get the nearest Floor Value of Fraction, always a integer value(-ve or +ve, 0) e.g:4/3 = 1.333 --> 1(Floor Value) Or, -1.333= -2  )
%	Modulus         	n1 % n2	  --> To get remainder of divison
**	Exponentiation	    n1 ** n2 --> n1^n2 

#Example : 
print("Sum :",2+3)
print("Difference :",2+3)
print("Product : ",4*3)
print("Divison : ",4/3)
print("Floor Divison : ",4//3)
print("Modulus : ",4%3)
print("Exponentiation : ", 4**3)
print(4/3)   #1.333
print(4//3)  # 1
print(-4//3) # -2


#Assignment Operator : - There are many assignment operator, It purpose is to assign value or variable to a new variable i.e put RHS value/variable into LHS variable. One Most USed, assignment operator is '=' (equal to) and there are other assignmet operators as well -



Operator	        Example
=	                n1 = 2
                    n2 = n1 # n2 = 2 now
+=	                n2 += n1 --->  n2 = n2 + n1
-=	                n2 -= n1 --->  n2 = n2 - n1
*=	                n2 *= n1 --->  n2 = n2 * n1
/=	                n2 /= n1 --->  n2 = n2 / n1
//=	                n2 //= n1 --->  n2 = n2 // n1
%=	                n2 %= n1 --->  n2 = n2 % n1
**=	                n2 **= n1 --->  n2 = n2 ** n1

&=	                n2 &= n1 --->  n2 = n2 & n1
|=	                n2 |= n1 --->  n2 = n2 | n1
^=	                n2 **= n1 --->  n2 = n2 ** n1
>>=	                n2 **= n1 --->  n2 = n2 ** n1
<<=	                n2 **= n1 --->  n2 = n2 ** n1
print(n2 := n1)	     n2 = n1 
                     print(n2)	

Here, In these operators, operation works from left to right operators e.g += means First add LHS value with RHS value and then assign resultant into LHS.

# Example : 
n1=5
n2=n1
print(n1, n2) #5 5
n2 += n1  # n2 = n2+n1
print(n1, n2) #5 10

print(x:=3) #Means First Assign x= 3 then print(x)




#Comparison Operators : Comparison operators are used to compare two values. COmparison operator evaluated output value is either True or False i,e Boolean Value.

Operator	Name	Example	Try it
==	Equal	         n1 == n2	
!=	Not equal       	n1 !=  n2	
>	Greater than	   n1 > n2	
<	Less than	        n1 < n2	
>=	Greater than or equal to	  n1 >= n2	
<=	Less than or equal to	   n1 <= n2                     


#Example : -
n1,n2 = 4,3
print(n1 == n2) # False
print(n1 != n2) # True
print(n1 > n2) # True
print(n1 >= n2) # True


# Logical Operators : It works upon the boolean values like True and False.
Logical operators are used to combine conditional statements, and works on the evaluation of two or more python expression together.

a) and operator : Returns True if both statements are true and In all other cases it will return false.

Ex: True and False   ---> False (only if both expression are TRue then and returns True else False in all other cases.)
 False and False   ---> False
 True and True  ---> True
 False and True   ---> False

 (1>0) and (3<2)  ---> True and False  ---> False
	
b) or Operator : Returns True if any one of the statements is true and False only get if both the operants will be False.

False or False ---> False
True or False ---> True
True or True ---> True
False or True ---> True

 (1>0) and (3<2)  ---> True and False  ---> True

c) not Operator :  It Reverse the result, returns False if the result is true.	

not (1>0)  --> not True ---> False


#Chart For and, or, not Operator : -


            and      or       
T   F        F        T
F   T        F        T
T   T        T        T
F   F        F        F

Note : For 'or' operator only one True can lead to True else False and For 'and' operator when Both operantes leads to True then only True else False.

Example : -

exp1 = 2 > 1  #True
exp2 = 5 < 4  #False

print(exp1 and exp2)  #False
print(exp1 or exp2)   #True
print( not exp1)   #False


#Indentity Operators : Whenever we need to check two varibles are same object or not, then we use identify operators (is or is not) instead of using comparison operator i.e == or != for just value comparsion checking.
# 
#  It is use to check the objects that they are equal or not means but if they are actually the same object, with the same memory location or different momory location.

Unlike Comparison Operator ==   checks the values that are equal or not e.g

x = 5
y = 5
x == y  #It just check the variable values.

Operator	                Description	                        Example
is     --->	Returns True if both variables are the same object	--> x is y	
is not -->	Returns True if both variables are not the same object	--> x is not y

#Example : -

x = 5
y = 5
print(x is y)  #True coz here holds in same object with same memory location.
print(x is not y) #False 




#Membership Operators : - Whenever we working with any sequence datatypes(list, tuple, set) then we use membership operator(in or not in) to know that any object is present in that sequence or not.
 
Operator	        Description	            Example
in   --> 	Returns True if a sequence with the specified value is present in the object           --->  	x in y	
not in  --> 	Returns True if a sequence with the specified value is not present in the object   --->	  x not in y


#Example
fruits = ["apple", "banana","cherry"]
print("banana" in fruits)  #True
print("mango" not in fruits)  #True



# BitWise Operators : - Bitwise operators are used to compare binary numbers 1 or 0.

0 or 1 are known as Bits in computer languages which is ---> 'Binary Number System'

0 or 1     ---> Binary Number System
0 to 9     ---> Decimal Number System

#Decimal No System ---Convert to --> Binary no system

Ex: 3 ---> 11

Decimal           Binary
0                   0
1                   1
2                   10
3                   11
5                   101
9                   1001
14                   1110

#binary No system to Decimal No System Conversion -





#Example : -




'''


#Bitwise operator Example : -

a = 5
b = 3
print("a AND b ", a & b)
print("a OR b ", a | b)
print("a XOR b ", a ^ b)
print(" NOT b ", ~b)



# 'Operator' Precedence In Progamming Language : In a programming langauges, if in an expression if there are multiple operators then which one gonnna perform/evaluate first will be decided by the 'Operator Precedence'.

# In Math we follow BODMAS RUle, The order to perform top to down -

# B  - Bracket i.e (), {}, []
# O  - Order i.e Power/Indices  --> of(*), power, roots like square, square_root 
# DM - Division and Multiplication (Comes at same priority)
# AS - Addition and Substraction (Comes at same priority)

''' Ex1 :  2+ 3 * 4 --> 2 + 12 = 13 
    Ex2 :  (2+ 3) * 4 --> 5 * 4 = 20
    Ex2 :  5 + (2*3)^2 --> 5 + 6^2 = 5 + 36 = 41
    Ex2 :  1/2 of 8 --> 1/2 * 8 = 4
    Ex2 :  3 + 1/2 of 10 --> 3 + 5 = 8

        '''

# Note : In case of same priority operators, whichever comes first means which we see first we evaluate that is obvisouly we see from left to right. Thus, Whichever comes first from left to right in expression we evaluate first.

''' Ex1 :  10 - 4 + 2 ---> Thus, Here - and + have same precedence, then calculated from Left to right whichever comes first.

        = 6 + 2 = 8  (Correct)
 
    Not, = 10 - 6 = 4 (Incorrect) 

    Ex2 :  8 * 6 / 4  ---> Here, * and / Have same precedence level, so we see L to R.

        =  48 /4 = 12
    If, we do divi sion first -
        = 8 * 1.5 = 12 (Same Answer)

    Ex3 : 6  * 4 / 2 = 24 /2 = 12 (Followd L to R coz * and / have same precedece)

    OR, IF we do divison first, 6 * 2 = 12 (Same Answer)

    Ex4 : 20 / 5 * 2 ---Follwing L to  R as same precedence  = 4 * 2 = 8

    If we Do multiplication first -
    20 /10 = 2 (WRONG - INCORRECT)

    Thus, Whenever we face the same precedence or same priority level of opertors we just simply follow L to R order to solve the problem.


    

        '''

# Note : In case of more than one brackets used in one expression then solve brackets from InnerMost to OuterMost means andar se bahar.here, Order of any brackte doesnot matter which is in inner that brackte will evaluate first then lastly outer most bracket. Ex :  {10 + [6 * (2+1)]}  --> {10 + [6*3]} --> 28

# 'Operator' Precedence In Python : As we also follow the mathemactical BODMAS rule for Operaror Precedence but In python we have more operators like **, // etc. except math basic operators.

# Thus, Their precedence order given below, starting with highest precedence and ends with lowest predence -


'''
    ()     --> 	Parentheses  
    **     -->  Exponentiation
    * , / , // , %   --->	Multiplication, division, floor division, and modulus   

    + , -	  --->   Addition and subtraction   


    << , >>	 --->  Bitwise left and right shifts

    &, ^, |    --->  Bitwise AND, XOR, OR

    ==  !=  >  >=  <  <=  is  , is not,  in , not in  ---> 	Comparisons, identity, and membership operators


    and , or, not   ---> LOGICAL Operators And, OR, Not


    Note : Here, At the same level, if there are more than one operators then shows have the same precedence order. THis in case we evaluate from left to right as per what we see first. In Other word, If two operators have the same precedence, the expression is evaluated from left to right.

    #  Example:

3 + 2**4/2*5 - 8//2

= 3 + 16/2*5 - 8//2
= 3 +  8*5 - 8 //2
= 3 + 40 - 4
39






'''


