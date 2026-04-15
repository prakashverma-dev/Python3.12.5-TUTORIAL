

'''

#1) Classic Function : -

# Sum of two number -
def sum(a,b):
    return a + b

print(sum(5,6))


#2) Lambda Function / Anonymous Function / Function Expression : - n Python, an anonymous function means that a function is without a name. Use 'lambda' keyword to create a anonymous functions or Lamba Function or Function Express and followed by number of arguments seperated with comma and followed by semicon then return the single exprssion in same line must without 'return' keyword and lambda function returns a value we store into a variable to be called later.


# Syntax: lambda arg1, arg2, arg3, ... : <expression_to_be_returned>

'''

# To sum two number -
def sum2(a, b): return a+b
print(sum2(4, 2))

# To sum three number -
def sum3(a, b, c): return a+b+c
print(sum3(5, 3, 4))

# Note : Check other use-case of lambda function with map() and filter() method in basic python series notes.


# 3) Recursion Functions : Recursion function means "It is a process for calling a function again and again untill a specific condition met."

# a normal function to print "Hi"
def pond():
    return "Hi"


print(pond())


'''

# Recursion Function : Recursive function calls itself repeatedly over and over again untill base case condition doest not stop it calling, to solve a bigger problem in parts wise. for the whole problem.

Recursive function acts like something we do in loops, In Other words, Recursive function fullfill the requirement of any loops.

Note : All loops problem can be solved vai using Recursion and same way all Recursive problems can also ve solved via using Loops. Hence, We use both according to uses and which makes problem more simplicity to get solved.

Note : Recursive function calls again and again own function untill we do not provide any base recursive condition where to stop the recursive function.

# Recursive function must have two parts "Base Case" and "Recursive Case" : -

Base Case : Stopping COnditon of Recrusive Function.
Recursive Case : The logic where function calling itself to solve the problme in subproblem or in reapeated times untill base case doesnot stop it.

"Base case of Recursion ----> Same as Loop stoping condition" where to stop loops or recursive function, else it will hang out system i.e Recursive function will run infinite like loop, hence memory get occupies at one point and code get crashed.
RecursionError: maximum recursion depth exceeded

Note : In short, Recursion is nothing but Loops other varient who is little tricky but solves problems efficiently. Recursion function is far away cousing of loop and reading his personality is little diffcult but not hard.

Note : Recursive function must take some argument which can work as stoping the recursive function.

'''

# Let's see Recursion - Print "Pond" 5 times with user 'n' input -


def pond(n):

    if n == 0:
        return

    print(f"{n}.Pond")  # 5-->4-->3-->2-->1 

    pond(n-1) 

    print(f"Ram") 

    # print(f"{n}.Pond")  # 5-->4-->3-->2-->1 


        # Note : Here if we dont specify the base Recursive conditon then the function will be called infine time and the function stack will be filled, will known as "Stack Over-flow" and program will be crashed.


print(pond(5))
