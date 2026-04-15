'''
# GCD of Two Numbers :-

You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.

The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


Example 1

Input: n1 = 4, n2 = 6
Output: 2

Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
Greatest Common divisor = 2.

Example 2

Input: n1 = 9, n2 = 8
Output: 1
Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
Greatest Common divisor = 1.




------------------------------------------------------------------

# GCD or HCF : Greatest Common Divisor or Highest Common Factor : -

N1 = 9 = 1, 3, 9
N2 = 12 = 1,2,3,4,6,12

Here, HIGhest Common Divisor is '3'. that we need to find out from the quetion.


# 1. Brute Force Approach :- loop from 1 to min(N1,N2)


Pseudo Code : Can we say if we take the smallest number till we loop the iteration we get highest divsior for both number. Thus we use min(N1,N2).

and then we divide both number with range from 1 to min(N1, N2) till last divide of the loop as we need to find the greated divisor, and we keep updating GCD as soon as both number get divide by iteration 'num'. and at the end final both divisor we will get.


GCD = 1 # The minumum divisor of any two numbers.

for(num = 1 ; num <= min(N1, N2); num++ ){

    if(N1 % num == 0 &&  N2%num == 0){
            GCD = num # updated GCD
        }

}

return GCD;

Time Complexity : O ( min(N1,N2) )) ~ O ( N ) ~ Linear 

#2. Better Approch :- Loop reverse min(N1,N2) to 1 for Time Efficieny and break the loop as soon as found.

Intuition:
We can optimise the time complexity of the previous approach. In the worst case, the loop iterates from 1 up to the minimum of N1 and N2. This could potentially result in a large number of iterations, especially when one input number is significantly larger than the other.

If we iterate from the minimum of N1 and N2 down to 1, we reduce the number of iterations because we start from the potentially largest common factor and work downwards.

The time complexity of this approach remains O(min(N1, N2)) but in practice, it will execute fewer iterations on average.


GCD = 1 # The minumum divisor of any two numbers.

for(num = min(N1, N2) ; num >= 1; num-- ){

    if(N1 % num == 0 &&  N2%num == 0){
            GCD = num # updated GCD
            break; # we break the for loop as soon as we get first GCD coz it will be highest as loop itertes from higher to lower.
        }

}

return GCD;


Time Complexity : O ( min(N1,N2) )) ~ O ( N ) ~ Linear 

#3. Optimal Approach : using 'Euclidean Algorithm' : It states a formula to solve two number GCD -

gcd(a, b) = gcd(a-b, b)
gcd(N1, N2) = gcd(N1-N2, N2)

OR, In other way, we use in code -

gcd(a,b) = gcd(a%b, b) ;      % moduler

Here, Divide a/b or b/a untill divisor get zero at one side; --> 

i.e  a = a % b  or 
     b = b % a  untill one becomes 0, the other is the GCD.  

Here, greaterNum % smallerNum  ---> loop on till one of them become zero then other one is gcd.

while(a> 0 && b > 0){

    if(a>b)  a = a%b
    else     b = b%a
}

if(a == 0) { ---> while loop false
    print("GCD : ", b )
}
else{
    print("GCD : ", a )
}

Time Complexity : O ( log( min(N1,N2) )) ~ O ( log( N )) ~ Logarithmic



# Euclidean Algorithm:

The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
of two numbers. It operates on the principle that the GCD of two numbers remains
the same even if the smaller number is subtracted from the larger number.

To find the GCD of n1 and n2 where n1 > n2:
1. Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
2. Once one becomes 0, the other is the GCD of the original numbers.

Example:
n1 = 20, n2 = 15

gcd(20, 15) = gcd(20 - 15, 15) = gcd(5, 15)
gcd(5, 15)  = gcd(15 - 5, 5)  = gcd(10, 5)
gcd(10, 5)  = gcd(10 - 5, 5) = gcd(5, 5)
gcd(5, 5)   = gcd(5 - 5, 5)  = gcd(0, 5)

Hence, return 5 as the GCD.
'''


#1.  Brute Force Approach :- loop from 1 to min(N1,N2) 

# Time Complexity : O ( min(N1,N2) )) ~ O ( N ) ~ Linear 

def gcd(N1, N2):

    GCD = 1
    for num in range(1, min(N1,N2) + 1 ):
        if N1%num==0 and N2%num==0:
            GCD = num
        
    return GCD 

# Input Handler-
arr = input().split(" ")
n1,n2 = map(int, arr)
print(gcd(n1,n2)) 

# NOte : a,b,c= map(int,input().split()) -->  # Taking 3 space separated Integer value as Input
#       mylist = list(map(int, input().split())) --> # Taking array as Input 




#2. Better Approch :- Loop reverse min(N1,N2) to 1 for Time Efficieny and break the loop as soon as found.

# Time Complexity : O ( min(N1,N2) )) ~ O ( N ) ~ Linear 

def gcd2(N1, N2):

    GCD = 1
    for num in range( min(N1,N2), 0, -1 ):
        if N1%num==0 and N2%num==0:
            GCD = num
            break
        
    return GCD 

# Input Handler-
arr = input().split(" ")
n1,n2 = map(int, arr)
print(gcd2(n1,n2)) 


#3. Optimal Approach : using 'Euclidean Algorithm' : It states a formula to solve two number GCD -

# gcd(a,b) = gcd(a%b, b) ;      % moduler

# Here, greaterNum % smallerNum  ---> go on till one of them become zero then other one is gcd.

# Time Complexity : O ( log( min(N1,N2) )) ~ O ( log( N )) ~ Logarithmic

def gcdOptimize(a, b):

    while a > 0 and b > 0:

        if a>b :
         a = a % b

        else :
         b = b % a

    if a == 0:
       return b
    else:
       return a


# Input Handler-
arr = input().split(" ")
n1,n2 = map(int, arr)
print(gcdOptimize(n1,n2)) 