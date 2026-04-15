'''
# CP2 : Print 1 to N using Recursion - return an array as resultant -

You are given an integer ‘n’  

Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.

Example:
Input: ‘n’ = 5
Output: 1 2 3 4 5

Explanation: An array containing integers from ‘1’ to ‘n’ is [1, 2, 3, 4, 5].
Detailed explanation ( Input/output format, Notes, Images )

Sample Input :
5
Sample Output :
1 2 3 4 5

Explanation Of Sample Input 1:
The array contains all integers from 1 to 5 in ascending order.

'''


# Link To Practice on Code360 : https://www.naukri.com/code360/problems/print-1-to-n_628290

def printNos(n) : 
    # Write your code here
    # pass
    if n == 0:
        return []
    
    return printNos(n-1) + [n] 

# Input code -
n1 = int(input())
print(printNos(n1))    



# Other Way : taking helper function for recursive call -
def print1toN(n):

    arr = []
    # taking a helper function for recursive call-
    def helper(N):

        if N == 0:
            return

        helper(N-1)
        arr.append(N)
    
    helper(n)
    return arr 

# Input code -
n2 = int(input())  
print(print1toN(n2))


# Time Complexity: O(N), we print every number from 1 to N using recursion
# Space Complexity: O(N), stack space used for recursive calls.
