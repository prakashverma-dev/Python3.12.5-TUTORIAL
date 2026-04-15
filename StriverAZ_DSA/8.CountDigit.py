'''
1. Count digits in a number : -

Problem Statement: Given an integer N, return the number of digits in N.
 521 ---> 3 
 3219 ---> 4
 7 ---> 1

'''

'''

Approach:

Initialise a counter to keep the count of digits in the number. 
Keep dividing the number by 10 until no more digits are left to extract.
For every digit extracted from the number, increment the counter by 1.
Once the iterations are over, the number of digits is stored in the counter.



'''

def countDigit(N):

    count = 0
    while N>0:

        lastDigit = N % 10 #last Digit each time
        count = count + 1 # Update the no of remainder


        N = N // 10 # To update N value for next while loop.

    return count # In CCP we just have to return value, print will be handled by inside input handler.

# n = int(input())
# print(countDigit(n))

# Time Complexity : O ( log10(n) ) coz while loop runs to N/10 if it N/2 TC : log2(n)
# Note : If no to iteration gets division, always remember Time complexity will be Logarithimic.




# Approch2 :  use : log10(N) + 1 = will get float value convert into integer 
# import math
# def countDigit(n):

#     count = math.log10(n) + 1
#     return int(count)

# n = int(input())
# print(countDigit(n))


# Approch3 :  Convert Interger value into string and return the string length 

def countDigit(n):

    strNum = str(n)
    return len(strNum)

n = int(input())
print(countDigit(n))