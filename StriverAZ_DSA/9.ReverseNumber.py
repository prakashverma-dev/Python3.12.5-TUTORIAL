'''
Problem statement : -

Ninja is feeling very bored and wants to try something new. So, he decides to find the reverse of a given number. But he cannot do it on his own and needs your help.

Note:

If a number has trailing zeros, then its reverse will not include them. For e.g., the reverse of 10400 will be 401 instead of 00401.




Sample Input:
2
10400
12345

Sample Output:
401
54321


'''

def reverseNumber(n):
    
    revNum = 0
    while n > 0:

        lastDigit = n % 10

        revNum = revNum * 10 + lastDigit # For adding of all lastDigits

        n = n//10 # Updating the number n 

    return revNum

t = int(input()) # For no of Test Case execute at one time for program.
for i in range(t) :
    n = int(input())
    # print(n)
    print(reverseNumber(n))


# Time Complexity : Logarithmic - O(log10(n))
# Space Complexity : Logarithmic - O(1) as no extra space needed.
