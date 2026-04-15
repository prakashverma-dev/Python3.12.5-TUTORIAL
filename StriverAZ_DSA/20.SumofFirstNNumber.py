'''   

Sum of First n Numbers : -


Your task is determining the sum of the first 'n' natural numbers and returning it.


Example:
Input: 'n' = 3
Output: 6

Explanation: The sum of the first 3 natural numbers is 1 + 2 + 3, equal to 6.

Input : 4
Output : 15
Explanation: The sum of the first 5 natural numbers is 1 + 2 + 3 + 4 + 5, equal to 15.

Expected Time Complexity:
The expected time complexity is O(1).
Expected Space Complexity:
The expected space complexity is O(1).



'''

'''
# Approch2 : Recursive Approach -
 
Complexity Analysis -
Time Complexity: O(N),The function is called N times, with each call performing O(1) work.
Space Complexity: O(N),Due to recursive function calls being stored on the call stack, which grows linearly with N.

Intuition : Instead of looping, we can solve the problem using recursion by defining the sum of the first N natural numbers as:

sum(N) = N + sum(N-1), with the base case sum(1) = 1.



'''


def NnumbersSum(N):
        #your code goes here

        if N == 1:
            return 1
        
        return N + NnumbersSum(N-1)

n = int(input()) 
print(NnumbersSum(n)) 



'''

# Approch1 :  Brute Force Approach -


Complexity Analysis -

Time Complexity: O(N),We iterate from 1 to N once, performing a constant-time addition operation in each iteration, resulting in linear time complexity.

Space Complexity: O(1),We only use a few variables to store the sum and loop counter, so the space usage remains constant regardless of N.

'''
# Normal Way -
def sumtillNormal(n):
    sum = 0
    #  Print 1 to n and add all of them -
    for num in range(1, n+1):
         sum += num
    
    return sum

print(sumtillNormal(5))


'''
# Approch3(MOST EFFICIENT WAY) : Using Formula N(N+1)/2 -

Complexity Analysis -
Time Complexity: O(1); as takes one step to execute the sum of first n-number
Space Complexity: O(1); as no extra space or variable used.

# Intuition : We can use the formula for the sum of N numbers, i.e N(N+1)/2.

reutn as  N*(N+1)//2, where N is a given number

'''

def sum(n):

    fisrtNo = 1
    lastNo = n
    NoOfTerms = n # (n2 - n1 + 1); n2 = lastNo; n1= firstNo.

    sum = (fisrtNo + lastNo) * (NoOfTerms) // 2

    return sum 
    # OR, Directly used the formula : n(n+1)/2
    # return n*(n+1)//2 # 5 not 5.0 float value

print(sum(4)) # 10 
print(sum(3)) # 6


# -------------------------------------------------------------


