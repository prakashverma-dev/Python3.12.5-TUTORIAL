

def missingNum(arr):

    actualN = N = len(arr) + 1
    n = len(arr) # currentn

    # sum of expected natual number -

    expectedSum = (N*(N+1))/2
    
    print(expectedSum)

    # Now sum of given array -

    sum = 0
    for i in range(n):

        sum = sum + arr[i]
    
    # print(sum)

    print(expectedSum - sum)


missingNum([1,2,3,5])