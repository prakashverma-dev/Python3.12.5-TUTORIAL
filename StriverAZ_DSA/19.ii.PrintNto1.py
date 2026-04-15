'''   

Coding Nijat Practice : https://www.naukri.com/code360/problems/n-to-1-without-loop_8357243


##CP4 : Print N to 1 using Recursion, return an Array -


You are given an integer ‘n’.



Your task is to return an array containing integers from ‘n’ to ‘1’ (in decreasing order) without using loops.



Note:
In the output, you will see the array returned by you.
Example:
Input: ‘n’ = 5

Output: 5 4 3 2 1

Explanation: An array containing integers from ‘n’ to ‘1’ is [5, 4, 3, 2, 1].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5
Sample Output 1 :
5 4 3 2 1
Explanation Of Sample Input 1:
Input: ‘n’ = 5

Output: 5 4 3 2 1

Explanation: An array containing integers from ‘5’ to ‘1’ is [5, 4, 3, 2, 1].



'''

def printNto1(n):

    temp = [] # Extra space for adding one after another

    def recursive(N):

        if N == 0:
            return
        
        temp.append(N)
        recursive(N-1)
    
    recursive(n)


    return temp

# Input code -
n = int(input())  
print(printNto1(n)) 


# Time Complexity: O(N), we print every number from 1 to N using recursion
# Space Complexity: O(N), stack space used for recursive calls.