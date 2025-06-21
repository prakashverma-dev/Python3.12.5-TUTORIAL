

#What is Strings in python : - A string is a sequence of characters written within single quotes(' '), doublequotes(" "), thriple quotes ('''  '''), When strings defined with single or double quotes known as 'SingleLine Strings' and strings defined with tripple quotes known 'Multiline Strings' means It can be break into multiple lines but if you try to break singleline strings then python will throw an error.

# Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. 


# Syntax : -
# Using Single quote: ' Hello, World! '
# Using Double quotes: "Python is awesome .
# Using Triple quotes/MultiLine String: ' ' 'Strings in Python are super fun' ' 

#Multipline String:  Multiline strings uses in form of a paragrapgh where we can break the lines and more flexibilty in writting strings and It is also use to formate long string as it is written like with added extra space or next line etc, It get printed as we have written inside '''     ''''.

paragraph = ''' This is a multiline string.
You can write multiple lines within triple quotes. '''


course = "Python programming"
message = '''
Hi John ,
this is Prakash


Blah Blah.... '''

print(message)


# Note : If we declare any strings without assigning to any variable, then python intepreter will ignore those strings, and treated them as a comment.Thuse we can place any comments inside it -
'''
this is strings without assignd to any variable so behaving like a comment.

'''


# Strings are Immutable datatype, that is can not change once It created means Origial string stored in any varibale will remain same, though we can create a new string by manipulating original string. Ex:

name = "Rowdy Prakash Hai" #Original String

# Now Applying String Manipulation/Let's Capitalize given string in upper case -

uppercase_str = name.upper()
print(uppercase_str) # ROWDY PRAKASH HAI

# Now check Original String Data is manipulated/Changed or not -
print(name) # Rowdy Prakash Hai (NO IT IS NOT)

# Thus, Hence Proved, strings datatype are immutable in nature at runtime in program.




#Creating Strings :-

name1 = 'Pysics Wallah'
name2 = "College Wallah"
name3 = '''MBA Wallah'''

print(name1, name2, name3)
print(type(name1), type(name2), type(name3))
      
#Thus, These all variables belong to class 'str'.

# --------------------------------------------------------------------

# Array-like indexing In Strings : - Like an array string have the same indexing for each characters which starts from 0 and goes upto one less than string length i.e string_length - 1, Means If string_length=4; last index= will be 3.

# To access characters from string, use array's square bracket -


# a) Accessing String characters with Positive Indexing : -

text = "Hello World"

print(text[0]) #H --->  Prints first character of string
print(text[1]) #e  --->  Prints second character in the string

print(text[len(text) -1 ]) #d  ---> Prints last char in the string

# Also, To Print last character in the string -
print(text[-1])  #Also, Prints last character of string


#Negative Indexing : IF we directly want to access string chars from backwards/ends, we use negative indexing which starts from -1 from last character and goes like -2, -3,..so on. to till first character Ex: -

'''
    a  b  c  d  e
    0  1  2  3  4   ---> Positive Indexing
   -5 -4 -3 -2 -1   ---> Negative Indexing

'''
# b) Accessing String characters with Negative Indexing : -

print(text[-1])  #ned or last char in the string
print(text[-2])  #before end char in the string


print(text[0]) # Prints first character of string



# ---------------------------------------------


#Traversing a string/ Looping Though a string : -

text = "Hello World"

#i) using for-in loop -

for i in text:
    print(i) # here, i represents each characters of the string.
    

#ii) using for-in with accessing index ( via range() function) -

for i in range(len(text)):
    print(i)  #Here, i represent the indexing of string.
    print(text[i]) # Here, we accessing characters corresponding to its index.



#iii) using for-in with accessing indexing (with help of enumerate() function) -
for index, char in enumerate(text):
    print(index) # index represent the indexing of string.
    print(char) # accessing characters directly from string.


#iv) Using a while loop -
i = 0 #indexing of string
while i < len(text):
    print(i) # Will get indexing frm string
    print(text[i]) # Will get the character corresponding to indexing
    i += 1 #Updating the indexing



#v) using list comprehension : we make string into list -
new_list = [char for char in text]
print(new_list) 

for i in new_list:
    print(i)

# OR, COnvert first text into list - 
my_list = list(text)
print(my_list)  # Same as above

for i in my_list:
    print(i)

#Also, we can traverse through each words in a string -

# Firstly we need to convert strings into list with once space found in thes tring using split() method of string, which by default finds once space in the originl string to split it into items of lists -

words = text.split()
print(words) # ['Hello', 'World']

# Now, can traverse through each word -
for i in words:
    print(i) # i represents each item present in the list



# Checking character or substring in main string using Membership operator -

# We can test if a char or Phrase or substring exists within a string or not, using the keyword in, and returns True and False.

txt = "The best things in life are free!"
print("free" in txt) #True
print("expensive" not in txt) # True

# With if-statemnt -
# a) Print 'yes' if "free" is present
if "free" in txt: print("Yes!")
# b)Print 'yes' if "expensive" is NOT present:
if "expensive" not in txt: print("Yes!")

# ------------------------------------------------------------------

# Concatenating and Repeating Strings : We can concatenate two or more strings into one using + operator and can repeat a string multiple times using * operator.

# Concontenating Using Plus(+) operator -
str1 = "Hello Rowdy"
str2 = " this is a great place"

print(str1 + str2)
print(str1 +" "+ str2) # To add a space between two strings

#Repeating a string 3 times Using Star(*) operator -
str = "Hello"
print(str * 3) # HelloHelloHello



# Formatting Strings :- It is use to insert any variable expressions into a string with more concise way. Python provides several ways to include variables inside strings -

# Example : - 

fruit1 = "mango"
fruit2 = "apple"

newfruit = "I have fruits "+ fruit1+ " and "+ fruit2 

# It can better formatted using Python formate strings, which are -

# a) using f-string : We can use f or F to formate any strings with adding up any python expression into string using curly braces to embedd any python expression or variable into string. It will alwasy return a string in resultant -

# Syntax : f or F"Ram is good boy he is {age} with calculated {3+5} roti"

new_fruit = f"I have fruits - {fruit1} and {fruit2}"
new_fruit2 = f"I have fruits - {fruit1} and {fruit2} have length : {len(fruit1) } and {len(fruit2)} with {10} count"

print(new_fruit)
print(new_fruit2)

# b) using format() method : - Another way to format strings is by using format() method where we add varivales with placeholder place using curly braces and later we add their resoective values with .formate() method with passing all values seperated with comma(,) -

check1 = "Wow"
check2 = "Rowdy"
result = "Hey They are good {} and name is {}".format(check1, check2)
print(result)

# OR, with passing a reference variable names
result2 = "Hey They are good {quality} and name is {name}".format(name = check2, quality = check1)

print(result2)



#Escape Characters In String : - These are special characters start with backslash(\) followed by either python defined single characters. It only used inside string i.e "  " and The purpose of using escape next character used in string and gives some different meanings like -


# Code	      Result
# \' or \"	    Add Single or Double Quote In Ouput
# \\	        Backslash	
# \n	        New Line	
# \t	        One Tab Space	
# \b      	    Back Character Remove	
# \r	        Carriage Return	
# \f      	    Form Feed	
# \ooo      	Octal value	
# \xhh    	    Hex value


# Example : Sometimes we need to highligh a paragraph with double quotes in result, which if we do so get an error if -

# txt = "We are the so-called "Vikings" from the north." //Get error


# a) Want to escape double quote followd by a double quotes in string - 
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# OR, txt = 'We are the so-called "Vikings" from the north.' #result can be fullfil in this way as well.

# Note: whenever we use escape character(\) inside string and just after character gets ignored by python compiler/interpreter.

print("Python \"Programming"); # Python "Progamming
print('Tom\'s friend is not good'); # Tom's friend is not good
print('Tom friend is \\ good'); # Tom friend is \ good
print('Tom friend is \n good'); # Print 'good' word in next line
print('Tom friend is \t good'); # One tab space between output
print('Tom friend is\b good'); # Remove just back character in output

# Note : \(backslash) ---> escape character
    #   \"(backslash  + any single character) ----> escape sequence




    
