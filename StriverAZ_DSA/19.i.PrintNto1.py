'''
#CP3 : Print N to 1 using Recursion

Hints
Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.

You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in decreasing order from n to 1

Example 1

Input: 5

Output:

5

4

3

2

1

Example 2

Input: 1

Output:

1


'''


class Solution:
    def printNumbers(self, n):
        
        if n == 0:
            return
        
        print(n)
        self.printNumbers(n-1) 
    

# Input Driver Code -
n = int(input())
# creating object -
obj = Solution()
obj.printNumbers(n) 



# Complexity : -
# Time Complexity: O(N), we print every number from N to 1 using recursion
# Space Complexity: O(N), stack space used for recursive calls.








