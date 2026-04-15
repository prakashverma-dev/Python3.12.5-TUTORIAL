
# Recursive Functional Way : We iterate the logic within function argument for recursive function iteration to full-fill the task.

# In Function way we return something each iteration recursive time.

count = 0
def hello1():

    
    global count
     # look for count variable in global/that is make count variable global.
    if count == 3:
        return
    
    # Else Part 
    print(count) # 0, 1, 2
    count += 1 
    
    hello1() # Function called itself
    
   

# hello1() # Main funtion called.

'''
#1. Print 1 to N or N to 1 using Functional Recursive Way : -

BackTracking : when we perform some operation after the function call

# In Function way we return something each iteration recursive time.



'''
def f(n):

    if n == 0:
        return 0   
    
    print(n) # 5, 4, 3, 2, 1   # this is not backtracking displaying value.
    return f(n-1) 
   

f(5)

def f(n):

    if n == 0:
        return 0   
    
    f(n-1) 
    print(n) # 1, 2, 3, 4, 5   # this is backtracking displaying value from last stored callstack.

f(5)


'''

#2. Sum of first n-natural number -
# n = means 1 se lekar n tak ka sum / means first we need to print 1 to till n -


# n = 3 = 3 + f(2 )
# f(2) = 2 + f(1)
# f(1) = 1 + f(0)
we know, f(0) = 0

Here, f(n) --> function of sum of first n-nos.
Thus, sum(n) = n + sum(n-1)

Problem is broken down into smaller parts.


'''
def sumtill(n):

    if n == 1:
        return 1
    # if n == 0:
    #     return 0
    
    return n + sumtill(n-1) # added 'n' here coz previous return value must get added to latest one. and finally it will return the final sum added value to last outer function.
    
print(sumtill(5)) # Recursion function last outer recursive function returned the value we need to print to diplay.




# Normal Way -
def sumtillNormal(n):
    sum = 0
    #  Print 1 to n and add all of them -
    for num in range(1, n+1):
         sum += num
    
    return sum

print(sumtillNormal(5))




''' 

#3. Factorial of n - Multiplication of numbers form 1 to till n -
Ex: 
n = 4 = 4 * 3 * 2 * 1  = 24
n = 3 = 3 * 2 * 1  = 6 = n * n-1 * n-2 * n-3 * ... 1

Formula : f(n) = n * (n-1)!

 fact(n) = n * fact(n-1)
'''



def fact(n):

    if n == 0 : # 0! = 1
        return 1
    
    return n * fact(n-1)

print(fact(4)) 
print(fact(3)) 


# Using Normal way -
def factNormal(n):
    fact = 1
    # Multiplcation of 1 to till n -
    for num in range(1,n+1):
        fact = fact*num
    
    return fact

print(factNormal(4))  
print(factNormal(3))  


# Time Complexity : O(N) ; for n number --> N calls
# Space Complexity : O(N) call-stack awaits ..awaits


'''
# Note Summary :-

i. For Natural number 1 to N : display1toN() = display1toN(n-1)
ii. For sum till to n-number :  sum() = n + sum(n-1)
iii. For Multiplication/Factorial till to n-number :  fact() = n * fact(n-1)

'''


