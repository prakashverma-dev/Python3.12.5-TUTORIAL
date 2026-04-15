
## Must do Pattern Problems before starting DSA to master the How programming Loops occurs.     

'''
There are three(+1 Optional) Steps to solve any Pattern In the world : -

Pattern Problem : We deal pattern problem in two dimension way to solve any pattern problem, we take inner loop and outer loop to solve pattern problems. i.e Pattern means Nested loops. Time Complexity O(n^2).

no of row in pattern ---> Outer Loop we take
no of column ---> inner loop we take where we print our values. 

***  ---> rows 
***
***
|
columns

Step1 : For the outer loop, count no of lines or rows in the pattern.
Step2 : For the inner loop, focus on the columns and connect them somehow to the rows.          
Step3 : Whatever we printing, print them "*" inside the inner for-loop.
Step4(Optional) : Observe the Symmetry, applicable to some pattern.





'''


# Application of for-loop is Pattern Printing : -


# Q1. 

'''                 
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 4, the pattern should look like as below:


*****

*****

*****

*****


Print the pattern in the function given to you.

'''
# FOr i = 0 ---> j = 0,1,2,3
# FOr i = 1 ---> j = 0,1,2,3
# FOr i = 2 ---> j = 0,1,2,3
# FOr i = 3 ---> j = 0,1,2,3

def pattern1(n):

    # n = 4 # no of rows
    for i in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
        print("\n")

# n = int(input()) 
# pattern1(n)

# Q2. Based on input, Print following pattern, example if n = 5; output should be -

'''                 
*       
**
***
****
*****

'''

def pattern2(n):

    # n = 4 # no of rows
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\n")

# n = int(input()) 
# pattern2(n)


# Q3. Based on input, Print following pattern, example if n = 5; output should be -

'''                 
1       
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''
def pattern3(n):

    # n = 4 # no of rows
    for i in range(0, n):
        for j in range(0, i+1):
            print(j+1, end=" ")
        print("\n")

# n = int(input()) 
# pattern3(n)


# Q4. Based on input, Print following pattern, example if n = 5; output should be -

# Note : Here we printing row number each time for each line.
'''                 
1       
2 2
3 3 3
4 4 4 4
5 5 5 5 5

'''

def pattern4(n):

    # n = 4 # no of rows
    for i in range(0, n):
        for j in range(0, i+1):
            print(i+1, end=" ")
        print()

# n = int(input()) 
# pattern4(n)

# Q5. 
'''                 
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


*****

****

***

**

*


Print the pattern in the function given to you.

'''

def pattern5(n):

    # n = 4 # no of rows
    for i in range(0, n):
        for j in range(n, i, -1):
            print("*", end=" ")
        print()

# n = int(input()) 
# pattern5(n)

'''
Q6. Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



12345

1234

123

12

1

'''

def pattern6(n):

    # n = 4 # no of rows
    for i in range(0, n):
        for j in range(n, i, -1):
            print(j, end=" ")
        print()

n = int(input()) 
pattern6(n)






