'''
s = "abcdabcfe"

here are 'q' no of queries to do in the above string to find "how many times a character is present in the above string" -

a --> 2
c --> 2
z ---> 0


'''

# There are two approaches : -


'''
## Approch1(Brute Force approach:) : taking counter variable as zero and looping over string once that char found increase the coun value.

It is similar to the previous problem. Here, for each query, we will iterate over the string using a for loop and will count the number of times the character appears in that string i.e. increment the counter variable if the character at that index of the string equals the given character. In terms of function, it will look like the following:


f(s, char){

    count = 0
    for (i= 0; i< len(char); i++){

            if(s[i] == char){
                count += 1
            }
    
        }

    return count

}

Note : THis will take O(Q*N) Time Complexity; For Optimizing we can hash them into array to solve time complexity.

'''


def charFreq(str, c):
    # c ---> 'c' our target char.

    count = 0
    for i in range(0, len(str)):
        if str[i] == c:
            count += 1

    return count


''' 
## Approch2(Optimized) : using hasharry apporoch to increase hasharray item as freqency count.

# Since there are 25 alphabets so we can map array indexes as aplhabets 26 characters.
arr = [0 , 0 , 0 , 0 , ........]
       0   1   2   3  4         25
       a   b   c   d  e        z 

Case1: if string contains only lowercase letters -

To map 0 as a and 1 as b and so on..
 0 --> a
 1 --> b
 2 --> c
 25 --> z

 # ASCII Values : - ASCII stands for the "American Standard Code for Information Interchange".
 There are ASCII Values for each 256 character set like lowercase, uppercase, digits etc.

 UpperCase A ---> 65
 UpperCase B ---> 66
 UpperCase Z ---> 99

 lowercase a ---> 97
 lowercase b ---> 98
 lowercase z ---> 122

 int x = 'a' ---> x stored ascii value of 97 for char a.

 To align with array indexing number 0,1,2,3.. for hashing character set -

 'a' - 'a' = 97 - 97 = 0
 'b' - 'a' = 98 - 97 = 1
 'c' - 'a' = 99 - 97 = 2
 'd' - 'a' = 100 - 97 = 3
 'z' - 'a' = 122 - 97 = 25

 In python, to know ascii value for character use ord() function.

 arr = [0] * 26  ---> for lowercase letters.

Case2: if string contains only uppercase letters A-Z -

'A' - 'A ' = 65 - 65 = 0
'B' - 'A ' = 66 - 65 = 1
'C' - 'A ' = 67 - 65 = 2
'Z' - 'A ' = 90 - 65 = 25

arr = [0] * 26  ---> for uppercase letters.

case3 : if String is mixed with uppercase and lowercase then -

 If the string contains both uppercase and lowercase letters: We have 256 characters in total in this case. So, we will create a hash array of size 256. We will not subtract anything from the given character and will use the character as it is, to access the hash array while pre-storing and fetching. 
 
 For pre-storing hash[s[i]] += 1




'''

# Suppose, if input string is mixed of lower-case and upper case, we take 256 array size and we will store all ascii value as it is as "hasharr indexes numbers" -

# No of characters exits is 256 total.

def charFreq1(str, char):
    # c ---> 'c' our target char.

    # we defined 256 char arry max size -
    hasharr = [0] * 256

    for i in range(0, len(str)):

        asciiValue = ord(str[i])
        hasharr[asciiValue] += 1

    # return hasharr
    return hasharr[ord(char)]


# IF input string is only lower-case, then we take hasharray max 25 size and we will try to map hasharray indexes with ASCII valuues with ord(str[i]) - ord("a")  to get corrent char -

def charFreq2(str, char):
    # c ---> 'c' our target char.

    # we defined 26 char arry max size of lowerCase all chars -
    hasharr = [0] * 26

    for i in range(0, len(str)):

        asciiValue = ord(str[i]) - ord("a")
        hasharr[asciiValue] += 1

    # return hasharr
    return hasharr[ ord(char) - ord("a") ] 


def charFreq3(str, char):
    # c ---> 'c' our target char.

    # we defined 26 char arry max size of upperCase all chars -
    hasharr = [0] * 26

    for i in range(0, len(str)):

        asciiValue = ord(str[i]) - ord("A")
        hasharr[asciiValue] += 1

    # return hasharr
    return hasharr[ ord(char) - ord("A") ] 



# Approch3 : In Number hashing we can hasharray with HASHMap of python ie dictionay to solve storing freqeuncy is optimized way with we can store any number of size we do not need to define size pre.
# 
#   
# using Hashmap (dictionary in python )

def char_frequency(str, item):
    hashmap = {}

    for i in range(0, len(str)):
         hashmap[str[i]] = hashmap.get(str[i], 0) + 1 # O(1))

    return hashmap.get(item, 0) #if item doesnot found we get 'zero' value. --> O(1)


# Example
s = "programming"
# print(char_frequency(s))


# Input-
# "abcdabcfe"
# 3
# a
# c
# z

# Input Driver code -
str = input()
t = int(input())
for _ in range(0, t):
    s = input()
    # print(charFreq(str, s))  # For General Way
    # print(charFreq1(str, s))  # For ASCII 256 hasharry size.
    # print(charFreq2(str, s))  # For ASCII lowercase, 26 hasharry size.
    # print(charFreq3(str, s))  # For ASCII uppercase, 26 hasharry size.
    print(char_frequency(str, s)) # For using HashMap for hashing.


# Time Complexity analysis of the function:

# It is as same as the one we calculated for the previous problem. If the number of queries is Q, the time complexity will be O(Q*N) where N = size of the string.

# Time Complexity Analysis of Hashmap : -

# Time Complexity  : O(n) as O(1) for loop up but O(n) for looping.
# Space Complexity  : O(n)


# Note : HashMap DS build using 'Division Method' or 'Folding Method' or 'Mid Square Method ' the reason stores any size bydefault even more than 10^7.


