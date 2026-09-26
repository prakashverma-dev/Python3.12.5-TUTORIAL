'''  Q1. WHat is Difference between list and tuple ?

List is mutable where as tuple is immutable
 
Tuple is fast in compare with List.


Q2. List Compreshension -

'''


square = []
for i in range(10):
    if i%2 == 0:
        square.append(i ** 2)

print(square)

# using list comprehension -

sq = [i**2 for i in range(10) if i%2 == 0]
print(sq)


# Q3. Q3 - What is the diff between deepcopy and shallowcopy -

''' 
In shallow Copy, when we create a copy it creates a new object which stores the reference of the original elements. 




'''

import copy

orginArr = [ [1,2,3], [4,5,6] ]

shalowcopy = copy.copy(orginArr)

shalowcopy[0][0] = 99

# Let' ssee original array -
print(orginArr)  # [[99, 2, 3], [4, 5, 6]]

# Deep copy : Create a new reference while creating the new object with it -

orginArr2 = [ [1,2,3], [4,5,6] ]
deepcopy = copy.deepcopy(orginArr2)
deepcopy[0][0] = 99

# Let' ssee original array -
print(orginArr2)  # [[1, 2, 3], [4, 5, 6]] // It doesnot change.


# Q.4 - Reverse a string -

def reverseStr(str):
    n = len(str)
    reverse = ""

    for char in range(n, -1, -1):

        reverse += char


    return reverse


# Q.5 - String Palindrom -

def palidromeStr(str):
    n = len(str)
    reverse = ""

    for char in range(n, -1, -1):

        reverse += char


    return reverse == str



# Q6. Factorial 

def fac(n):

    if(n==0):
        return 1
    
    return n * fac(n-1)

print(fac(5))


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        
        fact = fact * i 

    return fact


print(factorial(5))

#Q7. Check for anagram : silent and listen --> yes

# def anagram()
    

#Q8. Two Sum - 
l= [1,2,5,6,7] 
target = 10

# Tell me if there is a pair of number in l which adds up to target.







#Q9. Check where parenthisis are balanced or not / valid parenthesis -
# "()" ---> Balanced
# "([])" --> Balanced
# "((("  --> Not Balanced

valid = '{([])}'
invalid = '{([])'



# Q10. Find the missing number from input -
input = [1, 2, 3, 5]
output = 4



# Q11. Count Character Fequency -
Input = "Banana"

# Output = {
#     b: 1,
#     a: 3,
#     n: 2,
# }


# SQL Interview Questions -

#1. Find the highest second salary of the employee.
# 2.Find employee having duplicates names.

# SELECT name, COUNT(*) AS total
# FROM employees
# GROUPBY name
# HAVING COUNT(*) > 1



