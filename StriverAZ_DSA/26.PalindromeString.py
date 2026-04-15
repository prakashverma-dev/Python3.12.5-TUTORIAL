'''  

Check if a String is Palindrome or Not : We use Functional Recursion ; Returns true or Flase result value.

# We reverse first index string with last index string and after reversed compplety then we compare with the 
original string -

Ex: "MADAM" ---> "MADAM"  ---> True 
    "11211"  ---> "11211"


f(i){

    if (i >= n/2){

        return true; # for last case when reaches n//2 still not false means its true.
    }

    if (str[i] != str[n-1-i]){
        return false;
    }

    # if not above ..repeat the recursive
    return f(i+1); for upcoming indexes.



}


'''

# i) General Way : using One Pinter with no extra space cheking first and last index and continues -
# Note : We could take two pointer for checking left char and right char that is Equal or not and proceed -

# Time Complexity: O(N), where N is the length of the string. Each character is compared at most once till the middle of the string.
# Space Complexity : O(1) due to no extra sppace we need.

''' 

# Algorithm -

>To check whether a string is a palindrome, we only need to compare characters from the start and end, moving towards the center.

>Run a for loop from i = 0 to i < str.length() / 2. This ensures that each character is compared with its corresponding character from the end.

>In each iteration, compare the character at the front str[i] with the character at the back str[str.length() - i - 1].

>If at any point these characters do not match, return false as the string is not a palindrome.

>If the loop completes without returning false, then the string is a palindrome, and we return true.





'''

def isPalindrome(str):

    n = len(str) 
    for i in range(0, n//2):

        if str[i] != str[n-1-i]:
            return False


    return True

str = "PRAKASH"
str1 = "MADAM"
str2 =  "11211"
print(isPalindrome(str)) 
print(isPalindrome(str1)) 
print(isPalindrome(str2))  


# ii) Using Recursion Approch : Space Complexity will get increased here from previos O(1) to O(n).
# Time Complexity : O(n)
# Space Complexity : O(n) due to call stack.

'''  
# Algorithm : - Same Approch above just added recusion to check first and last char and continues -

Use recursion to compare characters at the start and end of the string.
If the characters are not equal, return false indicating the string is not a palindrome.
If they are equal, recursively call the function with the next set of indices: start + 1 and end - 1.
Base Case: If the start index becomes greater than or equal to the end index, return true as it means the entire string has been checked and is a palindrome.



'''

def palindromeCheck(i, str):

    n = len(str)

    if i >= n//2:
        return True
    
    if str[i] != str[n-1-i]:
        return False
    
    # if not above ..repeat the recursive
    return palindromeCheck(i+1, str) # for upcoming indexes.

str = "PRAKASH"
str1 = "MADAM"
str2 =  "11211"
print(palindromeCheck(0, str)) # start left Pointer from 0th index.
print(palindromeCheck(0, str1))
print(palindromeCheck(0, str2)) 



# iii) Using Baisc : Extra New String Storage Space and Checking it back -
# Time Complexity: O(n), as every character needs to be processed once to be included in the new string.
# Space Complexity: O(n), as a new string of size 'n' is allocated in memory to store the reversed characters. 

def isStringPalindrome(str):

    # print(id(str)) 

    n = len(str)
    newStr = ""

    for i in range(n-1, -1, -1):
        # print(i, str[i])

        newStr += str[i]

    # print(newStr)
    return str == newStr


str = "Prakash" 
str2 = "11211"
str3 = "MADAM"
# print(id(str)) 

print(isStringPalindrome(str))  # False
print(isStringPalindrome(str2))  # true
print(isStringPalindrome(str3))   # True


