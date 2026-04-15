# Multiple Recursion Calls : - When we call recusive function more than one times inside main recursion function called as Multiple recursion calls as shown below. and Most Important each recursive call starts and when it ends then the second recusion call starts and then ends then more to third recursive call..and so on untill last recursive call.Thats why as per no of times recusive calls there --> The Time Complexity is like Exponential in nature for two times recusive call 2^n Exponential Time Complexity which is for Fobonacci Series solving via Recusive Approch Time Complexity.

''' 

f(){

    f()  --> This will happen then come back
    f()  --> This will happen then come back
    f()  --> This will happen then come back
    .
    .    --> multiple time called.


}

Best Example: Fibonacci Numbers -

0 1 1 2 3 5 8.....

0th Fibonacci = 0
1th Fibonacci = 1
2th Fibonacci = 1
3rd Fibonacci = 2
4th Fibonacci = 3



Q: N ---> f(N) ---> give nth fibonacci Number in return
          f(4) ---> 3
          f(3) ---> 2 

Here, f(4) --> f(3) + f(2)  (Previous two function get added.)


'''
# Approch1 : Using Recursion (Inefficient coz Time Complexity : O(2^n) i.e Exponential Time Complexity. ) : -
# f(n) --> f(n-1) + f(n-2)

# Time Comlexity : O(2^n)
# Space Comlexity : O(n)

# Note : Always In Recusive approach, we get the Exponential Time Complexity in nature coz we calling twice recursive call each time which leads to 2^n Times, thus Time complexity becomes 2^n i.e Exponential Time Complexity.

'''
Complexity Analysis

Time Complexity: O(2^N) { This problem involves two function calls for each iteration which further expands to 4 function calls and so on which makes worst-case time complexity to be exponential in nature }.

Space Complexity: O(N) { At maximum there could be N function calls waiting in the recursion stack since we need to calculate the Nth Fibonacci number for which we also need to calculate (N-1) Fibonacci numbers before it }.

'''

def fibonacci(n):

    if n <= 1 :
        return n
    
    last = fibonacci(n-1)
    secondlast = fibonacci(n-2)

    return last + secondlast

    # return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(0)) 
# print(fibonacci(1)) 
# print(fibonacci(2)) 
# print(fibonacci(3)) 
print(fibonacci(4)) 
# print(fibonacci(-1)) 


# Approach2 : using an Array to store or array of (n+1) fixed size to store -

# Time Complexity : O(n) for going all n-terms. 
# Space Complexity: O(n) for storing the fibonacci series.

''' 
# Iterative Approch with Array Assignement(it needs fixed sized in python) :-

fib = [None]*n # Creating the size in python
fib[0] = 0
fib[1] = 1

for (i = 2 to n){
    fib[i] = fib[i-1] + fib[i-2]
}

Time : O(n)
Space : O(n)


'''

def fibonacci(n):

    if n <= 1:
        return n
    
    fib = [0, 1] 
    for i in range(2, n+1): 

        fib.append(fib[i-1] + fib[i-2])
    
    # return fib # to return complete fibonacci series in array.
    return fib[n] # To return the value at ith fibonacci indexed.

# print(fibonacci(-1))  
print(fibonacci(4))    
# print(fibonacci(3)) 

# With Array Fixed Size Way 
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1 

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Same Complexity -
# Time: O(n)
# Space: O(n)



## Approach3(MOST EFFICIENT) : TO Avoid Space Complexity from O(n) to O(1) with no taking extra space -
'''
Time Complexity: O(N).As we are iterating over just one for a loop.
Space Complexity: O(1), no extra space used.

Approach
Take two variables last and secondLast for storing (i-1)th and (i-2)th term.
Now iterate from 2 to n and calculate the ith term. ith term is last + secondLast term.
Then update secondLast term to the last term and the last term to ith term as we iterate
Complexity Analysis : 



'''
# We use two variables to store initial values a and b and we use temp as temporty store for storing value for next itertaion  -

def fibEfficient(n):
    if n <= 1:
        return n

#   0 1 1 2 3 ...
#   a b a b 

#   Here for next item -
    # a = b (a will be previous b)--> b = 
    # b = a + b (b will be previous a +b)
 
    a = 0 
    b = 1     

    for i in range(2, n + 1):
            temp = a + b  # Current ith Fibonacci number
            a = b # a will be the next item in the series always i.e b
            b = temp 

    return b

print(fibEfficient(5))
print(fibEfficient(4)) 
print(fibEfficient(-1))  



