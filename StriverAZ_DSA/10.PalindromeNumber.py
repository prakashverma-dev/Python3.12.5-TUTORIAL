

def isPalindrome(n):

    originalNum = n
    reverseNum = 0
    while n > 0:

        lastDigit = n % 10
        reverseNum = reverseNum*10 + lastDigit 

        n = n//10

    if originalNum == reverseNum : return True
    else: return False

    # OR, 
    # return originalNum == reverseNum
    

n = int(input())
print(isPalindrome(n))

# For strict 'true' and 'false' character value -   
# if isPalindrome(n):
#     print("true")
# else :
#     print("false")



# Time Complexity : Logarithmic - O(log10(n))
# Space Complexity : Logarithmic - O(1) as no extra space needed.