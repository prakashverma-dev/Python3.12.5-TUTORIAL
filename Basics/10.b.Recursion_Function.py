'''

# Recursion Function : When a function calls itself repeatedly, to solve a specific task in multiple parts for whole problem.

Recursive function acts like something we do in loops, In Other words, Recursive function fullfill the requirement of any loops.

We can relate Recusion function end task as Loop.

Note : All loops problem can be solved vai using Recursion and same way all Recursive problems can also ve solved via using Loops. Hence, We use both according to uses and which makes problem more simplicity to get solved.

Note : Recursive function calls again and again own function untill we do not provide any base recursive condition where to stop the recursive function.

"Base case of Recursion ----> Same as Loop stoping condition" where to stop loops or recursive function, else it will hang out system i.e Recursive function will run infinite like loop, hence memory get occupies at one point and code get crashed.

RecursionError: maximum recursion depth exceeded

Note : In short, Recursion is nothing but Loops other varient who is little tricky but solves problems efficiently. Recursion function is far away cousing of loop and reading his personality is little diffcult but not hard.






'''

# 1. Print a Number in reverse direction till 1 i.e Show number from 'n' number to till 1. 

#  5 --> (5-1) ---> (5-2) ---> (5-3) ....  ---> 1
#  n ---> (n-1) ---> (n-2) ---> (n-3)  .... ---> 1 

def showNums(n):

    if n == 0:
        print("Inner Recursive function ended here!")
        return
    
    print(n) # apne kaam ko recursive function ke uppar likhte hai so it get executed before going into call stack.

    showNums(n-1)

    # After this all statments will executes one by one once call stack function starts removing off when the recursive function loop stops.

    print(n) # I want to print 5 4 3 2 1 # This will print after the call stack starts ending one by one.
    print(f"{n}. Hello baby")

showNums(3)    


# 2. Factorial of a 'n' -

# n! = n * (n-1)!

# Note : (n-1) ! = (n-1) * (n-2) * (n-3) *..... * 3 * 2 * 1 

def factorial(n):

    if n == 0:
        print("Inner Recursive function ended here!")
        return 1
    
    result = n * factorial(n-1)
    return result

print(factorial(3))
print(factorial(5))
print(factorial(6))


# 3. Print "Hello World 11 times" -

# Using for loop -
for i in range(1, 12):
    print(f'{i}. Hello World')

# using recursive function to fullfill same task of printing "Hello World" 11 times-

print("-------------Using Recursion ---------")

def showHelloWorld(times):

     if times == 0 :
         print("Inner Recursive function ended here!")
         return

     print(f"{times}. Hello World")

     showHelloWorld(times - 1)
     
showHelloWorld(5)


# Problems : -

# 1. Write a Recursive function to calculate the sum of first n natural numbers.
#  sum of n = n + (n-1) + (n-2) + (n-3) + ..... 1. 

def sumofn(n):

    if n == 0:

        print("Inner Recursive function ended here!")
        return 0 # when returing for sum last base case value can return 0 so it will add zero (For Multiplication must return 1 as base value for multiplication)
    
    sum = n + sumofn(n-1)
    return sum

print(sumofn(5)) # sum of till 5th number
print(sumofn(10)) # sum of till 5th number

# 2. Write a Recursive function to print all elements in a list.
# (Hint : use list and index as paramerters; base case : index == len(list) )

# using loops -
mylist = ["Mango", "Banana", "Graves"]

for item in mylist:
    print(item)

# using Recursive function- index : 0, 0+1, 1+2... 0, 1, 
def displayItems(mylist, index=0): # Start index from 0 by  default.

    if index == len(mylist): # base case if index reaches length of list, stops.
        return
    
    print(mylist[index]) # Print current item.
    displayItems(mylist, index + 1) # Recursive call for next element.

displayItems(mylist)    










    




