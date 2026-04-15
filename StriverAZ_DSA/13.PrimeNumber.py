'''
Check for Prime Number 

You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.


Note : A prime number is a number which has no divisors except 1 and itself the number. In other words, a prime number have only two factors i.e 1 and number itself i.e 1 * 11 = 11 Prime number


5 -> Divisible by 1,5. Hence, 2 divisors --> Prime
2 -> Divisible by 1,2. Hence, 2 divisors --> Prime
11 -> Divisible by 1,11. Hence, 2 divisors --> Prime
13 -> Divisible by 1,13. Hence, 2 divisors --> Prime
4 ->  Divisible by 1,2,4. Hence, 3 divisors --> not Prime
8 ->  Divisible by 1,2,4,8. Hence, 4 divisors --> not Prime
17 -> Divisible by 1,17. Hence, 2 divisors --> Prime


Example 1

Input: n = 5

Output: true

Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.



'''

# 1. Brute Force Approach : O(n) Time Complexity 

def isPrime(N):

    countDivisor = 0 # if it is 2 Divisor then only it is Prime Number.
    # countlength = [] # We could use list length to determine Prime if length is 2 then prime else not prime.
    
    for num in range(1, N+1):
        if N % num == 0:
            countDivisor += 1
            # countLength.append(num)


    return countDivisor == 2 # if Divisor get 2 then only it is Prime Number.
    # return len(countLength) == 2
    
# Note : If the number of factors is exactly 2 (1 and the number itself), it's prime

n = int(input())
print(isPrime(n))

# Complexity Analysis of Brute Force Approach : - 

# Time Complexity: O(N), as we iterate from 1 to N performing constant-time operation for each iteration.

# Space Complexity : O(1), as the space used by the algorithm does not increase with the size of the input.




#2. Optimal Approach : O (sqrt(n)) Time Complexity 

import math
def optimizePrime(N):

    count = 0
    runtill = int(math.sqrt(N))

    for num in range(1, runtill + 1):

        if N % num == 0:
            count += 1

        if num  !=  N // num:
            count += 1

    # if count == 2:
    #     return True
    # else :
    #     return False

    return count == 2 # if Divisor get 2 then only it is Prime Number.

n = int(input())
print(optimizePrime(n))


'''
# Complexity Analysis of Optimal Approach : -

Time Complexity: O(sqrt(N)), as The loop iterates up to the square root of n performing constant time operations at each step.

Space Complexity : O(1), as the space complexity remains constant and independent of the input size. Only a fixed amount of memory is required to store the integer variables.


'''

#3. Brute Force Approach using list DS in place of countDivisor : O(n) Time Complexity 

# Here, we used list DS to get len to calculate stored data in list if it is 2 then Prime else Not Prime.


def isPrime2(N):

    list = [] # if it is 2 length then only it is Prime Number.

    for num in range(1, N+1):
        if N % num == 0:
            list.append(num)


    return len(list) == 2 # if list have only 2 length then it is prime else Not.

# Note : If the number of factors is exactly 2 (1 and the number itself), it's prime

n = int(input())
print(isPrime2(n)) 



#4. Optimized Approach using set DS in place of countDivisor : O(sqrt(n)) Time Complexity 

# Here, we used set DS to get len to calculate stored data in set if it is 2 length then Prime else Not Prime.


import math
def optimizePrime2(N):

    myset = set() # if set have only 2 length then it is prime else Not.
    runtill = int(math.sqrt(N))

    for num in range(1, runtill + 1):

        if N % num == 0:
            myset.add(num)
            myset.add(N // num)

    return len(myset) == 2 # if set have only 2 length then it is prime else Not.

n = int(input())
print(optimizePrime2(n)) 