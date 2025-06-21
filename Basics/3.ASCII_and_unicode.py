'''

#ASCII : Ashkayi(pronunciation) - It is American Standard Code For Information Interchange. It is help to represent "each characters as numeric codes"

 A - Z(Capital Letters) --> 65 to 90 Codes
#where A character numeric code is 65 in ASCII,  B --> 66 and 90 --> Z

 a - z(Small Letters) ---> 97 to 122

 0 - 9(If we see '0' as character value)  ---> 48 to 57 (ASCII Value)

 space(" " --> one space character)  --->  32 


 # ord() function : It is a Inbuilt function of python to know ASCII Code or Value of any character. This function takes a string of length 'one' character only. and returns the ASCII code corresponding to that character.
 

The 'ord' function is short of ordinal which means a number. The ord function in python accepts a single character as an argument and returns an integer value representing the unicode equivalent of that character.

print(ord("a"))  #97
print(ord("A"))  #65
print(ord(" "))  #32



# chr() function : Opposite of ord() function. It returns the character as string of passed ASCII value/code.

print(chr(67))  #67
print(chr(32))  #  (space)

'''

print(ord("a"))  #97
print(ord("A"))  #65
print(ord(" "))  #32

print(chr(67))  # C
print(chr(32))  # (space)

# To print a to z -

for i in range(65, 65+26):
    print(chr(i))



