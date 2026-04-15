'''
Check if a number is Armstrong Number or not

Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Example 1:
Input:N = 153
Output:True
Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
Example 2:
Input:N = 371                
Output: True
Explanation: 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371

Example 3:
Input:N = 1634               
Output: True
Explanation: 1^4 + 6^4 + 3^4 + 4^4 =  1634

Example 4:
Input:N = 35              
Output: False
Explanation: 3^2 + 5^2 = 9 + 25 = 34


'''

def isArmstrong(n):

    originalNum = n

    countDigit = len(str(n))
    summation = 0 # Will store the ArmStrong number here after summation

    while n > 0:

        lastDigit = n % 10
        summation = lastDigit**countDigit + summation

        n = n//10

    return originalNum == summation


n = int(input())
print(isArmstrong(n))


# Time Complexity : Logarithmic - O(log10(n))
# Space Complexity: O(1) as only a constant amount of additional memory for the reversed number regardless of size of the input number.



