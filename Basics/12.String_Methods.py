


#String Methods or Functions : Python has a set of built-in methods that you can use to perform some string operations over original string and return a new string always.      

# Note: All string methods returns new values. They do not change the original string.

#In OOPs, all functions are called as methods, it is the concept of OOPs.

# Note: In python everthings are objects that OOPs concept of visualizing everthing what we see around us. And Object can have properties and methods/i.e function can be accessed using dot notation.

# 1. len() : To find the length of string using len() function. It returns the length of a string.


text = "owww they are very good and very bad"
print(len(text))


# 2. find() : It returns the first occurance index of the character or substring that present in the original string and returns -1 if not found in original string.

# NOte: As we know python is case sensitive langauge so if we pass character in capital letter which isnot present then we also get -1 as didnt find.

# Example :-

# finding index of a character in the main string -
print(text.find('o')) # 0 --index
print(text.find('w')) # 1 -- find() always give the first occurance in the string, from starting index

print(text.find('z')) # -1 -->if -1 index returns tht means that char is not present in the string

#fnding or Searching index of first character occurance in the main string
print(text.find("very")) # 14 --> the first index occurance of the sustring in the main string.
print(text.find("Very")) # -1 --> case sensitive python, so didnt found and retuned -1.
print(text.find(" "))  #4 --> the first index occurance of white space in the string.

# Note : 'in' operator and find() method differnce is that find() method returns the starting index of sub-string and 'in' operator returns the true or false value of sub-string or not.

#3. String Slicing : - String slicing in Python is a way to get specific parts of a string from any position by specifying using start_index(inclusive), end_index(exlusive) and step values. 

# syntax : text[start_index : end_index(Exclusive i.e Not Included) : StepValue ] 

#  where start_index(Optional) --> Starting index (inclusive). Defaults is 0 Index. 
# end_index(Optional) ---> Stopping index (exclusive means Not Included Just before this index). Defaults is till the end of the string.

# stepValue (Optional) ---> Interval between Slicing. A positive value slices from left to right, while a negative value slices from right to left. If omitted, It defaults value is 1 which means slicing from left to right with no skipping of characters. If value is  2 ---> slice out with skipping every next character. If value is -1 ---> Slice out from right(end) to left(start) with no skipping of characters.

# example : slice out 'cd' from string 'abcdef' -  str[2:4] --> cd


# text[:] --->If we skip with start nd end index, then it slice out complete string i.e we will get copy of original string.

# text[:end_index] ---> slice out from start index i.e 0 by default to till provided end_index(exclusive).

# text[start_index:] ---> slice out till last index of the string from provided start_index.

# text[-negative_start_index :] ---> slice out from negative indexing i.e from provided negative_start_index to till negative_end_index(exlusive).

# text[::] --->If we skip start_indx, end_index and step_value then it slice out complete string with default stepValue i.e +1 which is no skipping in slicing out from left to right.
# text[::-1] --->If we skip start nd end index but step value is -1 means slice out entire string from right(end) to left(start) which is basically we get REVERSE string of main string.

#text[::n]  ---> Get Characters from sting with 'n' Specific Intervals

#  Example : 

myTxt = "College Wallah"

# Want 'Wallah' -
print(myTxt[8:]) # wallah

# Want 'Wall' -
print(myTxt[8:12]) # wall

# Want 'Wallah' with negative indexing -
print(myTxt[-6:])

# Get all characters with negative -1 stepValue which is From Right to start string slicing - //REVERSE STRING -
print(myTxt[::-1]) # hallaW egelloC

# Get Every second character from string -
print(myTxt[::2]) # CleeWla

# Every Every third character from index 1 to 8 (exclusive)
print(myTxt[1:8:3]) # oe

# Case-Conversion  -

# 4. upper() and lower() : It always return a new string with converting all characters into Upper Case or Lower Case, and remember it doesnot modify original string.

str1 = "new york is good city"
upper_case = str1.upper()
lower_case = str1.lower()
print(upper_case) # NEW YORK IS GOOD CITY
print(lower_case) # new york is good city

# 5. capitalize() & title() : capitalize() method, It only capitalize first starting character of the string.

firstChar_cap = str1.capitalize()
print(firstChar_cap) # New york is good city

# title() : It capitalized first char of each words from the pragraph or string. 

firstAll_cap = str1.title()
print(firstAll_cap) # New York Is Good City

# 6. swapcase() : It returns a string where all the upper case letters are lower case and vice versa.

str2 = "New York Is a Good City"
swap_Cases = str2.swapcase()
print(swap_Cases) #



# 7. strip() : For stripping/removing any trailing whitespace i.e white space from either of the sides from the string. It doesnot effects the original string.

# lstrip() and rstrip() : removes only the left white space and right white space from the string.

str2 = "    Hello world     "
print(str2.strip()) # Hello world
print(str2) #     Hello world  (Remains the white spaces in the original string)

print(str2.lstrip()) # removes left white space i.e left strip only
print(str2.rstrip()) # removes right white space i.e right strip only


# 8. replace() method : It returns a new string with replace all found character or sequence of character from existing string and If doesnot found character(with case-sensitiveness), returns the original string without any replacement.

# There is optional third argument which helps to control how many found character or substring will replace from original string.

# replace() method doesnot modify the original string. 

# Syntax : text.replace(existin_substring, new_substring, count)

# count(Optional) --->  To specify

# Example : 

text = "HEllo world, this is URI Yadav, what a beautiful world this is! "
new_text = text.replace("world", "woowo")
print(new_text) # HEllo woowo, this is URI Yadav, what a beautiful woowo this is!
print(text) # original string remain same.


# Only change 'world' once, from first occurance in the string -
print(text.replace("world", "hey", 1))

# Didnt not find the exact substring with case-sensitiveness, then it will return original string as well -
print(text.replace("World", "hey")) # Original string


#9. split() : It is use to split main string into substring or into characters depends on which seperator passed(bedefault space sperator passed i.e minimum one space length) and alwasy returns a list consiting all the substrings.

# If seperator doesnot found in the string, then returns the list with one item containing entire string.

# Syntax : text.split( seperator(Optional), maxsplit_count(Optional) )


# seperator(Optinal) --->  Specifies separator like white_space(" ") i.e minimum one space OR, comma(,) which ever present in the string; to use when splitting the string. By default any whitespace(" ") i.e minimum one space string length is seperator.(Empty strings are those with zero string length which are Falsy Value). 

#maxsplit_count ---> How many times found separator will split and will not split further from original string. By default, all occurrences split.

s1 = "ria pia sia tia mia"
# Split by space(" ") present in the string
print(s1.split()) # ['ria', 'pia', 'sia', 'tia', 'mia']
print(s1) #AS it is

s2 = "ria, pia, sia, tia, mia"

# Split by comma(,) in the string -
print(s2.split(",")) # ['ria', ' pia', ' sia', ' tia', ' mia']

# # Split by comma(,) with only two occrance split rest will come with single item in list -
print(s2.split(",", 2)) # ['ria', ' pia', ' sia, tia, mia']

# If doesnot found seperator in string, returns a single item in list with containing entire string
print(s2.split("z"))

# 10. splitlines() : It is usefull when we need to break the string from line break into substrings of list. If line break doesnot found in the string, then returns the list with one item containing entire string.

# Syntax : text.splitlines( keeplinebreaks(optional) )

# keeplinebreaks (Optional) --> Specifies if the line breaks should be included or not. Bedwfault included i.e value is False not if user doesnot want to include then pass 'True' Value and it will print as it is.

my_text = "Thank you for the music\nWelcome to the jungle"
print(my_text.splitlines()) # ['Thank you for the music', 'Welcome to the jungle']

my_text2 = "Thank you for the music Welcome to the jungle"
print(my_text2.splitlines()) # ['Thank you for the music Welcome to the jungle']

# Do not want to include line_break -
my_text3 = "Thank you for the music\nWelcome to the jungle"
print(my_text3.splitlines(True)) # ['Thank you for the music\n', 'Welcome to the jungle']

# Supose 
my_data = ''' 5
10
4
3
6
2
4

'''
# As we know each data present after line_break-
print(my_data.splitlines()) #[' 5', '10', '4', '3', '6', '2', '4', '']

# With removing space from start and end -
print(my_data.strip().splitlines()) # ['5', '10', '4', '3', '6', '2', '4']

# 11. join() : It is string method use to convert a iterable object(like tist, tuple etc) into string with providing a seperator(like once space string, #, comma etc) to join all items from list, tuple into a single string.

# Syntax : "<provide_seperator_value_in_string".join(<iterable_object>)

# Note : A string value must be specified as the separator.

mytuple = ("hey", "rowdy", "how", "are you!!")
myseperator = " " #Must be a string

myString = myseperator.join(mytuple)
print(myString)

mylist = ["hey", "rowdy", "how", "are you!!"]
final_string = " ".join(mylist)
string_with_hash = "#".join(mylist)

print(final_string) # hey rowdy how are you!!
print(string_with_hash) # hey#rowdy#how#are you!!

# 12.  startswith() and endsWith() : method returns True if the string starts with the specified value, otherwise False.

# Syntax : text.statrswith(character, startSearching, endSearching)

# Character --> 

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)



# --------------------------------------------------------------------------

# Example : - 
'''
Q1: Consider a string: 'The unexpected always happens".

Assign this string to a variable: text.
Print the string.
Print the length of the string.
Check if the phrase 'pp' is present in the string.
Print the substring from O till 10th index
Replace 'always' with 'never'.
Add "no matter what" to the string.
Print the final string.


'''

text = "The unexpected always happens"
print(text)
print(len(text))
print("pp" in text)
print(text[:11])
print(text.replace("always", "never"))
final_text = text + " no matter what"
print(final_text)


# Q2: Write a Python function that checks if the given string is a palindrome or not -

# Input : mama
# ouput : True

# Concept: Palindrome : Same from front and back sides or Reverse the string and if it matches with original then it is palindrome string.
# Ex:  s = "abccba" ----Reverse---> "abccba" (Same so yes palindrome)
# Ex:  s1 = "abcd" ----Reverse---> s2 = "dcba" (s1 nd s2 Not Same so Not palindrome)
# Ex : str = "abc de d cba" ---> It's also a palindrom string.


# Way1 : using String Slicing from backwards -
# Steps : -
# 1. remove white spaces between the string(with replace method)
# 2. Convert all characters to lowerCase, as python is caseSensitive
# 3. Then, Reverse and Check(compare)

def check_palindrome(str):

    # Cleaning the string
    cleaned_str = ( str.replace(" ","") ).lower()

    reverse_str = cleaned_str[::-1]

    return reverse_str == cleaned_str

print("It is Plindrome") if check_palindrome("abcd") else print("It is Not Palindrome")
print("It is Plindrome") if check_palindrome("abccba") else print("It is Not Palindrome")
print("It is Plindrome") if check_palindrome("abc de d cba") else print("It is Not Palindrome")
print("It is Plindrome") if check_palindrome("a man a plan a canal Panama ") else print("It is Not Palindrome")

  
#Q3: Write a Python Function that Prints all words that are of even length in the given string -
INPUT = "we love to code in the python" 
OUTPUT = "we love to code in python" 

def even_words(para):
     para_list = para.strip().split()

    #Now we need to loop over each list items with applying some operations, we use for-loop
     final_str = ""
     for item in para_list:
          if len(item) % 2 == 0 :
               final_str += item + " "
            
     return final_str.strip() # Remove trailing space
 
print(even_words("we love to code in the python"))
print(len(INPUT))
print(len(OUTPUT))

# OR, We could do the same with storing into List then making it into string with join() method.

def even_words2(para):
     para_list = para.strip().split()

    #Now we need to loop over each list items with applying some operations, we use for-loop
     final_list = []
     for item in para_list:
          if len(item) % 2 == 0 :
               final_list.append(item)
          
     final_str = " ".join(final_list) #Joined all List items into one string with seperator one space(" ").
     return final_str
 
print(even_words2("we love to code in the python"))

'''
#MCQ : -

MCQ -1 

i) What will be the output of the following Python code?
print ("Hello {name1} and {name2}" . 'foo' ,	name2=' bin'))

a. Hello foo and bin   (Correct)
b. Hello {name1} and {name2}
c. Error
d.Hello and


MCQ-2
What will be the output of the following code snippet?
str1 = "6/4"
print ("str1")

a. 1
b. 6/4
c. 1.5
d.str1  (Correct)  



MCQ-3
What will be the output of the following code snippet?
str1= " Information"
print(str1[2:8])
a. format  (Correct)
b. formatio
c. orma
d.ormat



MCQ-4
What will be the output of the following code snippet?
str1=" Application"
str2 = str1.replace('a', 'A')
print(str2)
a. application
b. Application
c. ApplicAtion  (Correct)
d. applicAtion


MCQ-5
What will be the output of the following code snippet?
str1 = "poWer"
strl.upper()
print(str1)
a. POWER
b. Power
c. power
d. poWer (Correct)



'''