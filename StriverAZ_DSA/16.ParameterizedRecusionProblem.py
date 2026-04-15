# Basic Recursion Problems : - We can solve Recursion Problem, with two ways -

# a) Parameterized Way : Passing Parameter to function to repeat the loop.
# b) Functional Way : Function itself returns function

# 1. Print Name 5-times /Print your name n-times
# 2. Print linearly from 1 to N
# 3. Print from N to 1
# 4. print linearly from 1 to N(But by Backtrack)
# 5. print from N to 1(But by Backtrack)

# Solving all these with Parameterized ways : -

# 1. Print Name N-times using Recursion - 
def displayName(i, n):

    # base case
    if i > n:
        return

    # else part  -
    print("Prakash")
    displayName(i+1, n) 


# (1,3)  --> (2,3) --> (3,3) --> (4, 3) gets True i.e i > n and Inner Function get terminated.
displayName(1, 3) # Name gets Printed Thrice; here user input is 3.



# Time Complexity : O(N) calling N function
# Space Complexity : also, O(N) coz computer internal memory uses for call stack storing functions.



# 2. Print linearly from 1 to N - /1 to 4
def display1toN(i,n):
    if i > n:
        return
    
    # task
    print(i)
    display1toN(i+1, n)

display1toN(1,4) # 1,2,3,4 Printed from 1 to 4; here user input is 4




# 3. print from N to 1(rever looping) - # Print 4,3,2,1
def displayNto1(i,n):

    if i < n:
        return
    
    # Task -
    print(i)
    displayNto1(i-1, n)

# (4,1) -> (3,1) ->(2,1)-> (1,1) -> (0,1)
displayNto1(4, 1) # from 4 to 1; here 4 is user input. 

# 4. Print from 1 to N using BackTracking :-

# BackTracking Means : It is a way to solve Recursion Problem in backtracking way means calling the task after the recursive function call and starts printing the output from the last inner function, comming out one after another from callstack in linear fasion reverse.

def print1toNBackTrack(i, n):

    if i > n:
        return
    
    print(i)
    print1toNBackTrack()

