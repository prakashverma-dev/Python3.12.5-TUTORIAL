

'''

Control Statements : They allow us to control the flow of our program. The Control statements are conditional statements, loops, and function calls.


#1)Conditional Statements : Based on some conditions(which might be True or False) in program, we need to take decision i.e used for 'Decision Making' in program, then we use conditional statements which are -

   a) if, if-else, if-elseif-else ladder
   b) nested if-else
   c) Ternary Operator
   d) switch/match statement

2) Loops : It is one more control Statemnets in python used to perform some repetative task again and again in the program. Example Print "Hello world" 10 Times using Loops.  

Python has two primitive loops:

    a) for loop 
    b) while loop

-------------------------------------------------------------

a) if statement : It is most basic decision-making statement where when 'if' condtions get True only then if-statements gets executed, otheriwise followd next line codes in the program will be followed, In case 'if' condition gets False.

Synax : if condition:
            # body of if statement

        #Normal Next Line Code    

Here, Condition evaluates based on comparison, logical and other operators and the we get Boolean Value always as True or False, and On the basis of this we decide to execute block or code or not for the same.

In Other words, Here, condition is a boolean expression, such as number > 5, that evaluates to either True or False.


b) if-else statement : It is most fundamental decision-making statement where 'If' some codition is met then we do something 'else' we do something. Means 

When 'if' condition gets true then only executes 'if' statements, otherwise 'else' statements will get executed in case of 'if' condition get false.


Ex: if raining === True : 
        print("take umbrella")
    else :
        print("don't take umberella)

Synatax : 

if condition :

    # statement1
else 

    #statement1

NOte : In Python, we must have to use collon(:) before starting of every block of codes or scopes to use python indentation, otherwise we wil get error and also In Python, It is optional or discouraged to use parenthesis i.e brackets() for wrapping conditions unlike some programming language. 


c) if-elif-...-else statement : In Python, we use elif syntax for else-if. if-elif-else statement is used for multi-way decision-making by checking multiple conditions sequentially from top-down and once any condition get TRue then executes that block of code and left the if-else-if entire hicharacy and move to next line code in program. and suppose there NO conditions get True then fashback statement i.e else condition get executed. 

Syntax : 

if condition1:
    # code block 1

elif condition2:
    # code block 2

elif condition3:
    # code block 3
 .
 .
else: 
    # code block 4


OR, 
if num > 2: print("woow1")
elif num <2 : print("wow2")
else: print("none")  

Note : If there is one statement as print then we can use in same line but when there are more than one statments in if-else block then we need to use in next line. It is not recommneded as syntax to use in pthon.



d) Nested If-else Statement : Nested if…else statement occurs when if…else structure is placed inside another if or else block. Nested If..else allows the execution of specific code blocks based on a series of conditional checks.

Syntax : 

#outer if statement
if condition1 :
    #inner if statement
        #Print
    
    #inner else statement
    else:
        #print

# outer else statement
else:
     #inner if statement
        #Print
    
    #inner else statement
    else:
        #print

# Python 'pass' Statement : At some certain situation in programm, if want our python compiler doesnot stop at some condition that might interrupt the code reading for compiler, we can just simple use 'pass' statement to pass the current line to the next line in the program.

Ex: whenever For if statement with no content i.e having an empty if statement, that would raise an error without the pass statement, like this -

a = 33
b = 200

if b > a:
  pass   #---> means telling Python Interpreter please while reading skip me and move to next line code in the program i.e passed from cuurrent line of code.
  
print("Code Further ie Next Line")



#Ternary Operator : It is one of the conditional statament used for simplifying if-else statement in one line i.e Short Hand syntax for writting if statement or if-else statement in one line.


Syntax : 

variable = <"value1" print> if <condition True> else <"value2" print>.

OR,

print("value1") if <condition_check>  else print("value2")

Here, when 'if' condition get True only then 'value1' get assigned to variable other if it gets False then 'value2' get assigned to variable.

Example : WAP to check number is ODD or Even using Ternary Operator -

num = int(input("Enter the number :"))

output = "Even Number" if num%2 == 0 else "Odd Number"
print("Output is :", output)

# OR,

print("Even Number") if num%2 ==0 else print("Odd Number")


#OR,  

num = int(input("Enter the number :"))
print("Output is :", "Even Number" if num%2 == 0 else "Odd Number" )


--------------------------------------------------------------------


#Python Match Case : It is one more conditional statement. It is use in place of using multiple if-elseif-else ladder Means Instead or altenative of writing many if..else statements, you can use the match statement for easy readability. Python match is similar like 'Switch' Case from other programming language. Here we dont need to break the each case statement, it comes in python inbuilt.


             -----Match 1--->   Statement1
Variable X   ------Match 2--->  statement2
             -----Match 3--->   statement3

Syntax :    

match expression/condition :
    case x:
        #Statement1
    case y:
        #Statement2
    case z:
        #Statement3
    .
    .
    case _ : 
        #DefaultStatement  

Here, We use 'match' keyword and 'case' keyword and underscore(_) character to work with match conditional statement.         


#How Match Statement works:


    a) The match expression is evaluated once means as soon as get matched from any cases from top to bottom, that case code get executed and come out of match statment and in fashback if there none case get matched then at the end default case get executed. Use underscore character(_) as default value to be matched. 
    
    b) Remember, Default case i.e with underscore must be the last case not any middle case. It is optional case we can use or skip default case in program.

    c) match case evaluate only once with either only one of the following 'cases', not with least more than one 'case'

    d) case and match keywords expect expression or value to be put, we cant leave anyone empty i.e if we skip or dont put value to 'case' then python gives an error.

    e) If there are two cases have same value or probable to match but as soon as The first case get macthed then that executes and come out of match statement and other case get ignored.

day = 13
match day:
  case 1:
    print("Monday")
  case 3:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")         
  case 7:
    print("Sunday")         
  case _ :
    print("Nothing Matched")       


Example : USing Match Cases, Build a basic calculator for by taking Integer two integer numbers from user and a operator from user, then match user entered operator with Match statement 'cases' and perform as per user actions - (Note: Devlop the project more with more number of operators entered by user) 

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))

operator = input("Enter the operator : ") # We get operator as String input  


match operator:
  case "+":
    print("Addition is :", num1 + num2)
  case "-":
    print("Substraction is : ", num1 - num2)
  case "*" :
    print("Multiplication is : ", num1 * num2)
  case "/":
    print ("Division is : ", num1/num2)  
  case _ :
    print ("Enter Only Basic Four Operators Only!")  
  


---------------------------------------------------------
#Python Indentation : Python Indentation is the whitespace (space or tab) before a block of code.

That whitespce as per programmer but must be minimum one space or fourspace(recommended for visibilty for prgrammers aslos consider as 1 Level indent) to define a block of code.


Indentation refers to the spaces at the beginning of a code line. But That code line must be block of code or defining scope for if-statement, for-loop, class etc. Otherwise if we use indentation i.e white space before any python code then we get type error in python. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

___print()  ---> if we leave a single space before any starting line python will give a error coz it is defined for identation for block of code or scope defining. 

# In Other programming lang, we uses curly braces to define a block of code or to define a scope, whereas in python we use indentation to define a block of code or scope; such as the scope of loops, functions and classes . For Defining indentation for a block of code, it must be at same level else compiler will throw an error.

Example : 

#Other Programming Languages :-

if(condition){

    curly braces : to specify block of codes for other langues
}

#In Python -

if(condtion):    

_____print() --> indentation use to sepecify block of code in python
which must be at same level.

     print()
                        
else:
    print()    
    print()    

    
Example2:

for x in sequence:
    # indent by four spaces = 1 level
    if condition:
            # Indent by eight spaces for this block
            print("a big indent here")
    else:
      # Indent by only two spaces for this block
      print("a smaller indent")
    print("outdent back to four spaces")

# Each block must be indented by one level relative to the previous block.

As far as where you need to indent, you have to memorise the rules:

a) The statement is followed by a colon “:” which helps you recognise that it needs a new block or requires the block to be indented.
b) The relevent statements followd by : class, def, if, elif and else, for and while
try, except and finally
with


------------------------------------------------------------






'''


# if-else -

# Q1 : Take integer input and tell if it is positive number or negative -

num = int(input("Enter the number : "))
if num >= 0 :
    print(f'{num} is positive')
else :
    print(f"{num} is negative")  

# Note : In Conditional Statement, We first check the top most neccessary condition firstly in the 'if-block' then followd by least important conditions in the 'if-else-if-block and lastly the least or fashback statement in the last of condition statements.     

#Q2 : Take positive integer input and tell if it is even or odd -

#Divisble by 2(remainder ==0) ---> Even and Not Divisible by 2(remainder != 0) ---> Odd

num = int(input("Enter the number : ")) 

if num % 2 == 0 : 
    print(f"{num} is Even Number")
else :
    print(f"{num} is Odd Number")

 
 #if-elif-else -


#Q3 : If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss or no profit no loss. Also determine how much profit he made or loss he incurred. 

#Notes : CP(Cost Price) : Kharid Price; and SP (Selling Price) : Jis Price Par Bechaa;  

# Example : CP = 5 amd SP = 8
# If SP > CP --> Seller Made Profit  --> Profit Calculate = SP - CP

# ANd, CP = 5 and SP = 2
# IF SP < CP ---> Seller In LOss ---> Loss Price Calculate = CP - SP

# ANd, CP = 5 and SP = 5
# IF SP = CP ---> Seller neither LOSS or PRofit ---> Thus Net Profit/Loss = CP - SP or SP - CP = 0

cp = float(input("Enter Cost Price : "))
sp = float(input("Enter Sellin Price : "))
profit_or_loss = sp - cp 
# print(profit_or_loss)

if(profit_or_loss>0):
    print("Seller Got Profit, The Profit Price is :", abs( profit_or_loss) )
elif (profit_or_loss < 0):
    print("Seller Got Loss, The Loss Price is : ", abs(profit_or_loss))

else:
    print("Seller Has Got Neither Profit or Loss, The Profit/Loss Price is : ", abs(profit_or_loss))


#Other -

cost_price = float(input("Enter COst Price :"))
selling_price = float(input("Enter selling Price :"))

#If sp is more than CP --> Profit
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("We have made profit of :", profit)
#If SP is less than CP ---> Loss    
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("We have incurred loss of :", loss)
#IF SP is equal to CP ---> Neither Profit nor Loss   
else: 
    profit_or_Loss = selling_price - cost_price
    print ("We have made no profit no loss of : ", profit_or_Loss)
# Note :  Remember, Alwasy take the reference of 'Selling Price(SP)' with Other Cost while solving Profit and Loss Problems.     

 
# elif multiple times : when we use when we have the multiple conditions.

#  Q4 : Take input percentage of a student and print the Grade according to marks as follows -

#  81 - 100  --->  Very Good  
#  61 - 80  --->  Good
#  41 - 60  ---> Average
#    <=40  ---> Fail

#NOte while using if-elif-else statement, we first start with checking the upper most condition i.e upper boundery condition then slowy we enter lower and last we ends with lower least condition i.e lower boundary condition. 
# 
# [0 100]Marks ---> Here Upper Most COndition is 100Marks and Lower Least Condition is 0 Marks.

marks = int(input("Enter Student Marks : "))

if marks > 80 :
    print("Very Good")
elif marks > 60 :
    print ("Good")    
elif marks > 40:
    print ("Average")    
else:
    print("Fail")    

#Solving Multiple Conditions Problem using 'and' and 'or' : Which are Logical operators that help us in combining the result of 2 conditions.

'''  

Cond1           Cond2
 T                 T    ----> We use 'and' operator if want both conditions get True.
 
 F                 T  ----> We use 'or' operator if want either any conditions gets True.
 T                 F



 F                 F  

 Example : Ria have got marks in english and math so we need to print Grades as per marks in both subjects -

 english_marks > 80 'and' math_marks > 80 ---> States If both True then only Print 'Grade A'

 english_marks > 80  'or'  math_marks > 80 ---> States If any one gets True then Print 'Grade B'

 And Lastly IF we both get False we add into the else Block to Print 'Grade C'



'''


eng_marks = int(input("Enter English Marks : "))
math_marks = int(input("Enter Math Marks : "))

#If both are more than 80, Print A Grade -
if eng_marks > 80 and math_marks > 80:
    print ("Grade A")
#If either of marks are more than 80, Print B Grade -
elif eng_marks > 80 or math_marks > 80:
    print ("Grade B")
#If neither of marks are more than 80 -    
else : 
    print ("Grade C")     

# Note :  First We check the most priorer condition first then least priorer like both subject must have above 80 have more prioer than any on of the subject have either above marks 80 and lastly neither of subject have marks above 80 at last priorer.


# Q. Take Posituv integer input and tell if is a four digit number or not -
'''
#Concept : 

One Digit Number Lies ---> 0 to 9 
Two Digit Number Lies ---> 10 to 99 
Three Digit Number Lies ---> 100 to 999 
Four Digit Number Lies ---> 1000 to 9999 ---> 10 <=  [XXXX]  <= 9999 --Both of the condition must be TRUE ---> We use 'and' Operator


'''

num = int(input("Enter the Number :"))
if num >= 1000 and num <= 9999 :
    print(f"{num} is Four A Digit Number")
else:
    print (f"{num} is Not A Four Digit Number")  



#Q : Take 3 Positive integers input and print the greatest of them.
'''
#COncept :  
 n1 > n2   and   n1 > n3  ----> Means n1 is greatest from n2 and n3
 n2 > n1   and   n2 > n3  ----> Means n2 is greatest from n1 and n3
 n3 > n1   and   n3 > n2  ----> Means n3 is greatest from n1 and n2


'''

n1 = int(input("Enter number1 :"))
n2 = int(input("Enter number2 :"))
n3 = int(input("Enter number3 :"))

#Checking n1 is greatest -
if n1 > n2 and n1 > n3 :
    print(n1,"is the greates number")

#Checking n2 is greatest -
elif n2 > n1 and n2 > n3 :
    print(n2,"is the greates number")

#Checking n3 is greatest -
else:
    print(n3,"is the greates number")

# OR, 

n1 = int(input("Enter number1 :"))
n2 = int(input("Enter number2 :"))
n3 = int(input("Enter number3 :"))

# Checking n1 is greatest than other two -
if n1 > n2 and n1 > n3:
    print(n1, "is the greates number")

# If above condition get false, that means n1 is not greatest either n2 or n3, lets compare betweeen n2 and n3 -
elif n2 > n3:
    print(n2, "is the greates number")

# Checking n3 is greatest -
else:
    print(n3, "is the greates number")


# OR,  Using Nested If-else block inside another if-else inside -    

n1 = int(input("Enter number1 :"))
n2 = int(input("Enter number2 :"))
n3 = int(input("Enter number3 :"))
#comparing n1 and n2 -
if n1 > n2:
    #either n1 or n3 is greatest, checking -
    if n1 > n3:
         print(n1," is Greatest")
    else:
        print(n3, "is Greatest")    

else:
    #either n2 or n3 is greates, checking -
    if n2 > n3:
        print(n2, " is greatest")
    else:
        print(n3,"is greatest")    

# Q : Take positive integer input and tell if it is divisble by 5 or 3 but not divisible by 15

# Ex: 18 ---> Divisble by 3 but Not Divisible by 15
# Ex: 10 ---> Divisble by 5 but Not Divisible by 15


num = int(input("Enter Positive integer number :"))

#Checking whether It is divisible by 15 or not -
if num % 15 == 0 :
    print("Divisible by 15")
else :
    #checking divisble by either 3 or 5
    if num % 3 == 0 or num % 5 == 0 :    
        print("Divisible By Either 3 or 5 But Not By 15")
    else: 
        print("Neither Divisible 3 or 5 or 15")    

