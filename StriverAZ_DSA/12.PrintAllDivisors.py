
'''
Problem statement
Given an integer 'N', your task is to write a program that returns all the divisors of ‘N’ in ascending order.

Return all the divisors of n as an array or list in a sorted order.

A number which completely divides another number is called it's divisor.


For example:
'N' = 5.
The divisors of 5 are 1, 5.

Sample Input 1 :
10
Sample Output 1 :
1 2 5 10


Explanation of Sample Input 1:
The divisors of 10 are 1,2,5,10.
'''

#1. Brute Force Approach : O(n) Time Complexity 

def allDivisors(n):

    divisors = []
    for num in range(1, n+1):  # T.C : O(n) Linear TC

         if n % num == 0:
             divisors.append(num)
        

    return divisors


# n = int(input())
# print(allDivisors(n)) 

# Note : Here, We takig O(n) Time complexity to solve, we can optimize the iteration run time by runing till square root of given number till loop, as follows and store the N/num or N/i for other half of divisors in un-sorted way.



# Way2 : - Optimal Approach : O (sqrt(n)) Time Complexity

# Iterate from 1 to sqrt(N) and for every divisor found add -
#  i) first num or iteration value
# ii) add its N/num value to it.

import math
def optimizeAllDivisors(N):

    divisors = []
    runtill = int(math.sqrt(N))
    for num in range(1, runtill + 1):  # T.C : O( sqrt(N) ) 

        if N % num == 0:
            divisors.append(num)
        if num  !=  N // num :
            divisors.append(N//num)

    # O (n log n)  --> Sorting takes
    return sorted(divisors) # To sort unsorted stored data.

# Note : mylist.sort() --> sort all of exisitng mylist and dosnot return any any list
#        sorted(mylist) --> sort all mylist and return a new list

# n = int(input())
# print(optimizeAllDivisors(n)) 



# Time Complexity: O(sqrt(N)), we check for every number between 1 and sqaure root of N.
# Space Complexity: O(2*sqrt(N)), extra space used for storing divisors.


# Way3 : using set DS in place of list DS : as we saw, we exclusing the ( N // num != num ) then we adding up the divisors.append(N//num) to avoid the duplicates value. But if we use Set DS. we dont have to use more condition set DS will handle while storing any duplicates it just removes duplicates.

import math
def optimizeAllDivisors2(N):

    divisors = set()
    runtill = int(math.sqrt(N))
    for num in range(1, runtill + 1):  # T.C : O( sqrt(N) ) 

        if N % num == 0:
            divisors.add(num) # Adding all value from 1 to sqrt(N)
            divisors.add(N//num) # Adding all value of N/num from 1 to sqrt(N).

    # O (n log n)  --> Sorting takes
    return sorted(divisors) # To sort set data and convert into list DS**.


n = int(input())
print(optimizeAllDivisors2(n)) 












# -----------------------------------------------------------------
# Creating Diffirent empty D.S using respective braces in python : -
mydict = {}
mylist = []
mytuple = ()

print(mydict, type(mydict)) # {} <class 'dict'>
print(mylist, type(mylist)) # [] <class 'list'>
print(mytuple, type(mytuple)) # () <class 'tuple'>

# Note :  set DS cannot be created using empty {} curly braces, it get created dictionary by default.

#Creating Diffirent empty D.S using respective DS constructors : -
myset1 = set()
mydict1 = dict()
mylist1 = list()
mytuple1 = tuple()

print(myset1, type(myset1)) # set() <class 'set'>
print(mydict1, type(mydict1)) # {} <class 'dict'>
print(mylist1, type(mylist1)) # [] <class 'list'>
print(mytuple1, type(mytuple1)) # () <class 'tuple'>


# Note : only set DS value looks like this and important it does not store any duplicates value in it with unordered storing of data. We use .add() to add data and .

myset1.add(5)
print(myset1) # {5}

myset1.add(5) # canot add duplicates.
print(myset1) # {5}

myset1.add(6)
myset1.add(8)
myset1.add(9)
myset1.add(10)
print(myset1) # {5, 6, 8, 9, 10} # Unordered data

# To know length -
print(len(myset1)) # 5



