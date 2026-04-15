'''
# CP1. Print 1 to N using Recursion -

Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.

You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in increasing order from 1 to n.

Example -
Input: n = 5

Output:
1  
2  
3  
4  
5

OR, Output : 
1 2 3 4 5   ---> print(n, end = " ")

'''


class Solution:
    def printNumbers(self, n):

        if n == 0:
            return
        
        self.printNumbers(n-1)
        print(n)
        # print(n, end=" ") # 1 2 3 4 5




# Input Driver Code : -
n = int(input())

# creating the object of class 'solution' and calling it -
if __name__ == "__main__":
    sol = Solution()
    sol.printNumbers(n)    

# Time Complexity: O(N), we print every number from 1 to N using recursion
# Space Complexity: O(N), stack space used for recursive calls.





'''
Note : here if block-  __name__ == "__main__":

This ensures: This code runs only when the file is executed directly from current file.

It will NOT run if the file is imported somewhere else (e.g., for testing)

Note : if __name__ == "__main__": ensures that code runs only when the file is executed directly, not when imported as a module like import myfile, import math_utils.

Very common in LeetCode / GFG / CodeStudio style problems.

'''








