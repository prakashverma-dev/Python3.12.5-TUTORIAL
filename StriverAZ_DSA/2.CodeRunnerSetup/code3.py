
# Input First Line --> no of total test cases(We dont know test cases)
# Input Second Line ---> First Test Case(array size)
# Input Third Line ---> Second Test Case(arry itself)
# so on...

def myMainFunction():
    pass  # It return a value



# Input Handler /Driver Code -

t = int(input()) # First line --> no of total test cases
for _ in range(t):
    n = int(input()) # for each line test case, array size
    arr = list(map(int, input().split())) # for each test case, arry itself
    print(myMainFunction(n, arr))


# Here an Sample Example of this Test Case, we get two  test cases -
'''

2  ---> no of test cases
7  ---> First Array size
0 4 1 1 7 4 3  --> First array itself
7  ---> Second Array Size
0 6 7 5 1 1 1  ---> Second array itself

'''
