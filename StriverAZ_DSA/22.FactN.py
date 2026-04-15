'''   

Factorial of a given number

You are given an integer n. Return the value of n! or n factorial.


Factorial of a number is the product of all positive integers less than or equal to that number.


Example 1

Input: n = 2

Output: 2

Explanation: 2! = 1 * 2 = 2.




'''


'''
#1. Approch1 :   Brute Force Approach
Time Complexity: O(n)
Space Complexity: O(1)

In each iteration, we multiply fact by i (i.e., fact = fact * i).

'''

# Using Normal way -
def factNormal(n):
    fact = 1
    # Multiplcation of 1 to till n -
    for num in range(1,n+1):
        fact = fact*num
    
    return fact

print(factNormal(4))  
print(factNormal(3))


'''
# Approch2 : Recursive Approch -

Complexity Analysis

Time Complexity: O(N), Since the function is being called n times, and for each function, we have only one printable line that takes O(1) time, so the cumulative time complexity would be O(N)

Space Complexity: O(N), In the worst case, the recursion stack space would be full with all the function calls waiting to get completed and that would make it an O(N) recursion stack space.


'''

def fact(n):

    if n == 0 : # 0! = 1
        return 1
    
    return n * fact(n-1)

print(fact(4)) 
print(fact(3))